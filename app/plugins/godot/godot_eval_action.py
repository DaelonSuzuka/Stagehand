from qtstrap import *
from qtstrap.extras.code_editor import CodeLine
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem


class GodotEvalAction(QWidget, ActionItem):
    name = 'godot-eval'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed

        self.eval = CodeLine(changed=changed)
        
        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.eval)

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
        Sandbox().godot.eval(self.eval.text(), self.eval_result)

    def eval_result(self, message):
        Sandbox().tools.print(message['result'])