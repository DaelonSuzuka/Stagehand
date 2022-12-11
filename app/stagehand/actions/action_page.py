from qtstrap import *
from .action_widget import ActionWidget
from .action_group import ActionWidgetGroup
from stagehand.components import StagehandPage
import json


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

        self.enabled = AnimatedToggle()
        self.enabled.stateChanged.connect(lambda _: self.group.set_active(self.enabled.isChecked()))
        self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)
        
        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                layout.add(QWidget())
                layout.add(self.label)
                layout.add(QWidget(), 1)
                layout.add(self.enabled)
                layout.add(QPushButton('New Action', clicked=self.create_action))
                layout.add(self.group.filter)
            with layout.scroll(margins=0):
                self.scroll = layout._layout
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.actions_container)
                layout.add(QWidget(), 1)

    def get_name(self):
        return self.label.text()

    def on_change(self):
        self.changed.emit()

    def create_action(self, data=None, index=None):
        name = f'Action {len(self.actions) + 1}'

        # make sure the action name is unique
        action_names = [a.name for a in self.actions]
        i = 0
        while name in action_names:
            i += 1
            name = f'Action {len(self.actions) + 1 + i}'

        if data:
            data['name'] = name
        else:
            data = {
                **ActionWidget.default_data,
                "name": name,
                "label": name,
            }
        if 'actions' not in self.group.data:
            self.group.data['actions'] = {}
        self.group.data['actions'][name] = data

        action = ActionWidget(name, group=self.group)
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

        label = f'Page {self.name}'
        if 'label' in data:
            label = data['label']
        self.label.setText(label)

        self.enabled.setChecked(data.get('enabled', True))

        if 'actions' in data and data['actions']:
            for name in data['actions']:
                action = ActionWidget(name, group=self.group)
                self.actions.append(action)
                self.actions_container.add(action)
        else:
            self.actions = [ActionWidget(f'Action {i}', group=self.group) for i in range(1, 2)]
            self.actions_container.add(self.actions)
            
    def get_data(self):
        data = {
            'page_type': self.page_type,
            'label': self.label.text(),
            'enabled': self.enabled.isChecked(),
            **self.group.get_data(),
        }
        return data