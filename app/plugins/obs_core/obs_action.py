from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionStackItem
# from stagehand.obs import requests
from .obs_extension import ObsExtension
from .obs_api import api


class FieldBox(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        if changed:
            self.currentIndexChanged.connect(changed)


from .requests import *
from .base_classes import BaseRequest

requests = {}
for request in BaseRequest.__subclasses__():
    if request.fields:
        requests[request.__name__] = request


class ObsActionWidget(QWidget, ActionStackItem):
    def __init__(self, changed):
        super().__init__()
        self.changed = changed

        self.obs = ObsExtension()

        self.request_widget = None

        self.type = QComboBox()
        self.type.addItems(requests.keys())

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.change_type)
        
        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)

    def change_type(self, *_):
        if self.request_widget:
            self.layout().removeWidget(self.request_widget)
            self.request_widget.deleteLater()
            
        self.request_widget = requests[self.type.currentText()].Widget(self.changed)
        self.layout().add(self.request_widget, 1)

    def from_dict(self, data):
        self.data = data
        try:
            self.type.setCurrentText(data['type'])
            if data['fields']:
                self.request_widget.from_dict(data['fields'])
                self.request_widget.refresh()
        except KeyError:
            pass

    def to_dict(self):
        data = {
            'type': self.type.currentText(),
            'fields': {},
        }

        if self.request_widget:
            data['fields'] = self.request_widget.to_dict()

        return data

    def run(self):
        if self.request_widget:
            payload = self.request_widget.payload()
            Sandbox().obs.send(payload)