from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem


class ActionSettings(QWidget):
    def __init__(self):
        super().__init__()

        with CVBoxLayout(self, margins=0) as layout:
            layout += QLabel('1')
            layout += QLabel('2')
            layout += QLabel('3')



class SaleaeAction(ActionItem):
    name = 'saleae'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed

        self.settings = ActionSettings()
        self.settings.hide()
        self.settings_button = QPushButton('Action Settings', clicked=self.toggle_settings)

        self.action = QComboBox()
        self.action.addItems(['Start', 'Stop'])
        self.action.currentIndexChanged.connect(changed)

        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox():
                layout += self.action
                layout.add(QLabel(), 1)
                layout += self.settings_button
            layout += self.settings
        
    def toggle_settings(self):
        self.settings.setVisible(not self.settings.isVisible())

    def set_data(self, data):
        self.data = data
        self.action.setCurrentText(data.get('action', 'Start'))

    def get_data(self):
        data = {
            'action': self.action.currentText(),
        }

        return data

    def run(self):
        pass