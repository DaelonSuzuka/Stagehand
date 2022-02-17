from qtstrap import *
from qtstrap.extras.code_editor import CodeEditor


class CodeLine(CodeEditor):
    def __init__(self, changed=None, model=None):
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setLineWrapMode(QTextEdit.NoWrap)
        self.setFixedHeight(28)
        
        if changed:
            self.textChanged.connect(changed)

        self.model = model

        self.completer = QCompleter(self.model, self)
        self.completer.setWidget(self)
        self.completer.popup().setMinimumWidth(150)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)

        self.completer.activated.connect(self.insert_completion)

    def insert_completion(self, completion):
        tc = self.textCursor()
        extra = len(completion) - len(self.completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)

    def text_under_cursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)
        return tc.selectedText()
        
    def keyPressEvent(self, event:QKeyEvent):
        force_popup = False
        if event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_Space:
                force_popup = True

        keys = [Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab]
        if self.completer.popup().isVisible():
            if event.key() in keys:
                event.ignore()
                return
    
        if event.key() in [Qt.Key_Enter, Qt.Key_Return]:
            event.accept()
            return

        braces = {
            '"': '"',
            "'": "'",
            '{': '}',
            '(': ')',
            '<': '>',
            '[': ']',
            '|': '|',
            '`': '`',
        }

        cur = self.textCursor()
        if cur.hasSelection():
            if event.text() in braces:
                start = cur.selectionStart()
                end = cur.selectionEnd()
                cur.clearSelection()
                cur.setPosition(end)
                cur.insertText(braces[event.text()])
                cur.setPosition(start)
                cur.insertText(event.text())
                cur.setPosition(start + 1)
                cur.setPosition(end + 1, QTextCursor.KeepAnchor)
                self.setTextCursor(cur)
                return

        super().keyPressEvent(event)

        prefix = self.text_under_cursor()
        if event.key() == Qt.Key_Period:
            force_popup = True
        if prefix or force_popup:
            if self.model:
                self.model.set_prefix(prefix, self.textCursor())
            self.completer.setCompletionPrefix(prefix)
            index = self.completer.completionModel().index(0, 0)
            self.completer.popup().setCurrentIndex(index)

            cr = self.cursorRect()
            cr.setWidth(self.completer.popup().sizeHintForColumn(0) + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:
            self.completer.popup().hide()

    def text(self):
        return self.toPlainText()