from qtstrap import *
from stagehand.actions import TriggerItem
from pynput.keyboard import Listener, Key, KeyCode, HotKey


@singleton
class ListenerObject(QObject):
    press = Signal(Key)
    release = Signal(Key)

    def __init__(self):
        super().__init__()
        self.pressed_keys: set[Key] = set()

        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        App().aboutToQuit.connect(self.listener.stop)
        self.listener.start()

    def canonical(self, key: Key | KeyCode):
        return self.listener.canonical(key)

    def on_press(self, key: Key):
        if key not in self.pressed_keys:
            self.pressed_keys.add(key)
            self.press.emit(key)

    def on_release(self, key: Key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)
            self.release.emit(key)


class KeyboardTrigger(TriggerItem):
    name = 'keyboard'
    triggered = Signal()

    def __init__(self, changed, run, owner=None):
        super().__init__()

        self.owner = owner
        self.triggered.connect(run)

        self.type = QComboBox()
        self.type.addItems(['press', 'release', 'hotkey'])
        self.type.currentIndexChanged.connect(changed)

        self.listener = ListenerObject()
        self.listener.press.connect(self.on_press)
        self.listener.release.connect(self.on_release)

        self.value = QLineEdit()
        self.value.textChanged.connect(changed)
        self.value.textChanged.connect(self.on_change)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.type)
            layout.add(self.value)

    def on_change(self, text):
        if self.type.currentText() == 'hotkey':
            try:
                self.hotkey = HotKey(HotKey.parse(text), self.on_hotkey)
            except:
                self.hotkey = None

    def on_hotkey(self):
        self.triggered.emit()

    def on_press(self, key: Key):
        if self.value.hasFocus():
            return

        if self.type.currentText() == 'press':
            if key == KeyCode.from_char(self.value.text()):
                self.triggered.emit()
        elif self.type.currentText() == 'hotkey':
            if self.hotkey:
                self.hotkey.press(self.listener.canonical(key))

    def on_release(self, key: Key):
        if self.value.hasFocus():
            return

        if self.type.currentText() == 'release':
            if key == KeyCode.from_char(self.value.text()):
                self.triggered.emit()
        elif self.type.currentText() == 'hotkey':
            if self.hotkey:
                self.hotkey.release(self.listener.canonical(key))

    def set_data(self, data):
        self.type.setCurrentText(data.get('type', 'press'))
        self.value.setText(data.get('value', ''))

    def get_data(self):
        return {
            'type': self.type.currentText(),
            'value': self.value.text(),
        }
