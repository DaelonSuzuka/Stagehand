from qtstrap import *
from stagehand.roadie import Engine, ExtensionToServiceAdapter
from .sandbox_tools import SandboxTools, SandboxToolsDockWidget


class SandboxExtension:
    pass


@singleton
class Sandbox(QObject):
    extensions = {}

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.tools_dock = SandboxToolsDockWidget(parent)
        self.tools = self.tools_dock.tools

        # Build the QuickJS engine and register all existing extensions
        self._engine = Engine()
        self._engine.on_print(lambda msg: self.tools.print(msg))

        for ext in SandboxExtension.__subclasses__():
            e = ext()
            if isinstance(ext.name, list):
                for name in ext.name:
                    self.extensions[name] = e
            else:
                self.extensions[ext.name] = e
            self._engine.register_service(ExtensionToServiceAdapter(e))

        self.reset_environment()

    def __getattr__(self, name):
        return self.extensions[name]

    def __getitem__(self, name):
        return self.extensions[name]

    def reset_environment(self):
        self._data = {}
        self._globals = {
            'save': self._save,
            'load': self._load,
            'data': self._data,
            'print': self.tools.print,
            # 'this' and 'source' removed — violations of the narrow waist.
            # If action code needs trigger context, it should flow through
            # the fire event payload, not UI object references.
            **self.extensions,
        }
        self._locals = {}

    def _save(self, name, value):
        self._data[name] = value

    def _load(self, name):
        return self._data[name]

    @Slot()
    def compile(self, text, error_cb=None):
        """Validate JS syntax without executing. Replaces Python's compile()."""
        result = self._engine.validate(text)
        error = result.error if not result.ok else ''

        if error_cb:
            error_cb(error)

    @Slot()
    def run(self, text, error_cb=None):
        """Execute JS code in a fresh context. Replaces Python's exec()."""
        if text == '':
            return

        result = self._engine.execute(text)
        error = result.error if not result.ok else ''

        if error_cb:
            error_cb(error)
        elif error:
            self.tools.print(error)

    @Slot()
    def eval(self, text, error_cb=None):
        """Evaluate JS code and return the result. Replaces Python's eval()."""
        if text == '':
            return

        result = self._engine.evaluate(text)
        error = result.error if not result.ok else ''

        if error_cb:
            error_cb(error)
        elif error:
            self.tools.print(error)