from qtstrap import *
from qtstrap.extras.code_editor import CodeEditor
import qtawesome as qta
from stagehand.sandbox import Sandbox


class ShellEditorDialog(QDialog):
    reload = Signal(str, Slot)

    def __init__(self, data, owner=None):
        super().__init__()

        self.owner = owner
        self.data = data
        self.setWindowTitle('Shell Script Editor')

        size: int = QSettings().value('font_size', 12)
        set_font_options(self, {'setPointSize': int(size)})

        self.geometry_setting = 'plugins/shell/shell_script_editor/geometry'

        geometry = QSettings().value(self.geometry_setting)
        if isinstance(geometry, QByteArray):
            self.restoreGeometry(geometry)

        self.finished.connect(lambda _: QSettings().setValue(self.geometry_setting, self.saveGeometry()))

        self.options = []
        if sys.platform == 'win32':
            self.options += ['cmd', 'ps']
        else:
            self.options += ['bash']

        self.shell = QComboBox()
        self.shell.addItems(self.options)
        self.shell.setCurrentText(data['shell'])

        self.name = owner.name
        self.label = QLineEdit(owner.label.text())

        self.editor = CodeEditor()
        self.editor.setText(data['action'])
        self.editor.textChanged.connect(lambda: self.reload.emit(self.editor.toPlainText(), self.set_error))
        self.editor.ctrl_enter_pressed.connect(self.run)
        # self.reload.connect(Sandbox().compile)
        self.error = QLabel('')

        self.reset_btn = QPushButton('Reset', clicked=self.on_reset)
        self.cancel_btn = QPushButton('Cancel', clicked=self.reject)
        self.ok_btn = QPushButton('Ok', clicked=self.accept)
        self.run_btn = QPushButton('', clicked=self.run)
        self.run_btn.setIcon(qta.icon('mdi.play-circle-outline'))

        with CVBoxLayout(self) as layout:
            with layout.hbox() as layout:
                layout.add(QLabel('Name:'))
                layout.add(QLabel(owner.name))
                layout.add(QLabel(), 1)
                layout.add(self.reset_btn)
            with layout.hbox(align='left') as layout:
                layout.add(QLabel('Label:'))
                layout.add(self.label)
                layout.add(QLabel(), 1)
                layout.add(self.run_btn)
            with layout.hbox(align='left') as layout:
                layout.add(QLabel('Shell:'))
                layout.add(self.shell)
            layout.add(self.editor)
            layout.add(self.error)
            with layout.hbox(align='right') as layout:
                layout.add(self.cancel_btn)
                layout.add(self.ok_btn)

        self.editor.setFocus()

    def run(self):
        Sandbox()[self.shell.currentText()].eval(self.editor.toPlainText())

    @Slot()
    def set_error(self, error):
        self.error.setText(error)

    def on_reset(self):
        self.editor.setText('')
        self.label.setText(self.name)
