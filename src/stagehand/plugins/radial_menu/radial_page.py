from qtstrap import *
from stagehand.components import SingletonPageMixin, StagehandPage
from pynput.keyboard import GlobalHotKeys

from .radial import RadialPopup


class ListenerObject(QObject):
    press = Signal()

    def __init__(self, hotkey: str, cb=None):
        super().__init__()
        self.pressed_keys = set()

        hotkeys = {hotkey: self.hotkey_pressed}
        self.listener = GlobalHotKeys(hotkeys)
        qApp.aboutToQuit.connect(self.listener.stop)
        self.listener.start()

        if cb:
            self.press.connect(cb)

    def hotkey_pressed(self):
        self.press.emit()


class RadialMenuPage(SingletonPageMixin, StagehandPage):
    page_type = 'Radial Menu'
    tags = ['singleton', 'user']

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name

        self.menu = None

        self.listener = ListenerObject('<ctrl>+<space>', self.open_popup)
        self.status = QLabel('penis')

        with CVBoxLayout(self) as layout:
            layout.add(self.status)

    def open_popup(self):
        self.menu = RadialPopup()
        self.menu.buttonClicked.connect(self.popup_clicked)

    def popup_clicked(self, result):
        self.status.setText(f'{result}')
