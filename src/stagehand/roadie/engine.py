from __future__ import annotations

"""
Roadie Engine — QuickJS-based evaluation engine.

Action code runs in isolated QuickJS contexts. Only explicitly injected
callables are available to user code. The boundary is structural, not
conventional.

QuickJS contexts support direct FFI via add_callable() — Python functions
are callable from JS with full return value propagation. No outbox/inbox
bridge needed.

Three execution modes match Stagehand's sandbox API:
- execute(code)  — fire-and-forget, like Sandbox().run()
- evaluate(code) — return value, like Sandbox().eval()
- validate(code) — syntax check only, like Sandbox().compile()

For the code editor (REPL), use create_context() to get a persistent
context where variables accumulate across evaluate() calls.

Service methods returning dicts/lists are auto-serialized to JSON strings
at the FFI boundary, then auto-unwrapped in JS via Proxy — so JS authors
see native objects, not JSON strings. Primitives pass through unchanged.
"""

import json
import time

import quickjs

# JS bootstrap injected into every QuickJS context.
# Provides:
#   - __autoUnwrap(): detects JSON strings from FFI returns and parses them
#   - Nested Proxy on stagehand that dynamically routes service.method()
#     calls to __service_method FFI callables, with auto-unwrap
_STAGEHAND_BOOTSTRAP = r"""
function __autoUnwrap(val) {
    if (typeof val === "string") {
        var c = val.charAt(0);
        if (c === "{" || c === "[") {
            try { return JSON.parse(val); } catch(e) {}
        }
    }
    return val;
}

stagehand = new Proxy({
    save: function(k, v) { __save(k, v); },
    load: function(k) { return __autoUnwrap(__load(k)); },
    print: function() { __print([].slice.call(arguments).join(" ")); }
}, {
    get: function(target, serviceName) {
        if (serviceName in target) return target[serviceName];
        return new Proxy({}, {
            get: function(methodTarget, methodName) {
                var ffiName = "__" + serviceName + "_" + methodName;
                return function() {
                    var args = [].slice.call(arguments);
                    var argExprs = [];
                    for (var i = 0; i < args.length; i++) {
                        argExprs.push("args[" + i + "]");
                    }
                    try {
                        var raw = eval(ffiName + "(" + argExprs.join(",") + ")");
                        return __autoUnwrap(raw);
                    } catch(e) {
                        throw new Error("stagehand." + serviceName + "." + methodName + " is not available");
                    }
                };
            }
        });
    }
});

var roadie = roadie || {};
roadie.helpers = roadie.helpers || {};
"""


