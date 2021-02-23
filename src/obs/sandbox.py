import json
from obs import requests
from qt import *
from .highlighter import PythonHighlighter

"""s
def SetCurrentScene(scene):
	send({"request-type":"SetCurrentScene","scene-name":scene}, print)

def GetSceneList():
    send({"request-type": 'GetSceneList'}, print)

def GetCurrentScene(cb=lambda x: x):
    send({"request-type": 'GetCurrentScene'}, lambda m: cb(m['name']))
"""


class ScriptBrowser(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def get_new_name(self):
        name = 'new'
        # for c in range(self.count()):
        #     if self.itemAt(c).text
        return name

    def new(self):
        item = QListWidgetItem(self.get_new_name())
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.addItem(item)
        self.editItem(item)


class CodeEditor(PersistentTextEdit):
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
    def __init__(self, reload=None, parent=None):
        super().__init__(parent=parent)

        self.scripts = QSettings().value('sandbox_scripts', {})

        self.browser = ScriptBrowser()
        self.editor = CodeEditor('sandbox_editor', changed=reload)
        self.new = QPushButton('New', clicked=self.browser.new)
        self.reload = QPushButton('Reload')

        with CHBoxLayout(self) as layout:
            with layout.vbox() as layout:
                with layout.hbox() as layout:
                    layout.add(self.new)
                    layout.add(self.reload)
                layout.add(self.browser)
            layout.add(self.editor, 2)


class _Sandbox(QWidget):
    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = obs
        self.reset_environment()
        
        self.editor = SandboxEditor(self.reload_environment)
        self.error = QLabel()

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
        text = self.editor.editor.toPlainText()
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

