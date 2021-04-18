from qtstrap import *
from . import requests


class SandboxTools(QWidget):
    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = obs

        self.scenes = QListWidget()
        self.scenes.currentTextChanged.connect(self.set_scene)
        self.refresh_scenes = QPushButton('Refresh')
        self.sources = QListWidget()
        self.refresh_sources = QPushButton('Refresh')
        self.output = QTextEdit(readOnly=True)
        self.clear_output = QPushButton('Clear', clicked=self.output.clear)

        with CHBoxLayout(self) as layout:
            with layout.hbox() as layout:
                with layout.vbox() as layout:
                    with layout.hbox(margins=(0,0,0,0)) as layout:
                        layout.add(QLabel('Scenes:'))
                        layout.add(QLabel(), 1)
                        layout.add(self.refresh_scenes)
                    layout.add(self.scenes)
                with layout.vbox() as layout:
                    with layout.hbox(margins=(0,0,0,0)) as layout:
                        layout.add(QLabel('Sources:'))
                        layout.add(QLabel(), 1)
                        layout.add(self.refresh_sources)
                    layout.add(self.sources)
            with layout.vbox() as layout:
                with layout.hbox(margins=(0,0,0,0)) as layout:
                    layout.add(QLabel('Output:'))
                    layout.add(QLabel(), 1)
                    layout.add(self.clear_output)
                layout.add(self.output)

        def get_scenes():
            self.obs.send(requests.GetSceneList(), self.update_scenes)

        self.obs.socket_connected.connect(self.on_connect)
        self.obs.message_received.connect(self.obs_message_recieved)

        self.refresh_scenes.clicked.connect(lambda: get_scenes())
    
    def on_connect(self):
        self.obs.send(requests.GetSceneList(), self.update_scenes)
        self.obs.send(requests.GetSourcesList(), self.update_sources)

    def set_scene(self, name):
        self.obs.send(requests.SetScene(name))

    def update_selected_scene(self, name):
        self.scenes.clearSelection()
        for i in range(self.scenes.count()):
            if self.scenes.item(i).text() == name:
                self.scenes.setItemSelected(self.scenes.item(i), True)

    def update_scenes(self, msg):
        self.scenes.clear()
        self.scenes.addItems([s['name'] for s in msg['scenes']])
        # print(msg.keys())

    def update_sources(self, msg):
        self.sources.clear()
        self.sources.addItems([s['name'] for s in msg['sources']])
        # print(msg['sources'])

    def obs_message_recieved(self, msg):
        if 'update-type' in msg:
            if msg['update-type'] == 'SwitchScenes':
                self.update_selected_scene(msg['scene-name'])
                self.update_sources(msg)
                # self.obs.send(requests.GetSourcesList(), self.update_sources)
