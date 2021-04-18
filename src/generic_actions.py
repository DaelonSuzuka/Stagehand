from qtstrap import *
from obs import ActionWidget


class GenericActionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        default = {f'Action {i}': ActionWidget.default_data(f'Action {i}') for i in range(1, 13)}
        prev_data = QSettings().value('generic_action', default)
        
        self.actions = {}
        for i in range(1, 13):
            name = f'Action {i}'
            self.actions[name] = ActionWidget(data=prev_data[name], changed=self.save_actions)

        with CVBoxLayout(self) as layout:
            for _, action in self.actions.items():
                layout.add(action)
            layout.add(QLabel(), 1)

    def save_actions(self):
        data = {name: action.to_dict() for name, action in self.actions.items()}

        QSettings().setValue('generic_action', data)