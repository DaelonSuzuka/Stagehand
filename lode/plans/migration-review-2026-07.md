# Migration Review Findings (2026-07)

Code review of the config-centric migration as of `3c30160` (action pipeline,
fire sources, services). The migration was **known to be mid-flight** when
reviewed — these are not "bugs someone shipped," they're the gap list between
current state and the design in [config-format.md](config-format.md). Recorded so
the gaps don't have to be rediscovered when work resumes.

Engine-specific items live in [roadie-hardening.md](roadie-hardening.md).

The first three items (M-2, M-3, M-4) define the **fire-event contract**; fix
them before wiring the pipeline in, because every future trigger source (device,
web, timer) will be written against whatever contract ships first.

---

## M-1: ActionPipeline is never instantiated

`src/stagehand/action_pipeline.py` defines the wiring singleton; nothing
constructs it — no import anywhere in the app. `StartupFireSource` is likewise
defined (`fire_sources.py`) and never created, so `startup` triggers can never
fire. Expected mid-migration state, but the commit message says "wires everything
together at app startup," so: recorded. Wiring it in is blocked on M-2/M-3/M-4.

## M-2: Keyboard combos are never composed

`KeyboardFireSource` emits one fire event per individual key (`'ctrl'`, `'h'`)
and never builds combo strings — but the config format (and the seed config's own
default action, `ctrl+shift+h`) expects `{'keyboard': {'key': 'ctrl+shift+h'}}`.
No fire event will ever carry that key: **the default Hello World action cannot
fire.** The docstring's `'event': 'hotkey'` variant is never emitted.

Fix direction: track the held-modifier set in the fire source and emit composed,
canonically-ordered combo strings (`ctrl+shift+h`) alongside or instead of bare
keys. pynput's `HotKey` helper (already imported) can canonicalize.

**Trap within the trap:** with Ctrl held, pynput delivers `KeyCode.char` as the
*control character* (`'\x0c'` for ctrl+l), not `'l'` — `_normalize_key` passes
that through, so even bare-key matching breaks while modifiers are down. Combo
composition must map control chars back to letters (or use `key.vk` /
`HotKey.parse` canonicalization) — test on Windows AND Linux, the two platforms
deliver different things.

## M-3: Every matching action fires twice per keystroke

`TriggerConfig.matches()` (config.py) requires trigger params to be
present-and-equal in the event — a trigger `{key: 'a'}` says nothing about
`event`, so it matches both the `press` AND `release` fire events. Decide the
contract: either matching defaults to press-only when `event` is unspecified
(recommended — principle of least surprise for "when I hit the key"), or the seed
config must always write `event: press` explicitly. Encode the decision in a
test.

## M-4: Fire events execute on the pynput listener thread

`registry.on_fire()` is called directly from the pynput callback — so QuickJS
execution, service calls, and the `on_action` UI-feedback callbacks all run off
the Qt main thread. Widget access from there is a crash; on Windows the callback
runs inside the low-level keyboard hook, so a slow task lags keyboard input
**system-wide**.

Fix direction: the fire source already has Qt signals — route fire events to the
registry through a queued signal connection (`fire_event = Signal(dict)`
connected to `registry.on_fire`) instead of the direct call. Everything then
executes on the main thread, and the H-5 policy (services must not block) plus
H-1 (script time limit) in roadie-hardening.md keep the main thread healthy.

## M-5: Synthetic-input feedback loop

`KeyboardService.tap()` injects OS-level key events; the global pynput listener
hears them and turns them back into fire events. An action triggered by `'a'`
whose task types `'a'` is an infinite loop (via the OS, so no stack to blow —
it just runs forever). Needs suppression: the service records keys it is
synthesizing (with a small time window) and the fire source drops matching
events. Test the window on Windows — injected-event timing there is loose.

## M-6: Named tasks don't work end-to-end; `stagehand.register()` doesn't exist

The design (config-format.md) has task files calling
`stagehand.register({id, run})` — the engine implements no such function. The
Proxy would return a service-proxy *object* for `stagehand.register`, and calling
it throws. Meanwhile:

- `ActionPipeline` injects task-file sources as helpers into **every** context —
  one task file using `register()` breaks every subsequent context creation.
- `TriggerRegistry._execute_task` looks up named tasks by **filename stem** and
  re-evals the whole file with `var _params = {...}` prepended — nothing ever
  calls a `run()` function, so `obs.switchScene: {scene: Live}` can't work.

This is the biggest open **design decision**, not just a bug: either implement
`register()` in the bootstrap (collect registrations at helper-eval time, invoke
`run(_params)` on execution), or drop it and commit to the file-per-task
convention (file `obs.switchScene.js`, whole file is the task body, `_params` in
scope). Decide before building the task-editor UI, which will bake the choice in.

## M-7: KeyboardService does no key-name resolution

The commit message claims resolution happens in services, but
`KeyboardService.tap('ctrl')` passes the raw string to pynput's
`Controller.press()`, which accepts only single characters or `Key` enums —
`ValueError` for `'ctrl'`, `'enter'`, `'space'`, any combo. `MouseService` got
`_resolve_button`; keyboard needs the equivalent: name → `Key` enum map plus
combo parsing (`'ctrl+shift+l'` → press ctrl, press shift, tap l, release in
reverse order).

## M-8: MouseService.scroll ignores its direction argument

Docstring says `scroll('down', 3)`; the implementation parses `direction` as an
int (0 for `'down'`) into dx and passes `steps` raw as dy — so `scroll('down', 3)`
scrolls **up**. Map `'up'/'down'/'left'/'right'` to signed dx/dy explicitly.

## M-9: Two parallel Engines

`Sandbox` builds its own `Engine`; `ActionPipeline` builds another. Two
persistence stores (`stagehand.save`/`load` don't cross), two service sets, two
print sinks. Tolerable during transition; the endgame is one engine instance —
likely ActionPipeline owns it and Sandbox becomes a view over it. Decide when
wiring M-1.

## M-10: Smaller items

- `Sandbox.eval()` discards `result.output` — callers expecting a value get
  None. Related: `SandboxFilterWidget.check()` evals and unconditionally
  `return True` — the sandbox filter is a no-op.
- `trigger_registry._execute_task` uses `__import__('json')` — import at top.
- `ActionPipeline.reload_helpers` pokes `engine._helpers` — add
  `Engine.clear_helpers()`.
- `roadie/adapter.py.__init__` normalizes `name` twice — second if/else is dead.
- Config parsing uses `assert` for validation — vanishes under `-O`, and
  hand-edited YAML (the whole point) deserves real error messages with the
  offending snippet.
- `trigger_registry.py` type hints: import `Callable` from `collections.abc`
  (beartype deprecation warnings in the test run).
