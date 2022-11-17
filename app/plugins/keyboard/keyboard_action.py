from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem


class KeyboardAction(QWidget, ActionItem):
    name = 'keyboard'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.type = QComboBox()
        self.type.addItems(['tap', 'press', 'release', 'type'])
        self.type.currentIndexChanged.connect(changed)

        self.value = QLineEdit()
        self.value.textChanged.connect(changed)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.type)
            layout.add(self.value)

    def set_data(self, data):
        try:
            self.type.setCurrentText(data['type'])
            self.value.setText(data['value'])
        except:
            pass

    def get_data(self):
        return {
            'type': self.type.currentText(),
            'value': self.value.text(),
        }

    def run(self):
        Sandbox().run(f"keyboard.{self.type.currentText()}('{self.value.text()}')")