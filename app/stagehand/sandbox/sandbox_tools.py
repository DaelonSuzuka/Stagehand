from qtstrap import *


class SandboxTools(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.output = QTextEdit(readOnly=True)
        self.clear_output = QPushButton('Clear', clicked=self.output.clear)

        with CHBoxLayout(self) as layout:
            with layout.vbox() as layout:
                with layout.hbox(margins=(0,0,0,0)) as layout:
                    layout.add(QLabel('Output:'))
                    layout.add(QLabel(), 1)
                    layout.add(self.clear_output)
                layout.add(self.output)

    def print(self, *args):
        s = ''
        for arg in args:
            s += str(arg)
        self.output.append(s)