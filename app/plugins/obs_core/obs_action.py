from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionItem
from .requests import requests
from .request_widgets import widgets


def filt(r:str) -> bool:
    if r.startswith('Get'):
        return False
    if r in ['Authenticate']:
        return False
    return True

request_names = [r for r in requests.keys() if filt(r)]


class ObsAction(QWidget, ActionItem):
    name = 'obs'

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed

        self.request_widget = None

        self.type = QComboBox()
        # this can't be editable without some additional work to make completion and search
        # behave better
        # self.type.setEditable(True)
        self.type.addItems(request_names)

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.change_type)
        
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.type)

    def change_type(self, *_):
        if self.request_widget:
            self.layout().removeWidget(self.request_widget)
            self.request_widget.deleteLater()
            
        self.request_widget = widgets[self.type.currentText()](self.changed)
        self.layout().add(self.request_widget, 1)

    def set_data(self, data):
        self.data = data
        try:
            self.type.setCurrentText(data.get('type', 'SetCurrentScene'))
            if data['fields']:
                if self.request_widget:
                    self.request_widget.set_data(data['fields'])
                    self.request_widget.refresh()
        except KeyError:
            pass

    def get_data(self):
        data = {
            'type': self.type.currentText(),
            'fields': {},
        }

        if self.request_widget:
            data['fields'] = self.request_widget.get_data()

        return data

    def run(self):
        if self.request_widget:
            payload = self.request_widget.payload()
            Sandbox().obs.send(payload)