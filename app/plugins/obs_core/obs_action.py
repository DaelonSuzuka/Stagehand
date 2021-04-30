from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.actions import ActionStackItem


class ObsActionWidget(QWidget, ActionStackItem):
    def __init__(self, changed):
        super().__init__()

        self.type = QComboBox()
        self.type.addItems(['set scene', 'mute', 'unmute'])
        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.load_values)
        
        self.value = QComboBox()
        self.value.currentIndexChanged.connect(changed)
        
        self.load_values()

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.value)

    def load_values(self, value=None):
        self.value.clear()
        if self.type.currentText() == 'set scene':
            def cb(msg):
                scenes = [s['name'] for s in msg['scenes']]
                self.value.clear()
                self.value.addItems(scenes)
                if value in scenes:
                    self.value.setCurrentText(value)

            Sandbox().obs.send(requests.GetSceneList(), cb)

    def from_dict(self, data):
        try:
            self.type.setCurrentText(data['type'])
            self.value.setCurrentText(data['value'])
            self.load_values(data['value'])
        except:
            pass

    def to_dict(self):
        return {
            'type': self.type.currentText(),
            'value': self.value.currentText(),
        }

    def run(self):
        if self.type.currentText() == 'set scene':
            Sandbox().obs.send(requests.SetScene(self.value.currentText()))