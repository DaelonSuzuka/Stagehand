from typing import Self

from qtstrap import *

from .radial_action import RadialActionWidget


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