from qtstrap import *
from qtstrap.extras import code_editor


class ActionEditorDialog(QDialog):
    reload = Signal(str, Slot)

    def __init__(self, data, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle('Action Editor')

        self.name = data['name']
        self.label = QLineEdit(data['label'])
        self.editor = CodeEditor()
        self.editor.setText(data['action'])
        self.editor.textChanged.connect(lambda: self.reload.emit(self.editor.toPlainText(), self.set_error))
        self.reload.connect(Sandbox().compile)
        self.error = QLabel('')

        self.reset = QPushButton('Reset', clicked=self.on_reset)
        self.cancel = QPushButton('Cancel', clicked=self.reject)
        self.ok = QPushButton('Ok', clicked=self.accept)
        self.run = QPushButton('', clicked=lambda: Sandbox().run(self.editor.toPlainText(), self.set_error))
        self.run.setIcon(QIcon(qta.icon('mdi.play-circle-outline')))

        with CVBoxLayout(self) as layout:
            with layout.hbox() as layout:
                layout.add(QLabel('Name:'))
                layout.add(QLabel(data['name']))
                layout.add(QLabel(), 1)
                layout.add(self.reset)
            with layout.hbox(align='left') as layout:
                layout.add(QLabel('Label:'))
                layout.add(self.label)
                layout.add(QLabel(), 1)
                layout.add(self.run)
            layout.add(self.editor)
            layout.add(self.error)
            with layout.hbox(align='right') as layout:
                layout.add(self.cancel)
                layout.add(self.ok)

        self.editor.setFocus()

    @Slot()
    def set_error(self, error):
        self.error.setText(error)

    def on_reset(self):
        self.editor.setText('')
        self.label.setText(self.name)