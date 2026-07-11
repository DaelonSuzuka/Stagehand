# Plan: Roadie Engine Hardening

Findings from a review of `src/stagehand/roadie/engine.py` (2026-07). The engine's
architecture is sound — isolated QuickJS contexts, nested-Proxy FFI, JSON
auto-serialization at the boundary — and none of these items change it. They close
gaps that will matter once user-authored scripts are the normal workload.

**Canonical-copy note:** this file (`src/stagehand/roadie/`) is the live engine.
The standalone repo at `~/projects/roadie` is a **dormant ancestor** (it began as
a full Stagehand rewrite on NiceGUI and shrank to just the engine; see its lode
for the pivot rationale). Do not sync changes to it. If the engine is ever
extracted and published under the Roadie name, see H-7 first.

Items H-1 and H-2 were empirically verified in a live interpreter, not just read
off the source. Tests go in `tests/test_roadie_engine.py`, which already covers
the engine well.

---

## H-1: No execution time limit — an infinite loop hangs the app

**Where:** `Engine.create_context()` — sets a 50MB memory limit and nothing else.

`engine.execute('while(true){}')` blocks the calling thread forever. Since the
entire premise is running user-authored action scripts, an accidental infinite
loop must not freeze Stagehand. **Verified:** the `quickjs` binding supports
`ctx.set_time_limit(seconds)` and `ctx.set_max_stack_size(bytes)`; with a 1s
limit, the loop above raises `JSException: InternalError: interrupted` at almost
exactly 1.00s.

**Fix:** in `create_context()`, next to the memory limit:

```python
ctx.set_time_limit(5)                    # actions are short; 5s is generous
ctx.set_max_stack_size(1024 * 1024)      # runaway recursion
```

Make both values `Engine.__init__` parameters with these defaults.

**Edge cases:**
- The REPL / code-editor path uses `create_context()` for a *persistent* context.
  The time limit applies per-eval (not cumulative), so it's safe there too — but
  confirm this empirically with two sequential 3s-total evals under a 5s limit
  before assuming it.
- The interrupt surfaces as `InternalError: interrupted` in
  `ExecutionResult.error` — map it to a friendlier message
  (`'script exceeded the {n}s time limit'`) in `execute()`/`evaluate()`, since
  end users will see this string.
- `validate()` builds its own bare context; it wraps code in a function and never
  executes, so it needs no limits. Leave it alone.

**Test:** `execute('while(true){}')` returns (does not hang) within ~limit
seconds, `result.ok` is False, and the error mentions the time limit.

---

## H-2: The Proxy's catch masks every real service error — CONFIRMED CLASS OF BUG

**Where:** `_STAGEHAND_BOOTSTRAP`, the nested Proxy's method wrapper:

```js
try {
    var raw = eval(ffiName + "(" + argExprs.join(",") + ")");
    return __autoUnwrap(raw);
} catch(e) {
    throw new Error("stagehand." + serviceName + "." + methodName + " is not available");
}
```

*Any* exception from the Python service method — wrong argument count, a network
failure, a bug — is swallowed and replaced with "not available". A user whose OBS
call fails will be told the method doesn't exist. Debugging service problems
through this is impossible.

**Fix:** separate "method doesn't exist" from "method failed":

```js
return function() {
    var fn = globalThis[ffiName];
    if (typeof fn !== "function") {
        throw new Error("stagehand." + serviceName + "." + methodName + " is not available");
    }
    return __autoUnwrap(fn.apply(null, arguments));
};
```

Note this also implements H-3 (no `eval`) — do them together.

**Edge cases:**
- **First, verify how the binding surfaces Python exceptions.** Write a throwaway
  service method that raises `ValueError('boom')` and check what
  `result.error` contains after the fix. If the binding converts Python
  exceptions to JS exceptions with the message intact, you're done. If it
  produces something opaque, wrap `_dispatch` in try/except and re-raise with a
  structured message (`'{service}.{method} failed: {exc}'`) — but only if needed.
- `tests/test_roadie_engine.py` has a test asserting `'not available'` for
  unknown methods — that behavior is preserved. **Add** the missing case: a
  service method that raises must surface its real message, not "not available".
- `fn.apply(null, arguments)` replaces the eval'd argument-expression trick;
  `arguments` is fine in the ES5-style bootstrap.

---

