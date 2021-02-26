from qt import *
from obs import Sandbox


class ActionWidget(QWidget):
    def __init__(self, name, parent=None):
        super().__init__(parent=parent)

        self.name = QLabel(name)
        self.action = PersistentLineEdit(f'{name}_action')
        self.run_btn = QPushButton('Run', clicked=self.run)

        with CHBoxLayout(self) as layout:
            layout.add(self.name)
            layout.add(self.action)
            layout.add(self.run_btn)

    def run(self):
        Sandbox().run(self.action.text())


class GenericActionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.actions = []

        for i in range(8):
            self.actions.append(ActionWidget(f'Action {i}'))

        with CVBoxLayout(self) as layout:
            for action in self.actions:
                layout.add(action)
            layout.add(QLabel(), 1)