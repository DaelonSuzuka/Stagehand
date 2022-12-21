from qtstrap import *
from .sandbox import Sandbox

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
