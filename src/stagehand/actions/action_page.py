from qtstrap import *
from .action_widget import ActionWidget
from .action_group import ActionWidgetGroup
from stagehand.components import StagehandPage
import json


class CustomAnimatedToggle(AnimatedToggle):
    def sizeHint(self):
        return QSize(50, 32)


class ActionsPage(StagehandPage):
    page_type = 'Generic Actions'
    changed = Signal()

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name
        self.icon_name = 'mdi.format-list-checkbox'

        self.setAcceptDrops(True)

        self.label = LabelEdit(f'Page {name}', changed=self.changed)
        self.group = ActionWidgetGroup(name, changed=self.on_change, parent=self, autosave=False)

        self.actions = []
        self.actions_container = CVBoxLayout()

        self.enabled = CustomAnimatedToggle()
        self.enabled.stateChanged.connect(lambda _: self.group.set_active(self.enabled.isChecked()))
        self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)

        with CVBoxLayout(self, margins=2) as layout:
            with layout.hbox(margins=0):
                layout.add(QWidget())
                layout.add(self.label)
                layout.add(QWidget(), 1)
                layout.add(self.enabled)
                layout.add(QPushButton('New Action', clicked=self.create_action))
                layout.add(self.group.filter)
            with layout.scroll(margins=0) as self.scroll:
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.actions_container)
                layout.add(QWidget(), 1)

    def get_name(self):
        return self.label.text()

    def on_change(self):
        self.changed.emit()

    def get_unique_action_name(self):
        name = f'Action {len(self.actions) + 1}'

        # make sure the action name is unique
        action_names = [a.name for a in self.actions]
        i = 0
        while name in action_names:
            i += 1
            name = f'Action {len(self.actions) + 1 + i}'

        return name

    def create_action(self, data=None, index=None):
        name = self.get_unique_action_name()

        if data:
            name = data.get('name', name)
            data['name'] = name
        else:
            data = {
                **ActionWidget.default_data,
                'name': name,
            }

        action = ActionWidget(name, group=self.group)
        action.set_data(data)
        if index:
            self.actions.insert(index, action)
            self.actions_container.insertWidget(index, action)
        else:
            self.actions.append(action)
            self.actions_container.add(action)

    def accept_action_drop(self, action_data=None) -> None:
        self.create_action(action_data)

    def dragEnterEvent(self, event) -> None:
        mime = event.mimeData()
        if mime.hasFormat('action_drop'):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        pos = event.pos()
        if not self.scroll.geometry().contains(pos):
            event.ignore()
            return
        event.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        pos = event.pos()

        if not self.scroll.geometry().contains(pos):
            event.ignore()
            return

        mime = event.mimeData()
        if not mime.hasFormat('action_drop'):
            event.ignore()
            return

        data = json.loads(bytes(mime.data('action_drop')).decode())

        after = None
        for a in self.actions:
            if a.geometry().contains(pos):
                if data['name'] == a.name:
                    event.ignore()
                    return
                after = a
                break
        else:
            after = a

        event.accept()
        idx = self.actions.index(after) + 1
        self.create_action(data, index=idx)

    def set_data(self, data):
        self.data = data
        self.group.set_data(self.data)

        self.label.setText(data.get('name', self.name))
        self.enabled.setChecked(data.get('enabled', True))

        if actions := data.get('actions'):
            for action_data in actions:
                action = ActionWidget(action_data['name'], group=self.group)
                action.set_data(action_data)
                self.actions.append(action)
                self.actions_container.add(action)
        else:
            self.create_action()

    def get_data(self):
        data = {
            'page_type': self.page_type,
            'name': self.label.text(),
            'enabled': self.enabled.isChecked(),
            **self.group.get_data(),
        }
        return data
