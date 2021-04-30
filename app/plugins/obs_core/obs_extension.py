from qtstrap import *
from stagehand.sandbox import Sandbox


# helper function
def send(payload, cb=None):
    Sandbox().obs.send(payload, cb)


class ObsExtension:
    def get_source_list(self, cb=None):
        send({"request-type": 'GetSourcesList'}, cb)

    def get_scene_list(self, cb=None):
        send({"request-type": 'GetSceneList'}, cb)

    def get_scene(self, cb=None):
        send(payload, cb)

    def set_scene(self, scene_name, cb=None):
        send({"request-type":"SetCurrentScene","scene-name":scene_name}, cb)

    def get_version(self, cb=None):
        send({"request-type": 'GetVersion'}, cb)

    def send(self, payload, cb=None):
        send(payload, cb)
