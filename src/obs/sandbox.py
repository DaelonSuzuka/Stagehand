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

        with CPersistentSplitter('sandbox_splitter', self) as splitter:
            splitter.add(self.browser, 1)
            splitter.add(self.editor, 4)

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


class SandboxEditorDockWidget(QDockWidget):
    def __init__(self, widget=None, parent=None):
        super().__init__('Sandbox Editor', parent=parent)
        self.setObjectName('Sandbox_Editor')

        self.setWidget(widget)

        # self.setAllowedAreas(Qt.BottomDockWidgetArea)
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

        # self.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)

        self.starting_area = Qt.BottomDockWidgetArea

        self.closeEvent = lambda x: self.hide()

    def toggleViewAction(self):
        action = super().toggleViewAction()
        action.setShortcut('Ctrl+T')
        return action



class SandboxTools(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.scenes = QListWidget()
        self.sources = QListWidget()
        self.output = QTextEdit()

        with CHBoxLayout(self) as layout:
            with layout.hbox() as layout:
                with layout.vbox() as layout:
                    layout.add(QLabel('Scenes:'))
                    layout.add(self.scenes)
                with layout.vbox() as layout:
                    layout.add(QLabel('Sources:'))
                    layout.add(self.sources)
            with layout.vbox() as layout:
                layout.add(QLabel('Output:'))
                layout.add(self.output)


class _Sandbox(QWidget):
    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = obs
        
        self.editor = SandboxEditor()
        self.editor.reload.connect(self.reload_environment)

        self.tools = SandboxTools()
        self.error = QLabel()

        self.reload_environment()

        self.editor_dock = SandboxEditorDockWidget(self.editor, self)
        self.tools_dock = SandboxToolsDockWidget(self.tools, self)

    def reset_environment(self):
        self._data = {}
        self._globals = {
            'send': self.obs.send,
            'requests': requests,
            'save': self._save, 
            'load': self._load, 
            'data': self._data, 
            'print': self._print, 
        }
        self._locals = {
        }

    def _print(self, *args):
        s = ''
        for arg in args:
            s += str(arg)
        self.tools.output.append(s + '\n')
        

    def _save(self, name, value):
        self._data[name] = value

    def _load(self, name):
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


def Sandbox(obs=None, parent=None):
    global sandbox
    if sandbox is None:
        sandbox = _Sandbox(obs, parent)
    return sandbox