from qtstrap import *
from pynput.keyboard import Key, Controller
from stagehand.sandbox import Sandbox, _Sandbox
from stagehand.actions import ActionStack


class Keyboard:
    def __init__(self):
        self.controller = Controller()

    def __getattr__(self, name):
        return getattr(Key, name)

    def key(self, k):
        self.controller.press(k)
        self.controller.release(k)

    def press(self, key):
        self.controller.press(key)

    def release(self, key):
        self.controller.release(key)


class KeyboardActionWidget(QWidget):
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
        try:
            self.type.setCurrentText(data['type'])
            self.value.setText(data['value'])
        except:
            pass

    def to_dict(self):
        return {
            'type': self.type.currentText(),
            'value': self.value.text(),
        }

    def run(self):
        Sandbox().run(f"keyboard.{self.type.currentText()}('{self.value.text()}')")



def install_plugin():
    ActionStack.actions['keyboard'] = KeyboardActionWidget

    keyboard = Keyboard()
    _Sandbox.extensions['kb'] = keyboard
    _Sandbox.extensions['keyboard'] = keyboard


install_plugin()