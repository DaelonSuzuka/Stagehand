from qtstrap import *
from stagehand.sandbox import Sandbox


class ObsExtension:
    def set_scene(self, name):
        Sandbox().obs.send(requests.SetScene(name))

    def send(self, payload, cb=None):
        Sandbox().obs.send(payload, cb)
