from qtstrap import CHBoxLayout, QPushButton, QSize, QComboBox
from qtstrap.extras.code_editor import CodeLine
import qtawesome as qta
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem
import sys
from .shell_script_editor import ShellEditorDialog


class ShellAction(ActionItem):
    name = 'shell'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed

        self.options = []
        if sys.platform == 'win32':
            self.options += ['cmd', 'ps']
        else:
            self.options += ['bash']

        self.shell = QComboBox()
        self.shell.addItems(self.options)
        self.shell.currentIndexChanged.connect(changed)

        self.eval = CodeLine(changed=changed)
        self.eval.ctrl_enter_pressed.connect(self.run)
        
        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=qta.icon('fa5.edit'))
        self.edit_btn.setIconSize(QSize(22, 22))

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.shell)
            layout.add(self.eval)
            layout.add(self.edit_btn)

    def open_editor(self, *_):
        self.data['action'] = self.eval.text()
        self.data['shell'] = self.shell.currentText()
        self.data['name'] = self.owner.name
        self.editor = ShellEditorDialog(self.data, self.owner)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        text = self.editor.editor.toPlainText()
        self.eval.setText(text)
        self.eval.setDisabled('\n' in text)
        self.shell.setCurrentText(self.editor.shell.currentText())
        self.owner.label.setText(self.editor.label.text())
        self.changed()

    def set_data(self, data):
        self.data = data
        self.shell.setCurrentText(data.get('shell', 'cmd'))
        self.eval.setText(data.get('eval', ''))

    def get_data(self):
        return {
            'shell': self.shell.currentText(),
            'eval': self.eval.text(),
        }
    
    def run(self):
        Sandbox()[self.shell.currentText()].eval(self.eval.text())