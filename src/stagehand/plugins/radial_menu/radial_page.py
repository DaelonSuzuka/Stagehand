from qtstrap import *
from stagehand.actions import ActionFilter, ActionTrigger, ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandPage

from .radial_menu import RadialPopup


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


class ColorPickerButton(QToolButton):
    changed = Signal()

    def __init__(self, title: str, color: QColor, changed):
        super().__init__()
        self.title = title
        self.set_color(color)
        self.setToolTip(title)
        self.setMinimumSize(30, 30)

        self.clicked.connect(self.on_click)
        self.changed.connect(changed)

    def on_click(self):
        self.dialog = QColorDialog(self.color)
        self.dialog.setWindowTitle(self.title)
        self.dialog.setModal(True)
        self.dialog.show()
        self.dialog.colorSelected.connect(self.color_selected)

    def set_color(self, new_color: QColor | str):
        self.color = QColor(new_color)
        self.setStyleSheet(f'background:{self.color.name()}')

    def color_selected(self, new_color: QColor):
        self.set_color(new_color)
        self.changed.emit()


class RadialMenuPage(StagehandPage):
    page_type = 'Radial Menu'
    icon_name = 'ri.share-circle-line'

    changed = Signal()

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name

        self.menu = None

        self.label = LabelEdit(f'Radial {name}', changed=self.changed)

        self.trigger = ActionTrigger(self.on_change, run=self.open_popup, owner=self)
        self.filter = ActionFilter(self.on_change, owner=self)
        self.group = ActionWidgetGroup(name, changed=self.on_change, parent=self, autosave=False)

        self._actions: dict[str, RadialActionWidget] = {}
        self.actions_container = CVBoxLayout()

        self.enabled = AnimatedToggle()
        self.enabled.setToolTip('Enable/Disable Menu')
        self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        self.background = ColorPickerButton(
            title='Radial Menu Background Color',
            color='#676767',
            changed=self.on_change,
        )
        self.hover = ColorPickerButton(
            title='Radial Menu Hover Color',
            color='#0078d4',
            changed=self.on_change,
        )

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)

        with CVBoxLayout(self) as layout:
            with layout.hbox(margins=0):
                layout.add(QWidget())
                layout.add(self.label)
                layout.add(self.trigger)
                layout.add(self.filter)
                layout.add(QWidget(), 1)
                layout.add(self.background)
                layout.add(self.hover)
                # layout.add(self.hotkey)
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
        if not self.enabled:
            return

        if not self.filter.check_filters():
            return

        if self.menu:
            # self.menu.move_to_cursor()
            self.menu.deleteLater()
            self.menu = None
            return
        self.menu = RadialPopup(
            list(self._actions.keys()),
            bg=self.background.color,
            hover=self.hover.color,
        )
        self.menu.buttonClicked.connect(self.popup_clicked)
        self.menu.exec()

    def popup_clicked(self, result):
        self.menu.deleteLater()
        self.menu = None
        if result in self._actions:
            self._actions[result].run()

    def set_data(self, data):
        self.data = data
        self.label.setText(data.get('name', self.name))
        self.trigger.set_data(data)
        self.filter.set_data(data)
        self.group.set_data(self.data)

        self.enabled.setChecked(data.get('enabled', True))
        self.background.set_color(data.get('background', '#676767'))
        self.hover.set_color(data.get('hover', '#0078d4'))

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
            'name': self.label.text(),
            'enabled': self.enabled.isChecked(),
            'background': self.background.color.name(),
            'hover': self.hover.color.name(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
            **self.group.get_data(),
        }