## H-3: Replace `eval` with `globalThis` lookup in the bootstrap

Covered by the H-2 fix above. Rationale recorded separately because it stands
alone: `eval(ffiName + "(...)")` is slower, and user code in the same context can
shadow `eval` (`eval = null`) and break every subsequent service call in that
context. `globalThis[ffiName]` is immune and direct. QuickJS supports
`globalThis` (ES2020) — verify once with `engine.evaluate('typeof globalThis')`
before relying on it; if it's somehow absent, fall back to capturing the global
object at bootstrap top (`var __global = this;`).

---

## H-4: Auto-unwrap heuristic mangles JSON-looking strings

**Where:** `__autoUnwrap` in the bootstrap + `Service._dispatch`.

Any service method returning a *string* that parses as JSON (`"[1,2]"`,
`"{\"a\":1}"`) is silently converted to an array/object in JS, because unwrap
guesses based on the first character. `_dispatch` controls both ends of the
boundary, so stop guessing — mark the payload:

```python
# _dispatch:
if isinstance(result, (dict, list)):
    return '\x00json:' + json.dumps(result)
return result
```

```js
function __autoUnwrap(val) {
    if (typeof val === "string" && val.charCodeAt(0) === 0 && val.slice(1, 6) === "json:") {
        return JSON.parse(val.slice(6));
    }
    return val;
}
```

**Edge cases:**
- The NUL byte cannot appear in legitimate service return strings (it would have
  to be deliberately constructed), which is what makes the sentinel safe. Keep it
  as `\x00` — a printable marker like `@json:` COULD legitimately occur.
- The bootstrap's `stagehand.load()` also calls `__autoUnwrap`. After this change
  it becomes a pass-through for everything `stagehand.save()` stored (which is
  only FFI-representable primitives today) — that's correct behavior; saved
  strings finally round-trip unmangled. If object save/load is wanted later,
  apply the same sentinel in the save path (`__save(k, SENTINEL + JSON.stringify(v))`
  for objects) — optional, separate change.
- `ExtensionToServiceAdapter._dispatch` duplicates the dict/list serialization —
  update it identically or, better, have it call `Service._dispatch`.
- Update the existing auto-unwrap tests; add the regression case: a service
  returning the literal string `"[1,2]"` must arrive in JS as a string.

---

## H-5: Write down the concurrency policy for services

Not a code change — a policy doc (add to `lode/config/services.md` or
`lode/sandbox/runtime.md`):

> **Actions are ISR-shaped:** short, synchronous, run-to-completion. FFI calls
> block the engine, and the engine runs on the main thread (see the threading
> item in [migration-review-2026-07.md](migration-review-2026-07.md)). Therefore
> **slow service operations must be fire-and-forget**: the service method queues
> the request and returns immediately. Results that matter later re-enter the
> system as fire events, not return values. A service method that blocks for
> more than ~a frame is a bug.

This constrains every future service author (HTTP, OBS round-trips) and needs to
exist before the first slow service gets written. It also means H-1's time limit
is a backstop, not a scheduling mechanism.

---

## H-6: Cherry-pick `benchmark_context()` from the dormant repo

`~/projects/roadie/src/roadie/engine.py` has a `benchmark_context(iterations)`
method (averages the per-phase timings over N context creations) that the
Stagehand copy lacks. Copy it in verbatim. Rationale: every `execute()` builds a
fresh context and re-evals all helpers + task-file sources, so per-context cost
grows linearly with the user's task library. This method is the measurement tool
for noticing when that becomes a problem (and for evaluating fixes like
precompiled helper bytecode or a context pool — neither needed today).

---

## H-7: Pre-extraction checklist (deferred — not today's work)

Recorded so it isn't rediscovered: if the engine is extracted back to a
standalone package under the Roadie name, the ONE decision locked in by user
scripts is the global namespace (`stagehand.print`, `stagehand.obs...`). Before
any external release: make it a constructor parameter
(`Engine(namespace='stagehand')`) so published-Roadie users get `roadie.*` while
Stagehand keeps `stagehand.*`. Everything else (packaging, repo slimming, test
migration) can be decided at extraction time.

---

## Order

H-2+H-3 together (same lines of code), then H-1, H-4, H-6 in any order, H-5
whenever. All are independent of the migration-review items except where H-5
references the threading fix.
