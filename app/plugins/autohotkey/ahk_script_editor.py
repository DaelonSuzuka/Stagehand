from qtstrap import *
from qtstrap.extras.code_editor import CodeEditor
import qtawesome as qta
from stagehand.sandbox import Sandbox
from .ahk_script_highlighter import AHKScriptHighlighter




class AHKScriptEditorDialog(QDialog):
    reload = Signal(str, Slot)

    def __init__(self, data, owner=None):
        super().__init__()

        self.owner = owner
        self.setWindowTitle('AutoHotKey Script Editor')

        size: int = QSettings().value('font_size', 12)
        set_font_options(self, {'setPointSize': int(size)})

        self.geometry_setting = 'plugins/ahk/ahk_script_editor/geometry'

        geometry = QSettings().value(self.geometry_setting)
        if isinstance(geometry, QByteArray):
            self.restoreGeometry(geometry)

        self.finished.connect(lambda _: QSettings().setValue(self.geometry_setting, self.saveGeometry()))

        self.name = owner.name
        self.label = QLineEdit(owner.label.text())
        self.editor = CodeEditor(highlighter=AHKScriptHighlighter)
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
            layout.add(self.editor)
            layout.add(self.error)
            with layout.hbox(align='right') as layout:
                layout.add(self.cancel_btn)
                layout.add(self.ok_btn)

        self.editor.setFocus()

    def run(self):
        Sandbox().run(f'ahk.run_script("{self.editor.toPlainText()}")', error_cb=self.set_error)

    @Slot()
    def set_error(self, error):
        self.error.setText(error)

    def on_reset(self):
        self.editor.setText('')
        self.label.setText(self.name)