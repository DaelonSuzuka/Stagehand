from qtstrap import *
from qtstrap.extras.code_editor import CodeLine
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem
from .ahk_action_widgets import widgets


class AutohotkeyAction(QWidget, ActionItem):
    name = 'autohotkey'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed

        self.ahk_widget = None

        self.type = QComboBox()
        self.type.addItems(widgets.keys())

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.change_type)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.type)

    def change_type(self, *_):
        if self.ahk_widget:
            self.layout().removeWidget(self.ahk_widget)
            self.ahk_widget.deleteLater()
            
        self.ahk_widget = widgets[self.type.currentText()](changed=self.changed, owner=self.owner)
        self.layout().add(self.ahk_widget, 1)

    def set_data(self, data):
        self.data = data
        try:
            self.type.setCurrentText(data['type'])
            self.change_type()
            if data['fields']:
                if self.ahk_widget:
                    self.ahk_widget.set_data(data['fields'])
                    self.ahk_widget.refresh()
        except:
            pass

    def get_data(self):
        data = {
            'type': self.type.currentText(),
            'fields': {},
        }

        if self.ahk_widget:
            data['fields'] = self.ahk_widget.get_data()

        return data

    def run(self):
        if self.ahk_widget:
            self.ahk_widget.run()
