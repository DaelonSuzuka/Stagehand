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
        send({"request-type": 'GetCurrentScene'}, cb)

    def set_scene(self, scene_name, cb=None):
        send({"request-type":"SetCurrentScene","scene-name":scene_name}, cb)

    def get_version(self, cb=None):
        send({"request-type": 'GetVersion'}, cb)

    def toggle_mute(self, source_name, cb=None):
        send({"request-type": 'ToggleMute', 'source': source_name}, cb)

    def mute(self, source_name, cb=None):
        send({"request-type": 'SetMute', 'source': source_name, 'mute': True}, cb)

    def unmute(self, source_name, cb=None):
        send({"request-type": 'SetMute', 'source': source_name, 'mute': False}, cb)

    def send(self, payload, cb=None):
        send(payload, cb)

    def get_filters(self, source_name, cb=None):
        payload = {
            "request-type": 'GetSourceFilters',
            'sourceName': source_name,
        }
        send(payload, cb)

    def enable_filter(self, source_name, filter_name, cb=None):
        send({
            "request-type": 'SetSourceFilterVisibility',
            'sourceName': source_name,
            'filterName': filter_name,
            'filterEnabled': True
        }, cb)

    def disable_filter(self, source_name, filter_name, cb=None):
        send({
            "request-type": 'SetSourceFilterVisibility',
            'sourceName': source_name,
            'filterName': filter_name,
            'filterEnabled': False
        }, cb)