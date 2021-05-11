from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import TriggerStackItem
from .pynput.keyboard import Listener, Key, KeyCode


@singleton
class ListenerObject(QObject):
    press = Signal(Key)
    release = Signal(Key)

    def __init__(self):
        super().__init__()
        self.pressed_keys = set()

        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        if key not in self.pressed_keys:
            self.pressed_keys.add(key)
            self.press.emit(key)

    def on_release(self, key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)
            self.release.emit(key)


class KeyboardTrigger(QWidget, TriggerStackItem):
    triggered = Signal()

    def __init__(self, changed, run):
        super().__init__()
        
        self.triggered.connect(run)

        self.type = QComboBox()
        self.type.addItems(['press', 'release', 'sequence'])
        self.type.currentIndexChanged.connect(changed)

        listener = ListenerObject()
        listener.press.connect(self.on_press)
        listener.release.connect(self.on_release)

        self.value = QLineEdit()
        self.value.textChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.value)

    def on_press(self, key):
        if self.value.hasFocus() or not self.isVisible():
            return
        if self.type.currentText() == 'press':
            if key == KeyCode.from_char(self.value.text()):
                self.triggered.emit()
        elif self.type.currentText() == 'sequence':
            pass

    def on_release(self, key):
        if self.value.hasFocus() or not self.isVisible():
            return
        if self.type.currentText() == 'release':
            if key == KeyCode.from_char(self.value.text()):
                self.triggered.emit()
        elif self.type.currentText() == 'sequence':
            pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

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
