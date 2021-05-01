from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionStackItem
from stagehand.obs import requests
from .obs_extension import ObsExtension
from .obs_api import api


class FieldBox(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        if changed:
            self.currentIndexChanged.connect(changed)


from .requests import *
from .base_classes import BaseRequest

requests = [r.__name__ for r in BaseRequest.__subclasses__()]



class ObsActionWidget(QWidget, ActionStackItem):
    def __init__(self, changed):
        super().__init__()

        self.obs = ObsExtension()

        self.type = QComboBox()
        self.type.addItems(requests)
        
        self.fields = [FieldBox(changed, self) for i in range(5)]

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.reload_fields)
        
        self.reload_fields()

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            for field in self.fields:
                layout.add(field)

    def reload_fields(self, data=None):
        return
        field_names = api[self.type.currentText()]['fields']
        num_of_fields = len(field_names)

        for i in range(5):
            self.fields[i].setVisible(i < num_of_fields)

        for i in range(num_of_fields):
            field = self.fields[i]
            name = field_names[i]
            if name == 'scene':
                self.get_scenes(field)
            if name == 'source':
                self.get_sources(field)
            if name == 'filter':
                self.get_sources(field)
        
    def get_scenes(self, field):
        value = field.currentText()
        def cb(msg):
            scenes = [s['name'] for s in msg['scenes']]
            field.clear()
            field.addItems(scenes)
            if value in scenes:
                field.setCurrentText(value)

        self.obs.get_scene_list(cb)

    def get_sources(self, field):
        value = field.currentText()
        def cb(msg):
            sources = [s['name'] for s in msg['sources']]
            field.clear()
            field.addItems(sources)
            if value in sources:
                field.setCurrentText(value)

        self.obs.get_source_list(cb)

    def from_dict(self, data):
        self.data = data
        try:
            self.type.setCurrentText(data['type'])
            # self.value.setCurrentText(data['value'])
            self.reload_fields(data)
        except:
            pass

    def to_dict(self):
        return {
            'type': self.type.currentText(),
            # 'value': self.value.currentText(),
        }

    def run(self):
        api[self.type.currentText()]['method'](self.value.currentText())