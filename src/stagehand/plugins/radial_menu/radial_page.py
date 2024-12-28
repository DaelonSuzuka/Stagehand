from typing import Self

import qtawesome as qta
from qtstrap import *
from stagehand.actions import ActionFilter, ActionTrigger, ActionWidget
from stagehand.components import StagehandPage

from .radial_menu import ArcSegment, MenuScene, RadialPopup


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
        self.action.label.hide()

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
        menu.addAction('Reset').triggered.connect(self.reset)
        menu.addAction('Remove').triggered.connect(self.remove)
        menu.exec_(event.globalPos())


class RadialItemWidget(QWidget):
    changed = Signal()
    deleted = Signal(object)

    def __init__(self, name: str, changed=None, deleted=None, level=0):
        super().__init__()

        self.name = name
        self.level = level

        self.label = LabelEdit(f'{name}', changed=self.changed)

        data = RadialActionWidget.make_default_data(f'{name} Left')
        self.left_click = RadialActionWidget('Left Click', data=data)
        data = RadialActionWidget.make_default_data(f'{name} Right')
        self.right_click = RadialActionWidget('Right Click', data=data)

        self.icon_button = QPushButton('Icon')

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

        if deleted:
            self.deleted.connect(deleted)

        self.action_container = CVBoxLayout(margins=0)
        self.children_container = CVBoxLayout(margins=0)

        self._actions: list[RadialActionWidget] = []
        self._children: list[RadialItemWidget] = []

        self.action_container += self.left_click
        self._actions.append(self.left_click)
        self.action_container += self.right_click
        self._actions.append(self.right_click)

        if level == 0:
            self.add_child()
            self.add_child()

        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                with layout.vbox(margins=0):
                    with layout.hbox(margins=0):
                        layout.add(self.label)
                        layout.add(QWidget(), 1)
                    with layout.hbox(margins=0):
                        # layout += self.icon_button
                        # layout.add(QLabel('Icon:'))
                        # layout.add(QLineEdit())
                        layout += self.background
                        layout += self.hover
                        layout.add(QWidget(), 1)
                    layout.add(QWidget(), 1)
                with layout.vbox(margins=0, stretch=5):
                    layout += self.action_container
                    layout += self.children_container
                    layout.add(QWidget(), 1)
            if level == 0:
                layout += HLine()

    def on_click(self, event: QGraphicsSceneMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.left_click.run()
        if event.button() == Qt.MouseButton.RightButton:
            self.right_click.run()

    def on_change(self):
        self.changed.emit()

    def get_unique_child_name(self):
        name = f'Child Action {len(self._children) + 1}'

        action_names = [a.name for a in self._children]
        i = 0
        while name in action_names:
            i += 1
            name = f'Child Action {len(self._children) + 1 + i}'

        return name

    def add_child(self):
        name = self.get_unique_child_name()
        item = RadialItemWidget(
            name,
            self.on_change,
            deleted=self.delete_child,
            level=self.level + 1,
        )
        self._children.append(item)
        self.children_container += item

    def delete_child(self, item: Self):
        if item in self._children:
            self._children.remove(item)
        item.deleteLater()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        # menu.addAction('Run').triggered.connect(self.run)
        # menu.addAction('Rename').triggered.connect(self.label.start_editing)
        # menu.addAction('Copy').triggered.connect(self.copy)
        # menu.addAction('Paste').triggered.connect(self.paste)
        # menu.addAction(self.trigger.enabled)
        # menu.addAction(self.filter.enabled)
        menu.addAction('Add Action')
        menu.addAction('Add Child').triggered.connect(self.add_child)
        menu.addAction('Remove').triggered.connect(lambda: self.deleted.emit(self))
        menu.exec_(event.globalPos())

    def remove(self):
        self.deleteLater()

    # def get_data(self):
    #     return {
    #         'page_type': self.page_type,
    #         'name': self.label.text(),
    #         'enabled': self.enabled.isChecked(),
    #         'background': self.background.color.name(),
    #         'hover': self.hover.color.name(),
    #         **self.trigger.get_data(),
    #         **self.filter.get_data(),
    #     }


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

    def delete_item(self, item: RadialItemWidget):
        if item in self._items:
            self._items.remove(item)
        item.deleteLater()

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
            step = 360 // count
            offset = 90

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

                for child in item._children:
                    print(child)

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

        for i in range(1, 7):
            name = f'Radial Action {i}'
            item = RadialItemWidget(name=name, changed=self.on_change, deleted=self.delete_item)
            self.items_container.add(item)
            self._items.append(item)

        # if actions := data.get('actions'):
        #     for action_data in actions:
        #         action = RadialActionWidget(action_data['name'])
        #         action.set_data(action_data)
        #         self._actions[action.name] = action
        #         self.actions_container.add(action)
        # else:
        #     self._actions = {}
        #     for i in range(1, 7):
        #         name = f'Radial Action {i}'
        #         action = RadialActionWidget(name=name)
        #         self._actions[name] = action

        #         data = RadialActionWidget.make_default_data(name)
        #         action.set_data(data)

        #     self.actions_container.add(list(self._actions.values()))

    def get_data(self):
        return {
            'page_type': self.page_type,
            'name': self.label.text(),
            'enabled': self.enabled.isChecked(),
            'background': self.background.color.name(),
            'hover': self.hover.color.name(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
        }
