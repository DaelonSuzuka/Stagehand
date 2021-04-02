import json
from obs import requests
from qtstrap import *
from .highlighter import PythonHighlighter
from pathlib import Path
from pyautogui import press, hotkey


class ScriptBrowser(PersistentTreeWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, index_column=3, **kwargs)
        
        self.setUniformRowHeights(True)
        self.setExpandsOnDoubleClick(False)
        self.setHeaderLabels(['Files'])

        self.nodes = {}
        self.refresh_nodes()

    def create_intermediate_nodes(self, name):
        parts = name.split('/')
        
        if len(parts) == 2:
            if parts[0] not in self.nodes:
                node = QTreeWidgetItem(self)
                node.setText(0, parts[0])
                node.setText(3, parts[0])
                node.setText(4, 'folder')
                self.nodes[parts[0]] = node

    def create_node(self, name):
        parts = name.split('/')
        if len(parts) == 1:
            node = QTreeWidgetItem(self)
            node.setText(0, parts[-1])
            node.setText(3, name)
            node.setText(4, 'file')
            self.nodes[name] = node

        else:
            self.create_intermediate_nodes(name)
            node = QTreeWidgetItem(self.nodes[parts[-2]])
            node.setText(0, parts[-1])
            node.setText(3, name)
            node.setText(4, 'file')
            self.nodes[name] = node
        
    def refresh_nodes(self):
        self.clear()
        self.nodes = {}

        files = [f.as_posix()[8:] for f in Path('./sandbox').rglob('*.py')]
    
        for f in files:
            self.create_node(f)

        self.expandAll()

    # def create_folder(self, parent):
    #     node = QTreeWidgetItem(parent)
    #     node.setText(0, 'new_folder')
    #     self.nodes.append(node)


    # def contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None:
    #     pos = event.globalPos()
    #     item = self.itemAt(self.viewport().mapFromGlobal(pos))

    #     menu = QMenu()
    #     menu.addAction(QAction('New Folder', self, triggered=lambda: self.create_folder(item)))
    #     menu.addAction(QAction('New File', self))
    #     menu.exec_(pos)


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
        for name in [f.as_posix() for f in Path('./sandbox').rglob('*.py')]:
            with open(name) as f:
                self.scripts[name[8:]] = f.read()

        self.browser = ScriptBrowser('sandbox_browser', changed=self.script_changed)
        self.editor = CodeEditor()
        self.editor.textChanged.connect(self.save)
        self.error = QLabel()
        
        self.current_file = ''
        self.script_changed()

        with CPersistentSplitter('sandbox_splitter', self) as splitter:
            splitter.add(self.browser, 1)
            with splitter.add(CVBoxLayout(margins=(0,0,0,0)), 4) as layout:
                layout.add(self.editor)
                layout.add(self.error)

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
            if name in self.scripts:
                self.editor.setText(self.scripts[name])
                self.current_file = 'sandbox/' + name


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


class SandboxTools(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.scenes = QListWidget()
        self.refresh_scenes = QPushButton('Refresh')
        self.sources = QListWidget()
        self.refresh_sources = QPushButton('Refresh')
        self.output = QTextEdit(readOnly=True)
        self.clear_output = QPushButton('Clear', clicked=self.output.clear)

        with CHBoxLayout(self) as layout:
            with layout.hbox() as layout:
                with layout.vbox() as layout:
                    with layout.hbox(margins=(0,0,0,0)) as layout:
                        layout.add(QLabel('Scenes:'))
                        layout.add(QLabel(), 1)
                        layout.add(self.refresh_scenes)
                    layout.add(self.scenes)
                with layout.vbox() as layout:
                    with layout.hbox(margins=(0,0,0,0)) as layout:
                        layout.add(QLabel('Sources:'))
                        layout.add(QLabel(), 1)
                        layout.add(self.refresh_sources)
                    layout.add(self.sources)
            with layout.vbox() as layout:
                with layout.hbox(margins=(0,0,0,0)) as layout:
                    layout.add(QLabel('Output:'))
                    layout.add(QLabel(), 1)
                    layout.add(self.clear_output)
                layout.add(self.output)


class _Sandbox(QWidget):
    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = obs
        
        self.editor = SandboxEditor()
        self.editor.reload.connect(self.reload_environment)
        self.tools = SandboxTools()

        def GetSceneList(cb):
            def collect_names(message):
                cb([s['name'] for s in message['scenes']])

            self.obs.send({"request-type": 'GetSceneList'}, collect_names)

        self.tools.refresh_scenes.clicked.connect(lambda:
            GetSceneList(lambda s: self.tools.scenes.addItems(s)))

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
            'press': press,
            'hotkey': hotkey,
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
        self.reset_environment()
        for name, script in self.editor.scripts.items():
            try:
                code = compile(script, '', 'exec')
                self.editor.error.setText('')
                exec(code, self._globals, self._locals)
            except Exception as e:
                self.editor.error.setText(str(e))

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