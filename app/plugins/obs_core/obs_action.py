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

        self.prev_type = ''
        self.request_widget = None

        self.type = QComboBox()
        self.type.addItems(requests.keys())
        self.placeholder = QLabel()

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.change_type)
        

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)

    def change_type(self, *_):
        if self.prev_type == self.type.currentText():
            return
        print('type changed')
        if self.request_widget:
            self.layout().removeWidget(self.request_widget)
            self.request_widget.deleteLater()
            
        self.request_widget = requests[self.type.currentText()].widget(print)
        self.layout().add(self.request_widget)

        self.reload_fields()

    def reload_fields(self, *_):
        # self.
        pass

        # field_names = requests[self.type.currentText()].fields
        # num_of_fields = len(field_names)

        # for i in range(5):
        #     self.fields[i].setVisible(i < num_of_fields)

        # for i in range(num_of_fields):
        #     field = self.fields[i]
        #     name = field_names[i]
            
        #     if name in ['scene', 'scene-name']:
        #         self.get_scenes(field)
        #     if name in ['source', 'sourceName']:
        #         self.get_sources(field)
        #     if name in ['filter', 'filterName']:
        #         self.get_filters(field, self.fields[i - 1].currentText())
        #     if 'Enabled' in name:
        #         field.clear()
        #         field.addItems(['True', 'False'])
        
        # self.changed()

    def get_scenes(self, field):
        def cb(msg):
            scenes = [s['name'] for s in msg['scenes']]
            value = field.currentText()
            field.clear()
            field.addItems(scenes)
            if value in scenes:
                field.setCurrentText(value)
            self.changed()

        self.obs.get_scene_list(cb)

    def get_sources(self, field):
        def cb(msg):
            sources = [s['name'] for s in msg['sources']]
            value = field.currentText()
            field.clear()
            field.addItems(sources)
            if value in sources:
                field.setCurrentText(value)
            self.changed()

        self.obs.get_source_list(cb)

    def get_filters(self, field, source):
        def cb(msg):
            if 'error' not in msg:
                filters = [f['name'] for f in msg['filters']]
                value = field.currentText()
                field.clear()
                field.addItems(filters)
                print(filters)
                if value in filters:
                    field.setCurrentText(value)
            self.changed()

        self.obs.get_filters(source, cb)

    def from_dict(self, data):
        self.data = data
        print('from_dict:', data)
        try:
            self.type.setCurrentText(data['type'])
        except KeyError:
            pass
        self.change_type()
        self.reload_fields()


    def to_dict(self):
        # print('to_dict:', self.get_fields())
        return {
            'type': self.type.currentText(),
            'fields': self.get_fields(),
        }

    def get_fields(self):
        values = []
        # for f in self.fields:
        #     if f.isVisible():
        #         values.append(f.currentText())
        return values

    def run(self):
        payload = requests[self.type.currentText()].payload(*self.get_fields())

        Sandbox().obs.send(payload)