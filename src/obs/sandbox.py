import json
from obs import requests
from qt import *
from .highlighter import PythonHighlighter
from pathlib import Path


class ScriptBrowser(PersistentListWidget):
    def __init__(self, *args, **kwargs):
        files = [f.as_posix()[8:] for f in Path('./sandbox').glob('*.py')]
        super().__init__(*args, items=files, **kwargs)


class CodeEditor(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        font = QFont();
        font.setFamily("Courier");
        font.setStyleHint(QFont.Monospace);
        font.setFixedPitch(True);
        font.setPointSize(10);
        self.setFont(font)
        
        self.setTabStopWidth(QFontMetricsF(font).width(' ') * 4)
        self.syntax = PythonHighlighter(self)


class SandboxEditor(QWidget):
    reload = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.scripts = {}
        for name in [f.as_posix() for f in Path('./sandbox').glob('*.py')]:
            with open(name) as f:
                self.scripts[name[8:]] = f.read()

        self.browser = ScriptBrowser('sandbox_browser', changed=self.script_changed)
        self.editor = CodeEditor()
        self.editor.textChanged.connect(self.save)
        self.current_file = ''
        self.script_changed()

        with CHBoxLayout(self) as layout:
            layout.add(self.browser)
            layout.add(self.editor, 2)

    def save(self):
        if items := self.browser.selected_items():
            name = items[0]
            self.scripts[name] = self.editor.toPlainText()
            with open('sandbox/' + name, 'w') as f:
                f.write(self.scripts[name])
            self.reload.emit()

    def script_changed(self):
        if items := self.browser.selected_items():
            name = items[0]
            self.editor.setText(self.scripts[name])
            self.current_file = 'sandbox/' + name


class _Sandbox(QWidget):
    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = obs
        
        self.editor = SandboxEditor()
        self.editor.reload.connect(self.reload_environment)
        self.error = QLabel()

        self.reload_environment()

        with CVBoxLayout(self) as layout:
            layout.add(self.editor, 1)
            layout.add(self.error)

    def reset_environment(self):
        self._data = {}
        self._globals = {
            'send': self.obs.send,
            'requests': requests,
            'save': self.save, 
            'load': self.load, 
            'data': self._data, 
        }
        self._locals = {
        }

    def save(self, name, value):
        self._data[name] = value

    def load(self, name):
        return self._data[name]

    def reload_environment(self):
        text = ''
        for name, script in self.editor.scripts.items():
            text += script
        self.reset_environment()
        try:
            code = compile(text, '', 'exec')
            self.error.setText('')
            exec(code, self._globals, self._locals)
        except Exception as e:
            self.error.setText(str(e))

    def run(self, text):
        if text:
            try:
                payload = json.loads(text)
                self.obs.send(payload)
            except:
                try:
                    code = compile(text, '', 'exec')
                    exec(code, self._globals, self._locals)
                    # exec(code)
                except Exception as e:
                    print(e)


sandbox = None


def Sandbox(obs=None):
    global sandbox
    if sandbox is None:
        sandbox = _Sandbox(obs)
    return sandbox