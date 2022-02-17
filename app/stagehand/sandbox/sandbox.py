from qtstrap import *
import json
from pathlib import Path
from .sandbox_tools import SandboxTools


class SandboxExtension:
    pass


words = None
subwords = None


def get_word_list():
    global words
    global subwords

    if words is None or subwords is None:
        words = {
            **Sandbox()._data,
            **Sandbox()._globals,
        }
        subwords = {}
        
        for word, obj in words.items():
            if type(obj).__name__ not in ['method', 'dict', 'NoneType']:
                subwords[word] = []
                for method in [m for m in dir(obj) if not m.startswith('__')]:
                    subwords[word].append(method)

    return words, subwords


class SandboxCompletionModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.prefix = ''

        words, subwords = get_word_list()
        self.words = words
        self.subwords = subwords
        
        self.sorted_words = []

    def get_prev_word(self, cursor):
        cursor.movePosition(QTextCursor.PreviousWord, QTextCursor.KeepAnchor, 2)
        cursor.select(QTextCursor.WordUnderCursor)
        return cursor.selectedText()

    def set_prefix(self, prefix, cursor):
        block = self.get_prev_word(cursor)
        previous_word = ''
        if prefix:
            if block == '.':
                previous_word = self.get_prev_word(cursor)
        else:
            previous_word = block

        self.prefix = prefix
        self.sorted_words = []

        words = self.subwords.get(previous_word, self.words.keys())
        for w in words:
            if w.lower().startswith(prefix.lower()):
                self.sorted_words.append(w)
        for w in words:
            if w in self.sorted_words:
                continue
            if prefix.lower() in w.lower():
                self.sorted_words.append(w)
            
    def rowCount(self, parent: QModelIndex) -> int:
        return len(self.sorted_words)

    def data(self, index: QModelIndex, role: int):
        if not index.isValid():
            return None

        if role in [Qt.EditRole, Qt.DisplayRole]:
            if index.row() < len(self.sorted_words):
                return self.sorted_words[index.row()]

    def index(self, row: int, column: int, parent: QModelIndex) -> QModelIndex:
        return self.createIndex(row, column)


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

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.tools = SandboxTools()
        self.tools_dock = SandboxToolsDockWidget(self.tools, self)

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
            'this': None,
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
    def run(self, text, this=None, error_cb=None):
        if text == '':
            return

        error = ''
        try:
            code = compile(text, '', 'exec')
            self._globals['this'] = this
            exec(code, self._globals, self._locals)
        except Exception as e:
            error = str(e)

        self._globals['this'] = None

        if error_cb:
            error_cb(error)
        else:
            self.tools.print(error)
    
    @Slot()
    def eval(self, text, this=None, error_cb=None):
        if text == '':
            return

        error = ''
        try:
            code = compile(text, '', 'exec')
            self._globals['this'] = this
            eval(code, self._globals, self._locals)
        except Exception as e:
            error = str(e)

        self._globals['this'] = None

        if error_cb:
            error_cb(error)
        else:
            self.tools.print(error)



sandbox = None


def Sandbox(parent=None):
    global sandbox
    if sandbox is None:
        sandbox = _Sandbox(parent)
    return sandbox