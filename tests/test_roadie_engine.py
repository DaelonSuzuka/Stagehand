"""Tests for the Roadie engine (QuickJS evaluation engine)."""

import pytest
from stagehand.roadie import Engine, Service, ExecutionResult, ValidationResult, ExtensionToServiceAdapter
from stagehand.sandbox import SandboxExtension


# --------------------------------------------------------------------------- #
# Mock services for testing
# --------------------------------------------------------------------------- #


class MockOBS(Service):
    name = 'obs'

    def switch_scene(self, scene: str):
        """Switch to a scene by name."""
        return f'switched to {scene}'

    def toggle_mute(self, source: str):
        """Toggle mute on a source."""
        return f'toggled {source}'

    def list_scenes(self):
        """Return all scenes as a dict (auto-serialized via _dispatch)."""
        return {"scenes": ["Live", "BRB", "Ending", "Offline"]}


class MockHTTP(Service):
    name = 'http'

    def get(self, url: str):
        """GET request. Returns a dict — auto-serialized for JS."""
        return {"status": 200, "body": f"Hello from {url}"}

    def post(self, url: str, data=''):
        """POST request. Returns a dict — auto-serialized for JS."""
        return {"status": 201, "id": 42}


class MockKeyboard(Service):
    name = ['keyboard', 'kb']

    def tap(self, key: str):
        """Tap a key."""
        return f'tapped {key}'

    def press(self, key: str):
        """Press a key."""
        return f'pressed {key}'

    def release(self, key: str):
        """Release a key."""
        return f'released {key}'


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #


@pytest.fixture
def engine():
    """Create an engine with mock services registered."""
    e = Engine()
    captured = []
    e.on_print(lambda msg: captured.append(msg))
    e._captured = captured  # stash for test access
    e.register_service(MockOBS())
    e.register_service(MockHTTP())
    e.register_service(MockKeyboard())
    return e


@pytest.fixture
def engine_with_helper(engine):
    """Engine with a test helper registered."""
    engine.register_helper("""
        roadie.helpers.discordAlert = function(message) {
            var r = stagehand.http.post("https://discord.example.com/webhook");
            stagehand.print("Discord alert sent: " + message + " (status: " + r.status + ")");
        };
    """)
    return engine


# --------------------------------------------------------------------------- #
# Basic execution
# --------------------------------------------------------------------------- #


class TestBasicExecution:
    def test_basic_math(self, engine):
        result = engine.execute('1 + 2')
        assert result.ok
        assert result.output == 3

    def test_print_callback(self, engine):
        result = engine.execute('stagehand.print("hello from the engine!")')
        assert result.ok
        assert 'hello from the engine!' in engine._captured

    def test_print_multiple_args(self, engine):
        result = engine.execute('stagehand.print("hello", "world")')
        assert result.ok
        assert 'hello world' in engine._captured


# --------------------------------------------------------------------------- #
# Service calls
# --------------------------------------------------------------------------- #


class TestServiceCalls:
    def test_void_call(self, engine):
        result = engine.execute('stagehand.obs.switch_scene("Live")')
        assert result.ok

    def test_string_return(self, engine):
        result = engine.execute('stagehand.obs.switch_scene("Live")')
        assert result.ok
        assert result.output == 'switched to Live'

    def test_service_aliases(self, engine):
        result = engine.execute('stagehand.keyboard.tap("a")')
        assert result.ok
        result = engine.execute('stagehand.kb.tap("b")')
        assert result.ok

    def test_unknown_method_clear_error(self, engine):
        result = engine.execute('stagehand.obs.nonexistent("test")')
        assert not result.ok
        assert 'not available' in result.error


# --------------------------------------------------------------------------- #
# Auto-unwrap (dict/list returns)
# --------------------------------------------------------------------------- #


class TestAutoUnwrap:
    def test_dict_returns_as_object(self, engine):
        result = engine.execute("""
            var scenes = stagehand.obs.list_scenes()
            typeof scenes
        """)
        assert result.output == 'object'

    def test_dict_property_access(self, engine):
        result = engine.execute('stagehand.obs.list_scenes().scenes[0]')
        assert result.output == 'Live'

    def test_http_auto_unwrap(self, engine):
        result = engine.execute("""
            var r = stagehand.http.get("https://api.example.com")
            r.status + " " + r.body
        """)
        assert result.output == '200 Hello from https://api.example.com'


# --------------------------------------------------------------------------- #
# Save/Load persistence
# --------------------------------------------------------------------------- #


class TestPersistence:
    def test_save_load_roundtrip(self, engine):
        engine.execute('stagehand.save("counter", 42)')
        result = engine.execute('stagehand.load("counter")')
        assert result.output == 42

    def test_persistence_across_contexts(self, engine):
        engine.execute('stagehand.save("name", "Roadie")')
        result = engine.execute('stagehand.load("name")')
        assert result.output == 'Roadie'

    def test_primitive_roundtrip(self, engine):
        engine.execute('stagehand.save("num", 99)')
        result = engine.execute('stagehand.load("num")')
        assert result.output == 99


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


class TestHelpers:
    def test_helper_auto_unwrap(self, engine_with_helper):
        engine_with_helper._captured.clear()
        result = engine_with_helper.execute('roadie.helpers.discordAlert("Going live!")')
        assert result.ok
        assert any('Discord alert' in c for c in engine_with_helper._captured)


