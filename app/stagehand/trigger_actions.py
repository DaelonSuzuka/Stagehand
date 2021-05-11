from qtstrap import *
from .actions import ActionWidget, ActionWidgetGroup


class TriggerActionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.group = ActionWidgetGroup('trigger_actions', self)

        self.actions = []
        for i in range(4):
            action = ActionWidget(f'Action {i + 1}', trigger=True, group=self.group)
            self.actions.append(action)

        with CVBoxLayout(self) as layout:
            for action in self.actions:
                layout.add(action)
            layout.add(QLabel(), 1)