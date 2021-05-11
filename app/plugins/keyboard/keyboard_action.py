from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionStackItem, TriggerStackItem


class KeyboardTrigger(QWidget, TriggerStackItem):
    def __init__(self, changed):
        super().__init__()
        
        self.type = QComboBox()
        self.type.addItems(['key', 'press', 'release', 'sequence'])
        self.type.currentIndexChanged.connect(changed)

        self.value = QLineEdit()
        self.value.textChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.value)

    def from_dict(self, data):
        self.type.setCurrentText(data['type'])
        self.value.setText(data['value'])

    def to_dict(self):
        return {
            'type': self.type.currentText(),
            'value': self.value.text(),
        }


class KeyboardAction(QWidget, ActionStackItem):
    def __init__(self, changed):
        super().__init__()

        self.type = QComboBox()
        self.type.addItems(['key', 'press', 'release', 'sequence'])
        self.type.currentIndexChanged.connect(changed)

        self.value = QLineEdit()
        self.value.textChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.value)

    def from_dict(self, data):
        self.type.setCurrentText(data['type'])
        self.value.setText(data['value'])

    def to_dict(self):
        return {
            'type': self.type.currentText(),
            'value': self.value.text(),
        }

    def run(self):
        Sandbox().run(f"keyboard.{self.type.currentText()}('{self.value.text()}')")