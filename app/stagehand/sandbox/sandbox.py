from qtstrap import *
import json
from pathlib import Path
from pynput.keyboard import Key, Controller
from .sandbox_tools import SandboxTools
from .sandbox_editor import SandboxEditor


class SandboxEditorDockWidget(QDockWidget):
    def __init__(self, widget=None, parent=None):
        super().__init__('Sandbox Editor', parent=parent)
        self.setObjectName('Sandbox_Editor')

        self.setWidget(widget)
        self.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.starting_area = Qt.RightDockWidgetArea
        self.closeEvent = lambda x: self.hide()

    def toggleViewAction(self):
        action = super().toggleViewAction()
        action.setShortcut('Ctrl+E')
        return action


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


class Obs:
    def __init__(self, obs):
        self.obs = obs

    def set_scene(self, name):
        self.obs.send(payload)

    def send(self, payload, cb=None):
        self.obs.send(payload, cb)


class Keyboard:
    def __init__(self):
        self.controller = Controller()

    def __getattr__(self, name):
        return getattr(Key, name)

    def key(self, k):
        self.controller.press(k)
        self.controller.release(k)

    def press(self, key):
        self.controller.press(key)

    def release(self, key):
        self.controller.release(key)


class _Sandbox(QWidget):
    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = Obs(obs)
        
        self.editor = SandboxEditor(obs)
        self.editor.reload.connect(self.reload_environment)
        self.tools = SandboxTools(obs)
        self.keyboard = Keyboard()

        self.reload_environment()

        self.editor_dock = SandboxEditorDockWidget(self.editor, self)
        self.tools_dock = SandboxToolsDockWidget(self.tools, self)

    def reset_environment(self):
        self._data = {}
        self._globals = {
            'obs': self.obs,
            'save': self._save, 
            'load': self._load, 
            'data': self._data, 
            'print': self.tools.print,
            'keyboard': self.keyboard,
            'kb': self.keyboard,
        }
        self._locals = {
        }

    def _save(self, name, value):
        self._data[name] = value

    def _load(self, name):
        return self._data[name]

    @Slot()
    def compile(self, text, error_cb=None):
        self.reload_environment()

        error = ''
        try:
            compile(text, '', 'exec')
        except Exception as e:
            error = str(e)

        if error_cb:
            error_cb(error)

    @Slot()
    def reload_environment(self, error_cb=None):
        self.reset_environment()

        error = ''
        for name, script in self.editor.scripts.items():
            try:
                code = compile(script, '', 'exec')
                exec(code, self._globals, self._locals)
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