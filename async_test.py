import PySide6.QtAsyncio as QtAsyncio
from promisio import promisify
from qtstrap import *


class ChoiceDialog(AwaitableDialog):
    def __init__(self, parent):
        super().__init__(parent=parent, modal=True)

        with CVBoxLayout(self) as layout:
            layout.add(QPushButton('one', clicked=lambda: self.submit('one')))
            layout.add(QPushButton('two', clicked=lambda: self.submit('two')))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton(text='pick one')
        button.clicked(self.ask_question)

        self.label = QLabel()

        with CVBoxLayout(self) as layout:
            layout.add(button, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.add(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.show()

    @promisify
    async def ask_question(self):
        result = await ChoiceDialog(self)
        self.label.setText(result)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    
    QtAsyncio.run(handle_sigint=True)
