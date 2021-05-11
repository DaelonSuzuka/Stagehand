from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import TriggerStackItem
from .pynput.keyboard import Listener, Key
import threading


class ListenerObject(QObject):
    press = Signal(Key)
    release = Signal(Key)

    def __init__(self):
        super().__init__()

        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        self.press.emit(key)

    def on_release(self, key):
        self.release.emit(key)


listener = None


class KeyboardTrigger(QWidget, TriggerStackItem):
    def __init__(self, changed):
        super().__init__()
        
        self.type = QComboBox()
        self.type.addItems(['key', 'press', 'release', 'sequence'])
        self.type.currentIndexChanged.connect(changed)

        global listener
        if listener is None:
            listener = ListenerObject()

        listener.press.connect(self.on_press)
        listener.release.connect(self.on_release)

        # self.thread = threading.Thread(name='keyboard_listener', target=start_listener, daemon=True)
        # self.thread.start()

        self.value = QLineEdit()
        self.value.textChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.value)

    def on_press(self, key):
        if self.isVisible():
            print('press:', key)

    def on_release(self, key):
        if self.isVisible():
            print('release:', key)

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
