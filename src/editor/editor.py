from qtstrap import *
from .highlighter import PythonHighlighter


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