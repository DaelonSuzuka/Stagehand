from qtstrap import *
from .actions import ActionWidget, ActionWidgetGroup


class GenericActionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.group = ActionWidgetGroup('generic_actions', self)
        self.actions = [ActionWidget(f'Action {i}', group=self.group) for i in range(1, 13)]

        with CVBoxLayout(self) as layout:
            for action in self.actions:
                layout.add(action)
            layout.add(QLabel(), 1)