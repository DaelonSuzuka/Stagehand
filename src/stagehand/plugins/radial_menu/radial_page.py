import qtawesome as qta
from qtstrap import *

from stagehand.actions import ActionFilter, ActionTrigger, ActionWidget, ActionWidgetGroup
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
            # layout.add(self.label)
            # layout.add(VLine())
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


class RadialButton(QWidget):
    """


    each button needs:
    - name
    - icon
    - hotkey
    - color palette
    - actions
    - child buttons

    """

    changed = Signal()

    def __init__(self, name: str, changed=None, level=0):
        super().__init__()

        self.menu_button = MenuButton(icon=qta.icon('mdi.menu'))
        self.menu_button.addAction('Add Action')
        self.menu_button.addAction('Add Submenu')

        self.label = LabelEdit(f'{name}', changed=self.changed)

        data = RadialActionWidget.make_default_data(name)

        self.left_click = RadialActionWidget('Left Click', data=data)
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

        self.action_container = CFormLayout(margins=0)
        self.children_container = CVBoxLayout(margins=0)

        self.action_container += ('Left Click', self.left_click)

        if level == 0:
            self.action_container += ('Right Click', self.right_click)

        # if level == 0:
        #     self.children_container += RadialButton('Child Action 1', self.on_change, level=level + 1)
        #     self.children_container += RadialButton('Child Action 2', self.on_change, level=level + 1)

        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                with layout.vbox(margins=0):
                    with layout.hbox(margins=0):
                        layout.add(self.label)
                        layout.add(QWidget(), 1)
                        layout.add(self.menu_button)
                        layout.add(QWidget())
                    with layout.hbox(margins=0):
                        # layout += self.icon_button
                        layout.add(QLabel('Icon:'))
                        layout.add(QLineEdit())
                        layout += self.background
                        layout += self.hover
                        layout.add(QWidget(), 1)

                    # with layout.hbox(margins=0):
                    #     layout.add(QWidget(), 1)
                    layout.add(QWidget(), 1)

                # layout += VLine()

                with layout.vbox(margins=0, stretch=5):
                    layout += self.action_container
                    layout.add(QWidget(), 1)

            if level == 0:
                layout += HLine()

            # with layout.hbox(margins=0):
            #     if level == 0:
            #         layout.add(QLabel('>'))

            #     layout += VLine()
            #     with layout.vbox(margins=0):
            #         layout += self.children_container
            #         layout.add(QWidget(), 1)

    def on_change(self):
        self.changed.emit()


class ColorPickerButton(QToolButton):
    changed = Signal()

    def __init__(self, title: str, color: QColor | str, changed):
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

        self._actions: dict[str, RadialActionWidget] = {}
        self.actions_container = CVBoxLayout(margins=0)

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
                layout.add(QPushButton('New Action', clicked=self.create_action))
                layout.add(self.filter)
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

        action = RadialActionWidget(name)
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
        ]

        with MenuScene(self.menu) as self.scene:
            # for i, angle in enumerate(range(0, 180, 180)):
            #     ArcSegment(
            #         start=angle + 90,
            #         end=angle + 180 + 90,
            #         icon=icons[i],
            #         normal_bg=self.background.color,
            #         hover_bg=self.hover.color,
            #     )

            for i, angle in enumerate(range(0, 360, 60), 0):
                ArcSegment(
                    start=angle + 90,
                    end=angle + 60 + 90,
                    icon=icons[i],
                    normal_bg=self.background.color,
                    hover_bg=self.hover.color,
                    show_ring=i < 3,
                )

            # ArcSegment(start=0, end=60, icon=icons[0])
            # ArcSegment(start=60, end=120, icon=icons[1])
            # ArcSegment(start=120, end=180, icon=icons[2])
            # ArcSegment(start=180, end=240, icon=icons[3])
            # ArcSegment(start=240, end=300, icon=icons[4])
            # ArcSegment(start=300, end=360, icon=icons[5])

            # for i, angle in enumerate(range(0, 360, 60)):
            #     ArcSegment(
            #         start=angle,
            #         end=angle + 60,
            #         icon=icons[i],
            #         normal_bg=self.background.color,
            #         hover_bg=self.hover.color,
            #     )

        # self.menu.buttonClicked.connect(self.popup_clicked)
        self.menu.exec()

    def popup_clicked(self, result):
        self.menu.deleteLater()
        self.menu = None
        if result in self._actions:
            self._actions[result].run()

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
            item = RadialButton(name=name, changed=self.on_change)
            self.actions_container.add(item)

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
