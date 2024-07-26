from qtstrap import *
from qtstrap.extras.code_editor import CodeLine, PythonHighlighter
import qtawesome as qta
from stagehand.sandbox import Sandbox, SandboxCompletionModel
from .sandbox_action_editor import ActionEditorDialog
from .items import ActionItem


class SandboxAction(ActionItem):
    name = 'sandbox'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.action = CodeLine(changed=changed, highlighter=PythonHighlighter, model=SandboxCompletionModel())
        self.action.ctrl_enter_pressed.connect(self.run)

        self.changed = changed

        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=qta.icon('fa5.edit'))
        self.edit_btn.setIconSize(QSize(22, 22))

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.action)
            layout.add(self.edit_btn)

    def open_editor(self, *_):
        self.data['action'] = self.action.text()
        self.data['name'] = self.owner.name
        self.editor = ActionEditorDialog(self.data, self.owner)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        text = self.editor.editor.toPlainText()
        self.action.setText(text)
        self.action.setDisabled('\n' in text)
        self.owner.label.setText(self.editor.label.text())
        self.changed()

    def set_data(self, data: dict):
        self.data = data
        if 'action' in data:
            self.action.setText(data['action'])
        self.action.setDisabled('\n' in self.action.text())

    def get_data(self):
        return {'action': self.action.text()}

    def reset(self):
        self.action.clear()
        self.action.setDisabled(False)

    def run(self):
        # Sandbox().run(self.action.text(), this=self.parent.this)
        Sandbox().run(self.action.text())
