from pynput.keyboard import GlobalHotKeys
from qtstrap import *

from stagehand.actions import ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandPage

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


class RadialActionWidget(ActionWidget):
    @classmethod
    def make_default_data(cls, name):
        return {
            'name': name,
            'enabled': True,
            'action': {'type': 'sandbox', 'action': f'print("{name}")'},
            'trigger': {'enabled': False, 'trigger_type': 'sandbox', 'trigger': ''},
            'filter': {'enabled': False, 'filters': []},
        }

    def do_layout(self):
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.label)
            layout.add(VLine())
            layout.add(self.action, 2)
            layout.add(self.run_btn)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction('Run').triggered.connect(self.run)
        menu.addAction('Rename').triggered.connect(self.label.start_editing)
        menu.addAction('Copy').triggered.connect(self.copy)
        menu.addAction('Paste').triggered.connect(self.paste)
        # menu.addAction(self.trigger.enabled)
        # menu.addAction(self.filter.enabled)
        menu.addAction('Reset').triggered.connect(self.reset)
        menu.addAction('Remove').triggered.connect(self.remove)
        menu.exec_(event.globalPos())


class RadialMenuPage(StagehandPage):
    page_type = 'Radial Menu'

    changed = Signal()

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name

        self.menu = None

        # self.listener = ListenerObject('<ctrl>+<space>', self.open_popup)

        self.group = ActionWidgetGroup(name, changed=self.on_change, parent=self, autosave=False)

        self.label = LabelEdit(f'Radial {name}', changed=self.changed)

        self._actions: dict[str, RadialActionWidget] = {}
        self.actions_container = CVBoxLayout()

        self.enabled = AnimatedToggle()
        self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        self.hotkey = QLineEdit(textChanged=self.on_change)
        self.hotkey.setText('<ctrl>+<space>')

        self.color = QLineEdit(textChanged=self.on_change)
        self.color.setText('')

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)

        with CVBoxLayout(self) as layout:
            with layout.hbox(margins=0):
                layout.add(QWidget())
                layout.add(self.label)
                layout.add(QWidget(), 1)
                layout.add(self.color)
                layout.add(self.hotkey)
                layout.add(self.enabled)
                layout.add(QPushButton('New Action', clicked=self.create_action))
                # layout.add(self.group.filter)
            with layout.scroll(margins=0):
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.actions_container)
                layout.add(QLabel(), 1)

    def get_name(self):
        return self.label.text()

    def on_change(self):
        self.changed.emit()

    def hotkey_changed(self, new):
        print(new)

    def color_changed(self, new):
        print(new)

    def get_unique_action_name(self):
        name = f'Radial Action {len(self._actions) + 1}'

        action_names = [a.name for a in self._actions.values()]
        i = 0
        while name in action_names:
            i += 1
            name = f'Radial Action {len(self._actions) + 1 + i}'

        return name

    def create_action(self, data=None):
        name = self.get_unique_action_name()

        if data:
            name = data.get('name', name)
            data['name'] = name
        else:
            data = RadialActionWidget.make_default_data(name)

        action = RadialActionWidget(name, group=self.group)
        action.set_data(data)
        self.actions[name] = action
        self.actions_container.add(action)

    def open_popup(self):
        if self.menu:
            self.menu.move_to_cursor()
            return
        self.menu = RadialPopup(list(self._actions.keys()), bg=self.color.text())
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

        self.enabled.setChecked(data.get('enabled', True))
        self.hotkey.setText(str(data.get('hotkey', '<ctrl>+<space>')))
        self.color.setText(str(data.get('color', '')))

        # if self.listener:
        #     self.listener.stop()

        self.listener = ListenerObject(self.hotkey.text(), self.open_popup)

        if actions := data.get('actions'):
            for action_data in actions:
                action = RadialActionWidget(action_data['name'], group=self.group)
                action.set_data(action_data)
                self._actions[action.name] = action
                self.actions_container.add(action)
        else:
            self.actions = {}
            for i in range(1, 7):
                name = f'Radial Action {i}'
                action = RadialActionWidget(name=name, group=self.group)
                self._actions[name] = action

                data = RadialActionWidget.make_default_data(name)
                action.set_data(data)

            self.actions_container.add(list(self._actions.values()))

    def get_data(self):
        return {
            'page_type': self.page_type,
            'enabled': self.enabled.isChecked(),
            'hotkey': self.hotkey.text(),
            'color': self.color.text(),
            **self.group.get_data(),
        }
