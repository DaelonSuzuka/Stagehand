from qtstrap import *
from .action_widget import ActionWidget
from .action_group import ActionWidgetGroup
from stagehand.components import StagehandPage


class ActionsPage(StagehandPage):
    page_type = 'Generic Actions'
    changed = Signal()
    
    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name
        self.icon_name = 'mdi.format-list-checkbox'

        self.label = LabelEdit(f'Page {name}', changed=self.changed)
        self.group = ActionWidgetGroup(name, changed=self.on_change, parent=self, autosave=False)

        self.actions = []
        self.actions_container = CVBoxLayout()

        self.enabled = AnimatedToggle()
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
                # layout.add(QPushButton('Add Action'))
                layout.add(self.enabled)
                layout.add(self.group.filter)
            with layout.scroll(margins=0):
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.actions_container)
                layout.add(QWidget(), 1)

    def get_name(self):
        return self.label.text()

    def on_change(self):
        self.changed.emit()

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
            actions = {}
            for i in range(1, 13):
                name = f'Action {i}'
                actions[name] = {
                    "name": name,
                    "label": name,
                    "action_type": "sandbox",
                    "action": "",
                    "trigger": {
                        "enabled": True,
                        "trigger_type": "sandbox",
                        "trigger": ""
                    },
                    "filter": {
                        "enabled": True,
                        "filters": []
                    }
                }
            data['actions'] = actions
            self.group.set_data(data)

            self.actions = [ActionWidget(f'Action {i}', group=self.group) for i in range(1, 13)]
            self.actions_container.add(self.actions)
            
    def get_data(self):
        data = {
            'page_type': self.page_type,
            'label': self.label.text(),
            'enabled': self.enabled.isChecked(),
            **self.group.get_data(),
        }
        return data