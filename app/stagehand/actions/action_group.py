from qtstrap import *
from .action_filter import ActionFilter


class ActionWidgetGroup(QObject):
    action_changed = Signal()

    def __init__(self, name, parent=None, changed=None, autosave=True):
        super().__init__(parent=parent)
        self.this = parent
        self.name = name
        self.autosave = autosave

        self.data = {
            'actions': {},
            'filter': {
                'enabled': True,
                'filters': []
            }
        }

        self.filter = ActionFilter(self.action_changed, owner=self)
        self.active = True

        if changed:
            self.action_changed.connect(changed)

        self.actions = []
        if autosave:
            self.load()

    def register(self, action):
        self.actions.append(action)
        
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

    def set_data(self, data):
        self.data = data
        self.filter.set_data(self.data)
        self.filter.enabled.setChecked(True)

    def get_data(self):
        data = {
            'actions': [a.get_data() for a in self.actions],
            **self.filter.get_data(),
        }
        return data