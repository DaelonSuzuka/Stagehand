from qtstrap import *
import json
from pathlib import Path
from stagehand.obs import requests
from .sandbox_tools import SandboxTools


class SandboxToolsDockWidget(QDockWidget):
    def __init__(self, widget=None, parent=None):
        super().__init__('Sandbox Tools', parent=parent)
        self.setObjectName('Sandbox_Tools')

        self.setWidget(widget)
        self.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.starting_area = Qt.BottomDockWidgetArea
        self.closeEvent = lambda x: self.hide()

    def toggleViewAction(self):
        action = super().toggleViewAction()
        action.setShortcut('Ctrl+T')
        return action


class _Sandbox(QWidget):
    extensions = {}

    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = obs
        
        self.tools = SandboxTools(obs)
        self.tools_dock = SandboxToolsDockWidget(self.tools, self)

        self.reset_environment()

    def reset_environment(self):
        self._data = {}
        self._globals = {
            'save': self._save, 
            'load': self._load, 
            'data': self._data, 
            'print': self.tools.print,
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
            exec(code, self._globals, self._locals)
        except Exception as e:
            error = str(e)

        if error_cb:
            error_cb(error)
        else:
            self.tools.print(error)


sandbox = None


def Sandbox(obs=None, parent=None):
    global sandbox
    if sandbox is None:
        sandbox = _Sandbox(obs, parent)
    return sandbox