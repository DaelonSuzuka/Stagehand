from qtstrap import *
from .sandbox_tools import SandboxTools, SandboxToolsDockWidget


class SandboxExtension:
    pass


@singleton
class Sandbox(QObject):
    extensions = {}

    def __init__(self):
        super().__init__()
        self.tools = SandboxTools()
        self.tools_dock = SandboxToolsDockWidget(self.tools)

        self.this = None
        self.source = None

        for ext in SandboxExtension.__subclasses__():
            e = ext()
            if isinstance(ext.name, list):
                for name in ext.name:
                    self.extensions[name] = e
            else:
                self.extensions[ext.name] = e

        self.reset_environment()

    def __getattr__(self, name):
        return self.extensions[name]

    def reset_environment(self):
        self._data = {}
        self._globals = {
            'save': self._save,
            'load': self._load,
            'data': self._data,
            'print': self.tools.print,
            'this': self.this,
            'source': self.source,
            **self.extensions,
        }
        self._locals = {
        }

    def _save(self, name, value):
        self._data[name] = value

    def _load(self, name):
        return self._data[name]

    @Slot()
    def compile(self, text, error_cb=None):
        error = ''
        try:
            compile(text, '', 'exec')
        except Exception as e:
            error = str(e)

        if error_cb:
            error_cb(error)

    @Slot()
    def run(self, text, error_cb=None):
        if text == '':
            return

        error = ''
        try:
            code = compile(text, '', 'exec')
            self._globals['this'] = self.this
            self._globals['source'] = self.source
            exec(code, self._globals, self._locals)
        except Exception as e:
            error = str(e)

        self._globals['this'] = None
        self._globals['source'] = None

        if error_cb:
            error_cb(error)
        else:
            self.tools.print(error)
    
    @Slot()
    def eval(self, text, error_cb=None):
        if text == '':
            return

        error = ''
        try:
            code = compile(text, '', 'exec')
            self._globals['this'] = self.this
            self._globals['source'] = self.source
            eval(code, self._globals, self._locals)
        except Exception as e:
            error = str(e)

        self._globals['this'] = None
        self._globals['source'] = None

        if error_cb:
            error_cb(error)
        else:
            self.tools.print(error)
