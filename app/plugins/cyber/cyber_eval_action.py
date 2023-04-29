from qtstrap import *
from qtstrap.extras.code_editor import CodeLine
import qtawesome as qta
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem
from .cyber_script_editor import CyberScriptEditorDialog
from .cyber_script_highlighter import CyberHighlighter


class CyberEvalAction(ActionItem):
    name = 'cyber-eval'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed

        self.eval = CodeLine(changed=changed, highlighter=CyberHighlighter)
        self.eval.ctrl_enter_pressed.connect(self.run)
        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=qta.icon('fa5.edit'))
        self.edit_btn.setIconSize(QSize(22, 22))
        
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.eval)
            layout.add(self.edit_btn)

    def open_editor(self, *_):
        self.data['action'] = self.eval.text()
        self.data['name'] = self.owner.name
        self.editor = CyberScriptEditorDialog(self.data, self.owner)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        text = self.editor.editor.toPlainText()
        self.eval.setText(text)
        self.eval.setDisabled('\n' in text)
        self.owner.label.setText(self.editor.label.text())
        self.changed()

    def set_data(self, data):
        self.data = data
        try:
            self.eval.setText(data['eval'])
        except KeyError:
            pass

    def get_data(self):
        data = {
            'eval': self.eval.text(),
        }

        return data

    def run(self):
        Sandbox().cyber.eval(self.eval.text())

    def eval_result(self, message):
        Sandbox().tools.print(message['result'])