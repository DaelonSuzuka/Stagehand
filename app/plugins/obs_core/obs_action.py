from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionStackItem
from .requests import requests
from .request_widgets import widgets


class ObsActionWidget(QWidget, ActionStackItem):
    def __init__(self, changed):
        super().__init__()
        self.changed = changed

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
            
        self.request_widget = widgets[self.type.currentText()](self.changed)
        self.layout().add(self.request_widget, 1)

    def from_dict(self, data):
        self.data = data
        try:
            self.type.setCurrentText(data['type'])
            if data['fields']:
                if self.request_widget:
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