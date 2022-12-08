from qtstrap import *
from .action_filter import ActionFilter


class ActionWidgetGroup(QObject):
    action_changed = Signal()

    def __init__(self, name, parent=None, changed=None, autosave=True):
        super().__init__(parent=parent)
        self.this = parent
        self.name = name
        self.autosave = autosave

        self.filter = ActionFilter(self.action_changed, owner=self)
        self.active = True

        if changed:
            self.action_changed.connect(changed)

        self.actions = []
        if autosave:
            self.load()

    def register(self, action):
        self.actions.append(action)
        if action.name in self.data:
            action.set_data(self.data[action.name])
        if 'actions' in self.data:
            if action.name in self.data['actions']:
                action.set_data(self.data['actions'][action.name])
        else:
            action.set_data(action.get_data())
        action.changed.connect(self.on_action_change)
        action.action.this = self.this

    def on_action_change(self):
        if self.autosave:
            self.save()
        self.action_changed.emit()

    def set_active(self, value: bool):
        self.active = value

    def can_run(self) -> bool:
        if not self.active:
            return False
        if not self.filter.check_filters():
            return False
        return True
        
    def load(self):
        self.data = QSettings().value(self.name, {})
        self.data['label'] = self.name
        self.filter.set_data(self.data)
        self.filter.enabled.setChecked(True)

    def save(self):
        QSettings().setValue(self.name, self.get_data())

    def set_data(self, data):
        self.data = data
        self.filter.set_data(self.data)
        self.filter.enabled.setChecked(True)

    def get_data(self):
        data = {
            'actions': {},
            **self.filter.get_data(),
        }
        for action in self.actions:
            data['actions'][action.name] = action.get_data()
        return data