class Engine:
    """
    Creates and manages isolated QuickJS evaluation contexts.

    Three execution modes:
    - execute(code) — fire-and-forget action execution (fresh context)
    - evaluate(code) — return a value (fresh or persistent context)
    - validate(code) — syntax check only, no execution

    For the code editor (REPL), use create_context() to get a persistent
    context where state accumulates across calls.

    Timing: create_context() records phase timings in the returned
    context's _roadie_timings dict for profiling startup cost.
    """

    def __init__(self):
        self._services: dict[str, 'stagehand.roadie.engine.Service'] = {}
        self._helpers: list[str] = []  # JS source strings
        self._persistence: dict = {}  # stagehand.save/load store
        self._print_callbacks: list = []  # output subscribers
        self._last_timings: dict[str, float] = {}  # timing data from last create_context()

    def register_service(self, service: 'Service') -> None:
        """Register a service that provides callables to JS contexts."""
        for name in service.names:
            self._services[name] = service

    def register_helper(self, js_source: str) -> None:
        """Register a JS helper to be injected into every context."""
        self._helpers.append(js_source)

    def on_print(self, callback) -> None:
        """Register a callback for stagehand.print() output. Signature: callback(message: str)"""
        self._print_callbacks.append(callback)

    def create_context(self) -> quickjs.Context:
        """
        Create a fresh isolated QuickJS context with the full API injected.

        The context lifecycle:
        1. Create fresh QuickJS context (no built-in I/O)
        2. Set memory limit (50MB)
        3. Inject core FFI callables (save, load, print)
        4. Bootstrap stagehand Proxy + autoUnwrap + roadie.helpers
        5. Register service methods as FFI callables
        6. Inject user helpers
        7. Ready for action code evaluation

        Timing data is stored in engine._last_timings after each call.
        """
        timings: dict[str, float] = {}
        t0 = time.perf_counter()

        ctx = quickjs.Context()
        timings['create_context'] = time.perf_counter() - t0

        t1 = time.perf_counter()
        ctx.set_memory_limit(50 * 1024 * 1024)  # 50MB
        timings['set_memory_limit'] = time.perf_counter() - t1

        # Core APIs — direct FFI
        t2 = time.perf_counter()
        ctx.add_callable('__save', self._save)
        ctx.add_callable('__load', self._load)
        ctx.add_callable('__print', self._print)
        timings['add_core_callables'] = time.perf_counter() - t2

        # Bootstrap stagehand Proxy, autoUnwrap, and roadie namespace
        t3 = time.perf_counter()
        ctx.eval(_STAGEHAND_BOOTSTRAP)
        timings['eval_bootstrap'] = time.perf_counter() - t3

        # Register service methods as FFI callables
        # Each method is wrapped through service._dispatch() so complex
        # return values (dicts/lists) are auto-serialized to JSON strings.
        # The JS Proxy layer auto-unwraps them back to native objects.
        t4 = time.perf_counter()
        for name, service in self._services.items():
            methods = service.methods()
            for method_name in methods:
                callable_name = f'__{name}_{method_name}'
                # closure captures service and method_name for _dispatch
                bound_dispatch = lambda *args, _svc=service, _mn=method_name: _svc._dispatch(_mn, *args)
                ctx.add_callable(callable_name, bound_dispatch)
        timings['add_service_callables'] = time.perf_counter() - t4

        # Inject user helpers
        t5 = time.perf_counter()
        for helper_source in self._helpers:
            ctx.eval(helper_source)
        timings['eval_helpers'] = time.perf_counter() - t5

        timings['total'] = time.perf_counter() - t0
        self._last_timings = timings
        return ctx

    # ----------------------------------------------------------------------- #
    # Core APIs (injected into every context via add_callable)
    # ----------------------------------------------------------------------- #

    def _save(self, key, val):
        """Persist a value for stagehand.load()."""
        self._persistence[key] = val

    def _load(self, key):
        """Retrieve a persisted value for stagehand.load()."""
        return self._persistence.get(key)

    def _print(self, message):
        """Route stagehand.print() to registered callbacks and stdout."""
        for cb in self._print_callbacks:
            cb(message)

    # ----------------------------------------------------------------------- #
    # Execution modes
    # ----------------------------------------------------------------------- #

    def execute(self, code: str) -> 'ExecutionResult':
        """
        Execute JS code in a fresh context (fire-and-forget).
        Like Stagehand's Sandbox().run() — execute statements, discard result.

        Returns an ExecutionResult with:
        - output: the return value of the last expression (if any)
        - error: error string if execution failed
        """
        ctx = self.create_context()
        result = ExecutionResult()

        try:
            output = ctx.eval(code)
            result.output = output
        except quickjs.JSException as e:
            result.error = str(e)

        return result

    def evaluate(self, code: str, context: quickjs.Context = None) -> 'ExecutionResult':
        """
        Evaluate JS code and return the result.
        Like Stagehand's Sandbox().eval() — evaluate an expression, return its value.

        If context is provided, evaluates in that context (state persists).
        If no context, creates a fresh one.
        """
        ctx = context or self.create_context()
        result = ExecutionResult()

        try:
            output = ctx.eval(code)
            result.output = output
        except quickjs.JSException as e:
            result.error = str(e)

        return result

    def validate(self, code: str) -> 'ValidationResult':
        """
        Check JS code for syntax errors without executing it.
        Like Stagehand's Sandbox().compile() — syntax check only.

        Returns a ValidationResult with:
        - ok: True if syntax is valid
        - error: error string if syntax check failed
        """
        result = ValidationResult()
        try:
            # Create a minimal context just for validation
            ctx = quickjs.Context()
            # Wrap in a function to catch syntax errors without executing
            ctx.eval(f'(function(){{\n{code}\n}})')
        except quickjs.JSException as e:
            result.error = str(e)
        return result


class ExecutionResult:
    """Result of executing JS code in an engine context."""

    def __init__(self):
        self.output = None
        self.error: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None

    def __repr__(self):
        if self.error:
            return f'ExecutionResult(error={self.error!r})'
        return f'ExecutionResult(output={self.output!r})'


class ValidationResult:
    """Result of validating JS code (syntax check only)."""

    def __init__(self):
        self.error: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None

    def __repr__(self):
        if self.error:
            return f'ValidationResult(error={self.error!r})'
        return 'ValidationResult(ok=True)'


class Service:
    """
    Base class for services that provide callables to JS contexts.

    Subclass this and define methods. The engine will automatically
    create stagehand.<name>.<method>() via nested Proxy + FFI.

    Supports multiple names: name = ['keyboard', 'kb']

    Return value convention:
    - Primitives (str, int, float, bool, None) cross the FFI boundary directly.
    - Dicts and lists are auto-serialized to JSON strings by _dispatch(),
      and auto-unwrapped back to native JS objects by the Proxy layer.
    - Service authors return Python dicts/lists naturally — no manual json.dumps().

    Example:

        class OBSService(Service):
            name = 'obs'

            def switch_scene(self, scene: str):
                pass

            def list_scenes(self):
                return {"scenes": ["Live", "BRB", "Ending"]}
    """

    name: str | list[str]

    @property
    def names(self) -> list[str]:
        """Return all names for this service (supports aliases)."""
        if isinstance(self.name, list):
            return self.name
        return [self.name]

    def methods(self) -> dict[str, str]:
        """
        Return a dict of {method_name: doc_string} for all callable methods.
        Methods starting with _ are excluded.
        """
        result = {}
        for attr_name in dir(self):
            if attr_name.startswith('_'):
                continue
            attr = getattr(self, attr_name)
            if callable(attr) and not isinstance(attr, type):
                result[attr_name] = attr.__doc__ or ''
        return result

    def _dispatch(self, method_name: str, *args):
        """
        Call a method and auto-serialize complex return values.

        QuickJS add_callable() only propagates primitives (str, int, float,
        bool, None) across the FFI boundary. This wrapper auto-serializes
        dicts and lists to JSON strings, which the JS Proxy layer then
        auto-unwraps back to native objects.

        This is transparent to:
        - Service authors: return dicts/lists naturally
        - JS authors: access properties directly, no JSON.parse() needed
        """
        method = getattr(self, method_name)
        result = method(*args)
        if isinstance(result, (dict, list)):
            return json.dumps(result)
        return result