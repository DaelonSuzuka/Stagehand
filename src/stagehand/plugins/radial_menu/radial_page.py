from pynput.keyboard import GlobalHotKeys
from qtstrap import *

from stagehand.components import StagehandPage

from stagehand.actions import CompactActionWidget, ActionWidget, ActionWidgetGroup

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

    def stop(self):
        self.listener.stop()

    def hotkey_pressed(self):
        self.press.emit()


class RadialMenuPage(StagehandPage):
    page_type = 'Radial Menu'

    changed = Signal()

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name

        self.menu = None

        self.listener = ListenerObject('<ctrl>+<space>', self.open_popup)
        self.group = ActionWidgetGroup(name, changed=self.on_change, parent=self, autosave=False)

        self._actions: dict[str, CompactActionWidget] = {}
        self.actions_container = CVBoxLayout()

        # self.enabled = AnimatedToggle()
        # self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)

        with CVBoxLayout(self) as layout:
            with layout.scroll(margins=0):
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.actions_container)
                layout.add(QLabel(), 1)

    def get_name(self):
        return self.name

    def on_change(self):
        self.changed.emit()

    def open_popup(self):
        if self.menu:
            self.menu.move_to_cursor()
            return
        self.menu = RadialPopup(list(self._actions.keys()))
        self.menu.buttonClicked.connect(self.popup_clicked)
        self.menu.exec()

    def popup_clicked(self, result):
        self.menu.deleteLater()
        self.menu = None
        if result in self._actions:
            self._actions[result].run()

    def set_data(self, data):
        self.data = data
        self.group.set_data(self.data)

        if actions := data.get('actions'):
            for action_data in actions:
                action = CompactActionWidget(action_data['name'], group=self.group)
                action.set_data(action_data)
                self._actions[action.name] = action
                self.actions_container.add(action)
        else:
            self.actions = {}
            for i in range(1, 7):
                name = f'Radial Action {i}'
                action = CompactActionWidget(name=name, group=self.group)
                self._actions[name] = action
                data = {**CompactActionWidget.default_data, 'name': name}
                data['action']['action'] = f'print("{name}")'
                action.set_data(data)

            self.actions_container.add(list(self._actions.values()))

    def get_data(self):
        return {
            'page_type': self.page_type,
            **self.group.get_data(),
        }
