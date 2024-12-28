import qtawesome as qta
from qtstrap import *
from stagehand.actions import ActionFilter, ActionTrigger
from stagehand.components import StagehandPage

from .radial_item import RadialItemWidget
from .radial_menu import ArcSegment, MenuScene, RadialPopup


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

        self._items: list[RadialItemWidget] = []
        self.items_container = CVBoxLayout(margins=0)

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

        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                layout.add(QWidget())
                layout.add(self.label)
                layout.add(self.trigger)
                layout.add(QWidget(), 1)
                layout.add(self.background)
                layout.add(self.hover)
                layout.add(self.enabled)
                layout.add(QPushButton('New Action', clicked=self.create_item))
                layout.add(self.filter)
                layout.add(QWidget())
            with layout.scroll(margins=0):
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.items_container)
                layout.add(QLabel(), 1)

    def get_name(self):
        return self.label.text()

    def on_change(self):
        self.changed.emit()

    def get_unique_item_name(self):
        name = f'Radial Action {len(self._items) + 1}'

        action_names = [a.name for a in self._items]
        i = 0
        while name in action_names:
            i += 1
            name = f'Radial Action {len(self._items) + 1 + i}'

        return name

    def create_item(self):
        name = self.get_unique_item_name()

        # if data:
        #     name = data.get('name', name)
        #     data['name'] = name
        # else:
        #     data = RadialActionWidget.make_default_data(name)

        action = RadialItemWidget(name, changed=self.on_change, deleted=self.delete_item)
        self._items.append(action)
        self.items_container.add(action)
        self.changed.emit()

    def delete_item(self, item: RadialItemWidget):
        if item in self._items:
            self._items.remove(item)
        item.deleteLater()
        self.changed.emit()

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

        self.menu = RadialPopup()

        icons = [
            qta.icon('ph.number-circle-one-fill', color='white'),
            qta.icon('ph.number-circle-two-fill', color='white'),
            qta.icon('ph.number-circle-three-fill', color='white'),
            qta.icon('ph.number-circle-four-fill', color='white'),
            qta.icon('ph.number-circle-five-fill', color='white'),
            qta.icon('ph.number-circle-six-fill', color='white'),
            qta.icon('ph.number-circle-seven-fill', color='white'),
            qta.icon('ph.number-circle-eight-fill', color='white'),
            qta.icon('ph.number-circle-nine-fill', color='white'),
        ]

        with MenuScene(self.menu) as self.scene:
            count = len(self._items)
            if count == 0:
                return
            step = 360 // count
            offset = 90
            if count == 4:
                offset = 45

            for i, angle in enumerate(range(0, 360, step), 0):
                item = self._items[i]
                arc = ArcSegment(
                    start=angle + offset,
                    end=angle + step + offset,
                    icon=icons[i],
                    normal_bg=self.background.color,
                    hover_bg=self.hover.color,
                    show_ring=bool(item._children),
                )
                arc.clicked.connect(item.on_click)

                # for child in item._children:
                #     print(child)

        # self.menu.buttonClicked.connect(self.popup_clicked)
        self.menu.exec()

    def popup_clicked(self, result):
        self.menu.deleteLater()
        self.menu = None
        # if result in self._actions:
        #     self._actions[result].run()

    def set_data(self, data):
        if 'trigger' not in data:
            data['trigger'] = {
                'enabled': False,
                'trigger_type': 'keyboard',
                'type': 'hotkey',
                'value': '<ctrl>+<space>',
            }

        self.data = data
        self.label.setText(data.get('name', self.name))
        self.trigger.set_data(data)
        self.filter.set_data(data)

        self.enabled.setChecked(data.get('enabled', True))
        self.background.set_color(data.get('background', '#676767'))
        self.hover.set_color(data.get('hover', '#0078d4'))

        if actions := data.get('actions'):
            for action_data in actions:
                action = RadialItemWidget(
                    action_data['name'],
                    changed=self.on_change,
                    deleted=self.delete_item,
                )
                action.set_data(action_data)
                self._items.append(action)
        else:
            self._items.clear()
            for i in range(1, 7):
                action = RadialItemWidget(
                    f'Radial Action {i}',
                    changed=self.on_change,
                    deleted=self.delete_item,
                )
                self._items.append(action)

        self.items_container.add(self._items)

    def get_data(self):
        return {
            'page_type': self.page_type,
            'name': self.label.text(),
            'enabled': self.enabled.isChecked(),
            'background': self.background.color.name(),
            'hover': self.hover.color.name(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
            'actions': [item.get_data() for item in self._items],
        }