# --------------------------------------------------------------------------- #
# Isolation
# --------------------------------------------------------------------------- #


class TestIsolation:
    def test_no_require(self, engine):
        result = engine.execute("""
            try {
                require;
                "REQUIRE_EXISTS"
            } catch(e) {
                "require blocked"
            }
        """)
        assert result.output == 'require blocked'

    def test_error_handling(self, engine):
        result = engine.execute('undefined_function()')
        assert not result.ok


# --------------------------------------------------------------------------- #
# Execution modes
# --------------------------------------------------------------------------- #


class TestExecutionModes:
    def test_evaluate_returns_value(self, engine):
        result = engine.evaluate('1 + 2')
        assert result.ok
        assert result.output == 3

    def test_validate_valid_syntax(self, engine):
        result = engine.validate('var x = 1;')
        assert result.ok

    def test_validate_invalid_syntax(self, engine):
        result = engine.validate('var x = ;')
        assert not result.ok

    def test_persistent_context_repl(self, engine):
        ctx = engine.create_context()
        engine.evaluate('var x = 10', context=ctx)
        result = engine.evaluate('x + 5', context=ctx)
        assert result.output == 15


# --------------------------------------------------------------------------- #
# ExtensionToServiceAdapter
# --------------------------------------------------------------------------- #


class TestExtensionAdapter:
    def test_adapter_wraps_extension(self, engine):
        class TestExt(SandboxExtension):
            name = 'test'
            def greet(self, name: str):
                """Greet someone."""
                return f'Hello, {name}!'

        engine.register_service(ExtensionToServiceAdapter(TestExt()))
        result = engine.execute('stagehand.test.greet("World")')
        assert result.ok
        assert result.output == 'Hello, World!'

    def test_adapter_dict_return(self, engine):
        class DataExt(SandboxExtension):
            name = 'data'
            def get_info(self):
                """Return info dict."""
                return {"name": "test", "version": 1}

        engine.register_service(ExtensionToServiceAdapter(DataExt()))
        result = engine.execute('stagehand.data.get_info().name')
        assert result.ok
        assert result.output == 'test'

    def test_adapter_alias_names(self, engine):
        class AliasExt(SandboxExtension):
            name = ['alias', 'alt']
            def ping(self):
                return 'pong'

        adapter = ExtensionToServiceAdapter(AliasExt())
        engine.register_service(adapter)

        result1 = engine.execute('stagehand.alias.ping()')
        assert result1.ok
        assert result1.output == 'pong'

        result2 = engine.execute('stagehand.alt.ping()')
        assert result2.ok
        assert result2.output == 'pong'

    def test_adapter_methods_introspection(self):
        class IntrospectExt(SandboxExtension):
            name = 'intro'
            def method_a(self):
                """Method A."""
                pass
            def method_b(self, x: int):
                """Method B."""
                pass

        adapter = ExtensionToServiceAdapter(IntrospectExt())
        methods = adapter.methods()
        assert 'method_a' in methods
        assert 'method_b' in methods
        assert methods['method_a'] == 'Method A.'


# --------------------------------------------------------------------------- #
# Sandbox→Engine bridge (no Qt dependency)
# --------------------------------------------------------------------------- #


class TestSandboxBridge:
    """Test that Sandbox's run/eval/compile delegate to the QuickJS engine.
    
    These tests create an Engine directly and verify the same code paths
    that Sandbox delegates to. Sandbox itself requires Qt (SandboxToolsDockWidget)
    so we can't instantiate it in headless tests.
    """

    def test_compile_valid_js(self):
        """validate() accepts valid JS — same path as Sandbox().compile()."""
        engine = Engine()
        result = engine.validate('var x = 1;')
        assert result.ok

    def test_compile_invalid_js(self):
        """validate() rejects invalid JS — same path as Sandbox().compile()."""
        engine = Engine()
        result = engine.validate('var x = ;')
        assert not result.ok
        assert result.error != ''

    def test_run_basic(self):
        """execute() runs JS code — same path as Sandbox().run()."""
        engine = Engine()
        result = engine.execute('1 + 1')
        assert result.ok

    def test_run_error(self):
        """execute() reports JS errors — same path as Sandbox().run()."""
        engine = Engine()
        result = engine.execute('undefined_function()')
        assert not result.ok
        assert result.error != ''

    def test_run_empty_is_noop(self):
        """Empty string is still executed (context created, empty eval)."""
        engine = Engine()
        # Empty string just creates a context and evaluates nothing
        result = engine.execute('')
        assert result.ok

    def test_eval_basic(self):
        """evaluate() evaluates JS and returns result — same path as Sandbox().eval()."""
        engine = Engine()
        result = engine.evaluate('1 + 1')
        assert result.ok
        assert result.output == 2

    def test_print_routes_through_engine(self):
        """stagehand.print() routes through engine.on_print — 
        same path as Sandbox().run() routing to tools.print."""
        engine = Engine()
        captured = []
        engine.on_print(lambda msg: captured.append(msg))
        engine.execute('stagehand.print("hello from bridge test")')
        assert 'hello from bridge test' in captured