from qtstrap import *


class ActionWidgetGroup(QObject):
    action_changed = Signal()

    def __init__(self, name, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.actions = []
        self.load()

    def register(self, action):
        self.actions.append(action)
        if action.name in self.prev_data:
            action.set_data(self.prev_data[action.name])
        action.changed.connect(self.on_action_change)

    def on_action_change(self):
        self.save()
        self.action_changed.emit()

    def load(self):
        self.prev_data = QSettings().value(self.name, {})

    def save(self):
        QSettings().setValue(self.name, self.get_data())

    def get_data(self):
        data = {}
        for action in self.actions:
            data[action.name] = action.to_dict()
        return data