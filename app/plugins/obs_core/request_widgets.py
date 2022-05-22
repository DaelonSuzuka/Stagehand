from .base_classes import *
from qtstrap import *
from stagehand.sandbox import Sandbox


class GetVersionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetVersion'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetAuthRequiredWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetAuthRequired'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class AuthenticateWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.auth = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.auth)

    def payload(self):
        payload = {}
        payload['request-type'] = 'Authenticate'
        payload['auth'] = self.auth.get_data()
        return payload

    def refresh(self):
        self.auth.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.auth.set_data(data['auth']) 

    def get_data(self):
        return {
            'auth': self.auth.get_data(),
        }


class SetHeartbeatWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.enable = BoolSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.enable)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetHeartbeat'
        payload['enable'] = self.enable.get_data()
        return payload

    def refresh(self):
        self.enable.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.enable.set_data(data['enable']) 

    def get_data(self):
        return {
            'enable': self.enable.get_data(),
        }


class SetFilenameFormattingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.filename_formatting = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.filename_formatting)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetFilenameFormatting'
        payload['filename-formatting'] = self.filename_formatting.get_data()
        return payload

    def refresh(self):
        self.filename_formatting.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.filename_formatting.set_data(data['filename_formatting']) 

    def get_data(self):
        return {
            'filename_formatting': self.filename_formatting.get_data(),
        }


class GetFilenameFormattingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetFilenameFormatting'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetStatsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetStats'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class BroadcastCustomMessageWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.realm = UnimplementedField('[field not implemented]')
        self.data = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.realm)
            layout.add(self.data)

    def payload(self):
        payload = {}
        payload['request-type'] = 'BroadcastCustomMessage'
        payload['realm'] = self.realm.get_data()
        payload['data'] = self.data.get_data()
        return payload

    def refresh(self):
        self.realm.refresh()
        self.data.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.realm.set_data(data['realm']) 
        self.data.set_data(data['data']) 

    def get_data(self):
        return {
            'realm': self.realm.get_data(),
            'data': self.data.get_data(),
        }


class GetVideoInfoWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetVideoInfo'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class OpenProjectorWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.type = UnimplementedField('[field not implemented]')
        self.monitor = UnimplementedField('[field not implemented]')
        self.geometry = UnimplementedField('[field not implemented]')
        self.name = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.monitor)
            layout.add(self.geometry)
            layout.add(self.name)

    def payload(self):
        payload = {}
        payload['request-type'] = 'OpenProjector'
        payload['type'] = self.type.get_data()
        payload['monitor'] = self.monitor.get_data()
        payload['geometry'] = self.geometry.get_data()
        payload['name'] = self.name.get_data()
        return payload

    def refresh(self):
        self.type.refresh()
        self.monitor.refresh()
        self.geometry.refresh()
        self.name.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.type.set_data(data['type']) 
        self.monitor.set_data(data['monitor']) 
        self.geometry.set_data(data['geometry']) 
        self.name.set_data(data['name']) 

    def get_data(self):
        return {
            'type': self.type.get_data(),
            'monitor': self.monitor.get_data(),
            'geometry': self.geometry.get_data(),
            'name': self.name.get_data(),
        }


class TriggerHotkeyByNameWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.hotkeyName = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.hotkeyName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyByName'
        payload['hotkeyName'] = self.hotkeyName.get_data()
        return payload

    def refresh(self):
        self.hotkeyName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.hotkeyName.set_data(data['hotkeyName']) 

    def get_data(self):
        return {
            'hotkeyName': self.hotkeyName.get_data(),
        }


class TriggerHotkeyBySequenceWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.keyId = UnimplementedField('[field not implemented]')
        self.keyModifiers = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.keyId)
            layout.add(self.keyModifiers)

    def payload(self):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyBySequence'
        payload['keyId'] = self.keyId.get_data()
        payload['keyModifiers'] = self.keyModifiers.get_data()
        return payload

    def refresh(self):
        self.keyId.refresh()
        self.keyModifiers.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.keyId.set_data(data['keyId']) 
        self.keyModifiers.set_data(data['keyModifiers']) 

    def get_data(self):
        return {
            'keyId': self.keyId.get_data(),
            'keyModifiers': self.keyModifiers.get_data(),
        }


class ExecuteBatchWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.requests = UnimplementedField('[field not implemented]')
        self.abortOnFail = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.requests)
            layout.add(self.abortOnFail)

    def payload(self):
        payload = {}
        payload['request-type'] = 'ExecuteBatch'
        payload['requests'] = self.requests.get_data()
        payload['abortOnFail'] = self.abortOnFail.get_data()
        return payload

    def refresh(self):
        self.requests.refresh()
        self.abortOnFail.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.requests.set_data(data['requests']) 
        self.abortOnFail.set_data(data['abortOnFail']) 

    def get_data(self):
        return {
            'requests': self.requests.get_data(),
            'abortOnFail': self.abortOnFail.get_data(),
        }


class SleepWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sleepMillis = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sleepMillis)

    def payload(self):
        payload = {}
        payload['request-type'] = 'Sleep'
        payload['sleepMillis'] = self.sleepMillis.get_data()
        return payload

    def refresh(self):
        self.sleepMillis.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sleepMillis.set_data(data['sleepMillis']) 

    def get_data(self):
        return {
            'sleepMillis': self.sleepMillis.get_data(),
        }


class PlayPauseMediaWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.playPause = BoolSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.playPause)

    def payload(self):
        payload = {}
        payload['request-type'] = 'PlayPauseMedia'
        payload['sourceName'] = self.sourceName.get_data()
        payload['playPause'] = self.playPause.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.playPause.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.playPause.set_data(data['playPause']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'playPause': self.playPause.get_data(),
        }


class RestartMediaWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'RestartMedia'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class StopMediaWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'StopMedia'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class NextMediaWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'NextMedia'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class PreviousMediaWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'PreviousMedia'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class GetMediaDurationWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetMediaDuration'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class GetMediaTimeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetMediaTime'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class SetMediaTimeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.timestamp = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.timestamp)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetMediaTime'
        payload['sourceName'] = self.sourceName.get_data()
        payload['timestamp'] = self.timestamp.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.timestamp.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.timestamp.set_data(data['timestamp']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'timestamp': self.timestamp.get_data(),
        }


class ScrubMediaWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.timeOffset = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.timeOffset)

    def payload(self):
        payload = {}
        payload['request-type'] = 'ScrubMedia'
        payload['sourceName'] = self.sourceName.get_data()
        payload['timeOffset'] = self.timeOffset.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.timeOffset.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.timeOffset.set_data(data['timeOffset']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'timeOffset': self.timeOffset.get_data(),
        }


class GetMediaStateWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetMediaState'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class GetMediaSourcesListWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetMediaSourcesList'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class CreateSourceWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.sourceKind = UnimplementedField('[field not implemented]')
        self.sceneName = SceneSelector(changed, parent=self)
        self.sourceSettings = UnimplementedField('[field not implemented]')
        self.setVisible = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.sourceKind)
            layout.add(self.sceneName)
            layout.add(self.sourceSettings)
            layout.add(self.setVisible)

    def payload(self):
        payload = {}
        payload['request-type'] = 'CreateSource'
        payload['sourceName'] = self.sourceName.get_data()
        payload['sourceKind'] = self.sourceKind.get_data()
        payload['sceneName'] = self.sceneName.get_data()
        payload['sourceSettings'] = self.sourceSettings.get_data()
        payload['setVisible'] = self.setVisible.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.sourceKind.refresh()
        self.sceneName.refresh()
        self.sourceSettings.refresh()
        self.setVisible.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.sourceKind.set_data(data['sourceKind']) 
        self.sceneName.set_data(data['sceneName']) 
        self.sourceSettings.set_data(data['sourceSettings']) 
        self.setVisible.set_data(data['setVisible']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'sourceKind': self.sourceKind.get_data(),
            'sceneName': self.sceneName.get_data(),
            'sourceSettings': self.sourceSettings.get_data(),
            'setVisible': self.setVisible.get_data(),
        }


class GetSourcesListWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSourcesList'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetSourceTypesListWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSourceTypesList'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetVolumeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)
        self.useDecibel = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)
            layout.add(self.useDecibel)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetVolume'
        payload['source'] = self.source.get_data()
        payload['useDecibel'] = self.useDecibel.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        self.useDecibel.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 
        self.useDecibel.set_data(data['useDecibel']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
            'useDecibel': self.useDecibel.get_data(),
        }


class SetVolumeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)
        self.volume = UnimplementedField('[field not implemented]')
        self.useDecibel = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)
            layout.add(self.volume)
            layout.add(self.useDecibel)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetVolume'
        payload['source'] = self.source.get_data()
        payload['volume'] = self.volume.get_data()
        payload['useDecibel'] = self.useDecibel.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        self.volume.refresh()
        self.useDecibel.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 
        self.volume.set_data(data['volume']) 
        self.useDecibel.set_data(data['useDecibel']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
            'volume': self.volume.get_data(),
            'useDecibel': self.useDecibel.get_data(),
        }


class SetAudioTracksWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.track = UnimplementedField('[field not implemented]')
        self.active = BoolSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.track)
            layout.add(self.active)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetAudioTracks'
        payload['sourceName'] = self.sourceName.get_data()
        payload['track'] = self.track.get_data()
        payload['active'] = self.active.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.track.refresh()
        self.active.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.track.set_data(data['track']) 
        self.active.set_data(data['active']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'track': self.track.get_data(),
            'active': self.active.get_data(),
        }


class GetAudioTracksWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetAudioTracks'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class GetMuteWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetMute'
        payload['source'] = self.source.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
        }


class SetMuteWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)
        self.mute = BoolSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)
            layout.add(self.mute)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetMute'
        payload['source'] = self.source.get_data()
        payload['mute'] = self.mute.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        self.mute.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 
        self.mute.set_data(data['mute']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
            'mute': self.mute.get_data(),
        }


class ToggleMuteWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)

    def payload(self):
        payload = {}
        payload['request-type'] = 'ToggleMute'
        payload['source'] = self.source.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
        }


class GetSourceActiveWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSourceActive'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class GetAudioActiveWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetAudioActive'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class SetSourceNameWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.newName = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.newName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSourceName'
        payload['sourceName'] = self.sourceName.get_data()
        payload['newName'] = self.newName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.newName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.newName.set_data(data['newName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'newName': self.newName.get_data(),
        }


class SetSyncOffsetWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)
        self.offset = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)
            layout.add(self.offset)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSyncOffset'
        payload['source'] = self.source.get_data()
        payload['offset'] = self.offset.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        self.offset.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 
        self.offset.set_data(data['offset']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
            'offset': self.offset.get_data(),
        }


class GetSyncOffsetWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSyncOffset'
        payload['source'] = self.source.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
        }


class GetSourceSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.sourceType = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.sourceType)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSourceSettings'
        payload['sourceName'] = self.sourceName.get_data()
        payload['sourceType'] = self.sourceType.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.sourceType.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.sourceType.set_data(data['sourceType']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'sourceType': self.sourceType.get_data(),
        }


class SetSourceSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.sourceType = UnimplementedField('[field not implemented]')
        self.sourceSettings = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.sourceType)
            layout.add(self.sourceSettings)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSourceSettings'
        payload['sourceName'] = self.sourceName.get_data()
        payload['sourceType'] = self.sourceType.get_data()
        payload['sourceSettings'] = self.sourceSettings.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.sourceType.refresh()
        self.sourceSettings.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.sourceType.set_data(data['sourceType']) 
        self.sourceSettings.set_data(data['sourceSettings']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'sourceType': self.sourceType.get_data(),
            'sourceSettings': self.sourceSettings.get_data(),
        }


class GetTextGDIPlusPropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetTextGDIPlusProperties'
        payload['source'] = self.source.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
        }


class SetTextGDIPlusPropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)
        self.align = UnimplementedField('[field not implemented]')
        self.bk_color = UnimplementedField('[field not implemented]')
        self.bk_opacity = UnimplementedField('[field not implemented]')
        self.chatlog = UnimplementedField('[field not implemented]')
        self.chatlog_lines = UnimplementedField('[field not implemented]')
        self.color = UnimplementedField('[field not implemented]')
        self.extents = UnimplementedField('[field not implemented]')
        self.extents_cx = UnimplementedField('[field not implemented]')
        self.extents_cy = UnimplementedField('[field not implemented]')
        self.file = UnimplementedField('[field not implemented]')
        self.read_from_file = UnimplementedField('[field not implemented]')
        self.font = UnimplementedField('[field not implemented]')
        self.gradient = UnimplementedField('[field not implemented]')
        self.gradient_color = UnimplementedField('[field not implemented]')
        self.gradient_dir = UnimplementedField('[field not implemented]')
        self.gradient_opacity = UnimplementedField('[field not implemented]')
        self.outline = UnimplementedField('[field not implemented]')
        self.outline_color = UnimplementedField('[field not implemented]')
        self.outline_size = UnimplementedField('[field not implemented]')
        self.outline_opacity = UnimplementedField('[field not implemented]')
        self.text = UnimplementedField('[field not implemented]')
        self.valign = UnimplementedField('[field not implemented]')
        self.vertical = UnimplementedField('[field not implemented]')
        self.render = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)
            layout.add(self.align)
            layout.add(self.bk_color)
            layout.add(self.bk_opacity)
            layout.add(self.chatlog)
            layout.add(self.chatlog_lines)
            layout.add(self.color)
            layout.add(self.extents)
            layout.add(self.extents_cx)
            layout.add(self.extents_cy)
            layout.add(self.file)
            layout.add(self.read_from_file)
            layout.add(self.font)
            layout.add(self.gradient)
            layout.add(self.gradient_color)
            layout.add(self.gradient_dir)
            layout.add(self.gradient_opacity)
            layout.add(self.outline)
            layout.add(self.outline_color)
            layout.add(self.outline_size)
            layout.add(self.outline_opacity)
            layout.add(self.text)
            layout.add(self.valign)
            layout.add(self.vertical)
            layout.add(self.render)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetTextGDIPlusProperties'
        payload['source'] = self.source.get_data()
        payload['align'] = self.align.get_data()
        payload['bk_color'] = self.bk_color.get_data()
        payload['bk_opacity'] = self.bk_opacity.get_data()
        payload['chatlog'] = self.chatlog.get_data()
        payload['chatlog_lines'] = self.chatlog_lines.get_data()
        payload['color'] = self.color.get_data()
        payload['extents'] = self.extents.get_data()
        payload['extents_cx'] = self.extents_cx.get_data()
        payload['extents_cy'] = self.extents_cy.get_data()
        payload['file'] = self.file.get_data()
        payload['read_from_file'] = self.read_from_file.get_data()
        payload['font'] = self.font.get_data()
        payload['gradient'] = self.gradient.get_data()
        payload['gradient_color'] = self.gradient_color.get_data()
        payload['gradient_dir'] = self.gradient_dir.get_data()
        payload['gradient_opacity'] = self.gradient_opacity.get_data()
        payload['outline'] = self.outline.get_data()
        payload['outline_color'] = self.outline_color.get_data()
        payload['outline_size'] = self.outline_size.get_data()
        payload['outline_opacity'] = self.outline_opacity.get_data()
        payload['text'] = self.text.get_data()
        payload['valign'] = self.valign.get_data()
        payload['vertical'] = self.vertical.get_data()
        payload['render'] = self.render.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        self.align.refresh()
        self.bk_color.refresh()
        self.bk_opacity.refresh()
        self.chatlog.refresh()
        self.chatlog_lines.refresh()
        self.color.refresh()
        self.extents.refresh()
        self.extents_cx.refresh()
        self.extents_cy.refresh()
        self.file.refresh()
        self.read_from_file.refresh()
        self.font.refresh()
        self.gradient.refresh()
        self.gradient_color.refresh()
        self.gradient_dir.refresh()
        self.gradient_opacity.refresh()
        self.outline.refresh()
        self.outline_color.refresh()
        self.outline_size.refresh()
        self.outline_opacity.refresh()
        self.text.refresh()
        self.valign.refresh()
        self.vertical.refresh()
        self.render.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 
        self.align.set_data(data['align']) 
        self.bk_color.set_data(data['bk_color']) 
        self.bk_opacity.set_data(data['bk_opacity']) 
        self.chatlog.set_data(data['chatlog']) 
        self.chatlog_lines.set_data(data['chatlog_lines']) 
        self.color.set_data(data['color']) 
        self.extents.set_data(data['extents']) 
        self.extents_cx.set_data(data['extents_cx']) 
        self.extents_cy.set_data(data['extents_cy']) 
        self.file.set_data(data['file']) 
        self.read_from_file.set_data(data['read_from_file']) 
        self.font.set_data(data['font']) 
        self.gradient.set_data(data['gradient']) 
        self.gradient_color.set_data(data['gradient_color']) 
        self.gradient_dir.set_data(data['gradient_dir']) 
        self.gradient_opacity.set_data(data['gradient_opacity']) 
        self.outline.set_data(data['outline']) 
        self.outline_color.set_data(data['outline_color']) 
        self.outline_size.set_data(data['outline_size']) 
        self.outline_opacity.set_data(data['outline_opacity']) 
        self.text.set_data(data['text']) 
        self.valign.set_data(data['valign']) 
        self.vertical.set_data(data['vertical']) 
        self.render.set_data(data['render']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
            'align': self.align.get_data(),
            'bk_color': self.bk_color.get_data(),
            'bk_opacity': self.bk_opacity.get_data(),
            'chatlog': self.chatlog.get_data(),
            'chatlog_lines': self.chatlog_lines.get_data(),
            'color': self.color.get_data(),
            'extents': self.extents.get_data(),
            'extents_cx': self.extents_cx.get_data(),
            'extents_cy': self.extents_cy.get_data(),
            'file': self.file.get_data(),
            'read_from_file': self.read_from_file.get_data(),
            'font': self.font.get_data(),
            'gradient': self.gradient.get_data(),
            'gradient_color': self.gradient_color.get_data(),
            'gradient_dir': self.gradient_dir.get_data(),
            'gradient_opacity': self.gradient_opacity.get_data(),
            'outline': self.outline.get_data(),
            'outline_color': self.outline_color.get_data(),
            'outline_size': self.outline_size.get_data(),
            'outline_opacity': self.outline_opacity.get_data(),
            'text': self.text.get_data(),
            'valign': self.valign.get_data(),
            'vertical': self.vertical.get_data(),
            'render': self.render.get_data(),
        }


class GetTextFreetype2PropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetTextFreetype2Properties'
        payload['source'] = self.source.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
        }


class SetTextFreetype2PropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)
        self.color1 = UnimplementedField('[field not implemented]')
        self.color2 = UnimplementedField('[field not implemented]')
        self.custom_width = UnimplementedField('[field not implemented]')
        self.drop_shadow = UnimplementedField('[field not implemented]')
        self.font = UnimplementedField('[field not implemented]')
        self.from_file = UnimplementedField('[field not implemented]')
        self.log_mode = UnimplementedField('[field not implemented]')
        self.outline = UnimplementedField('[field not implemented]')
        self.text = UnimplementedField('[field not implemented]')
        self.text_file = UnimplementedField('[field not implemented]')
        self.word_wrap = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)
            layout.add(self.color1)
            layout.add(self.color2)
            layout.add(self.custom_width)
            layout.add(self.drop_shadow)
            layout.add(self.font)
            layout.add(self.from_file)
            layout.add(self.log_mode)
            layout.add(self.outline)
            layout.add(self.text)
            layout.add(self.text_file)
            layout.add(self.word_wrap)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetTextFreetype2Properties'
        payload['source'] = self.source.get_data()
        payload['color1'] = self.color1.get_data()
        payload['color2'] = self.color2.get_data()
        payload['custom_width'] = self.custom_width.get_data()
        payload['drop_shadow'] = self.drop_shadow.get_data()
        payload['font'] = self.font.get_data()
        payload['from_file'] = self.from_file.get_data()
        payload['log_mode'] = self.log_mode.get_data()
        payload['outline'] = self.outline.get_data()
        payload['text'] = self.text.get_data()
        payload['text_file'] = self.text_file.get_data()
        payload['word_wrap'] = self.word_wrap.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        self.color1.refresh()
        self.color2.refresh()
        self.custom_width.refresh()
        self.drop_shadow.refresh()
        self.font.refresh()
        self.from_file.refresh()
        self.log_mode.refresh()
        self.outline.refresh()
        self.text.refresh()
        self.text_file.refresh()
        self.word_wrap.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 
        self.color1.set_data(data['color1']) 
        self.color2.set_data(data['color2']) 
        self.custom_width.set_data(data['custom_width']) 
        self.drop_shadow.set_data(data['drop_shadow']) 
        self.font.set_data(data['font']) 
        self.from_file.set_data(data['from_file']) 
        self.log_mode.set_data(data['log_mode']) 
        self.outline.set_data(data['outline']) 
        self.text.set_data(data['text']) 
        self.text_file.set_data(data['text_file']) 
        self.word_wrap.set_data(data['word_wrap']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
            'color1': self.color1.get_data(),
            'color2': self.color2.get_data(),
            'custom_width': self.custom_width.get_data(),
            'drop_shadow': self.drop_shadow.get_data(),
            'font': self.font.get_data(),
            'from_file': self.from_file.get_data(),
            'log_mode': self.log_mode.get_data(),
            'outline': self.outline.get_data(),
            'text': self.text.get_data(),
            'text_file': self.text_file.get_data(),
            'word_wrap': self.word_wrap.get_data(),
        }


class GetBrowserSourcePropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetBrowserSourceProperties'
        payload['source'] = self.source.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
        }


class SetBrowserSourcePropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.source = SourceSelector(changed, parent=self)
        self.is_local_file = UnimplementedField('[field not implemented]')
        self.local_file = UnimplementedField('[field not implemented]')
        self.url = UnimplementedField('[field not implemented]')
        self.css = UnimplementedField('[field not implemented]')
        self.width = UnimplementedField('[field not implemented]')
        self.height = UnimplementedField('[field not implemented]')
        self.fps = UnimplementedField('[field not implemented]')
        self.shutdown = UnimplementedField('[field not implemented]')
        self.render = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.source)
            layout.add(self.is_local_file)
            layout.add(self.local_file)
            layout.add(self.url)
            layout.add(self.css)
            layout.add(self.width)
            layout.add(self.height)
            layout.add(self.fps)
            layout.add(self.shutdown)
            layout.add(self.render)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetBrowserSourceProperties'
        payload['source'] = self.source.get_data()
        payload['is_local_file'] = self.is_local_file.get_data()
        payload['local_file'] = self.local_file.get_data()
        payload['url'] = self.url.get_data()
        payload['css'] = self.css.get_data()
        payload['width'] = self.width.get_data()
        payload['height'] = self.height.get_data()
        payload['fps'] = self.fps.get_data()
        payload['shutdown'] = self.shutdown.get_data()
        payload['render'] = self.render.get_data()
        return payload

    def refresh(self):
        self.source.refresh()
        self.is_local_file.refresh()
        self.local_file.refresh()
        self.url.refresh()
        self.css.refresh()
        self.width.refresh()
        self.height.refresh()
        self.fps.refresh()
        self.shutdown.refresh()
        self.render.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.source.set_data(data['source']) 
        self.is_local_file.set_data(data['is_local_file']) 
        self.local_file.set_data(data['local_file']) 
        self.url.set_data(data['url']) 
        self.css.set_data(data['css']) 
        self.width.set_data(data['width']) 
        self.height.set_data(data['height']) 
        self.fps.set_data(data['fps']) 
        self.shutdown.set_data(data['shutdown']) 
        self.render.set_data(data['render']) 

    def get_data(self):
        return {
            'source': self.source.get_data(),
            'is_local_file': self.is_local_file.get_data(),
            'local_file': self.local_file.get_data(),
            'url': self.url.get_data(),
            'css': self.css.get_data(),
            'width': self.width.get_data(),
            'height': self.height.get_data(),
            'fps': self.fps.get_data(),
            'shutdown': self.shutdown.get_data(),
            'render': self.render.get_data(),
        }


class GetSpecialSourcesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSpecialSources'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetSourceFiltersWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSourceFilters'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class GetSourceFilterInfoWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.filterName = FilterSelector(changed, self.sourceName, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.filterName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSourceFilterInfo'
        payload['sourceName'] = self.sourceName.get_data()
        payload['filterName'] = self.filterName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.filterName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.filterName.set_data(data['filterName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'filterName': self.filterName.get_data(),
        }


class AddFilterToSourceWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.filterName = FilterSelector(changed, self.sourceName, parent=self)
        self.filterType = UnimplementedField('[field not implemented]')
        self.filterSettings = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.filterName)
            layout.add(self.filterType)
            layout.add(self.filterSettings)

    def payload(self):
        payload = {}
        payload['request-type'] = 'AddFilterToSource'
        payload['sourceName'] = self.sourceName.get_data()
        payload['filterName'] = self.filterName.get_data()
        payload['filterType'] = self.filterType.get_data()
        payload['filterSettings'] = self.filterSettings.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.filterName.refresh()
        self.filterType.refresh()
        self.filterSettings.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.filterName.set_data(data['filterName']) 
        self.filterType.set_data(data['filterType']) 
        self.filterSettings.set_data(data['filterSettings']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'filterName': self.filterName.get_data(),
            'filterType': self.filterType.get_data(),
            'filterSettings': self.filterSettings.get_data(),
        }


class RemoveFilterFromSourceWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.filterName = FilterSelector(changed, self.sourceName, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.filterName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'RemoveFilterFromSource'
        payload['sourceName'] = self.sourceName.get_data()
        payload['filterName'] = self.filterName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.filterName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.filterName.set_data(data['filterName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'filterName': self.filterName.get_data(),
        }


class ReorderSourceFilterWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.filterName = FilterSelector(changed, self.sourceName, parent=self)
        self.newIndex = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.filterName)
            layout.add(self.newIndex)

    def payload(self):
        payload = {}
        payload['request-type'] = 'ReorderSourceFilter'
        payload['sourceName'] = self.sourceName.get_data()
        payload['filterName'] = self.filterName.get_data()
        payload['newIndex'] = self.newIndex.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.filterName.refresh()
        self.newIndex.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.filterName.set_data(data['filterName']) 
        self.newIndex.set_data(data['newIndex']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'filterName': self.filterName.get_data(),
            'newIndex': self.newIndex.get_data(),
        }


class MoveSourceFilterWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.filterName = FilterSelector(changed, self.sourceName, parent=self)
        self.movementType = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.filterName)
            layout.add(self.movementType)

    def payload(self):
        payload = {}
        payload['request-type'] = 'MoveSourceFilter'
        payload['sourceName'] = self.sourceName.get_data()
        payload['filterName'] = self.filterName.get_data()
        payload['movementType'] = self.movementType.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.filterName.refresh()
        self.movementType.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.filterName.set_data(data['filterName']) 
        self.movementType.set_data(data['movementType']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'filterName': self.filterName.get_data(),
            'movementType': self.movementType.get_data(),
        }


class SetSourceFilterSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.filterName = FilterSelector(changed, self.sourceName, parent=self)
        self.filterSettings = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.filterName)
            layout.add(self.filterSettings)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSourceFilterSettings'
        payload['sourceName'] = self.sourceName.get_data()
        payload['filterName'] = self.filterName.get_data()
        payload['filterSettings'] = self.filterSettings.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.filterName.refresh()
        self.filterSettings.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.filterName.set_data(data['filterName']) 
        self.filterSettings.set_data(data['filterSettings']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'filterName': self.filterName.get_data(),
            'filterSettings': self.filterSettings.get_data(),
        }


class SetSourceFilterVisibilityWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.filterName = FilterSelector(changed, self.sourceName, parent=self)
        self.filterEnabled = BoolSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.filterName)
            layout.add(self.filterEnabled)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSourceFilterVisibility'
        payload['sourceName'] = self.sourceName.get_data()
        payload['filterName'] = self.filterName.get_data()
        payload['filterEnabled'] = self.filterEnabled.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.filterName.refresh()
        self.filterEnabled.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.filterName.set_data(data['filterName']) 
        self.filterEnabled.set_data(data['filterEnabled']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'filterName': self.filterName.get_data(),
            'filterEnabled': self.filterEnabled.get_data(),
        }


class GetAudioMonitorTypeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetAudioMonitorType'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class SetAudioMonitorTypeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.monitorType = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.monitorType)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetAudioMonitorType'
        payload['sourceName'] = self.sourceName.get_data()
        payload['monitorType'] = self.monitorType.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.monitorType.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.monitorType.set_data(data['monitorType']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'monitorType': self.monitorType.get_data(),
        }


class GetSourceDefaultSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceKind = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceKind)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSourceDefaultSettings'
        payload['sourceKind'] = self.sourceKind.get_data()
        return payload

    def refresh(self):
        self.sourceKind.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceKind.set_data(data['sourceKind']) 

    def get_data(self):
        return {
            'sourceKind': self.sourceKind.get_data(),
        }


class TakeSourceScreenshotWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)
        self.embedPictureFormat = UnimplementedField('[field not implemented]')
        self.saveToFilePath = UnimplementedField('[field not implemented]')
        self.fileFormat = UnimplementedField('[field not implemented]')
        self.compressionQuality = UnimplementedField('[field not implemented]')
        self.width = UnimplementedField('[field not implemented]')
        self.height = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)
            layout.add(self.embedPictureFormat)
            layout.add(self.saveToFilePath)
            layout.add(self.fileFormat)
            layout.add(self.compressionQuality)
            layout.add(self.width)
            layout.add(self.height)

    def payload(self):
        payload = {}
        payload['request-type'] = 'TakeSourceScreenshot'
        payload['sourceName'] = self.sourceName.get_data()
        payload['embedPictureFormat'] = self.embedPictureFormat.get_data()
        payload['saveToFilePath'] = self.saveToFilePath.get_data()
        payload['fileFormat'] = self.fileFormat.get_data()
        payload['compressionQuality'] = self.compressionQuality.get_data()
        payload['width'] = self.width.get_data()
        payload['height'] = self.height.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        self.embedPictureFormat.refresh()
        self.saveToFilePath.refresh()
        self.fileFormat.refresh()
        self.compressionQuality.refresh()
        self.width.refresh()
        self.height.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 
        self.embedPictureFormat.set_data(data['embedPictureFormat']) 
        self.saveToFilePath.set_data(data['saveToFilePath']) 
        self.fileFormat.set_data(data['fileFormat']) 
        self.compressionQuality.set_data(data['compressionQuality']) 
        self.width.set_data(data['width']) 
        self.height.set_data(data['height']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
            'embedPictureFormat': self.embedPictureFormat.get_data(),
            'saveToFilePath': self.saveToFilePath.get_data(),
            'fileFormat': self.fileFormat.get_data(),
            'compressionQuality': self.compressionQuality.get_data(),
            'width': self.width.get_data(),
            'height': self.height.get_data(),
        }


class RefreshBrowserSourceWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sourceName = SourceSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sourceName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'RefreshBrowserSource'
        payload['sourceName'] = self.sourceName.get_data()
        return payload

    def refresh(self):
        self.sourceName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sourceName.set_data(data['sourceName']) 

    def get_data(self):
        return {
            'sourceName': self.sourceName.get_data(),
        }


class ListOutputsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'ListOutputs'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetOutputInfoWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.outputName = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.outputName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetOutputInfo'
        payload['outputName'] = self.outputName.get_data()
        return payload

    def refresh(self):
        self.outputName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.outputName.set_data(data['outputName']) 

    def get_data(self):
        return {
            'outputName': self.outputName.get_data(),
        }


class StartOutputWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.outputName = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.outputName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartOutput'
        payload['outputName'] = self.outputName.get_data()
        return payload

    def refresh(self):
        self.outputName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.outputName.set_data(data['outputName']) 

    def get_data(self):
        return {
            'outputName': self.outputName.get_data(),
        }


class StopOutputWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.outputName = UnimplementedField('[field not implemented]')
        self.force = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.outputName)
            layout.add(self.force)

    def payload(self):
        payload = {}
        payload['request-type'] = 'StopOutput'
        payload['outputName'] = self.outputName.get_data()
        payload['force'] = self.force.get_data()
        return payload

    def refresh(self):
        self.outputName.refresh()
        self.force.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.outputName.set_data(data['outputName']) 
        self.force.set_data(data['force']) 

    def get_data(self):
        return {
            'outputName': self.outputName.get_data(),
            'force': self.force.get_data(),
        }


class SetCurrentProfileWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.profile_name = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.profile_name)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetCurrentProfile'
        payload['profile-name'] = self.profile_name.get_data()
        return payload

    def refresh(self):
        self.profile_name.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.profile_name.set_data(data['profile_name']) 

    def get_data(self):
        return {
            'profile_name': self.profile_name.get_data(),
        }


class GetCurrentProfileWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetCurrentProfile'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ListProfilesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'ListProfiles'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetRecordingStatusWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetRecordingStatus'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartStopRecordingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartStopRecording'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartRecordingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartRecording'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StopRecordingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StopRecording'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class PauseRecordingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'PauseRecording'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ResumeRecordingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'ResumeRecording'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SetRecordingFolderWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.rec_folder = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.rec_folder)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetRecordingFolder'
        payload['rec-folder'] = self.rec_folder.get_data()
        return payload

    def refresh(self):
        self.rec_folder.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.rec_folder.set_data(data['rec_folder']) 

    def get_data(self):
        return {
            'rec_folder': self.rec_folder.get_data(),
        }


class GetRecordingFolderWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetRecordingFolder'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetReplayBufferStatusWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetReplayBufferStatus'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartStopReplayBufferWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartStopReplayBuffer'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartReplayBufferWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartReplayBuffer'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StopReplayBufferWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StopReplayBuffer'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SaveReplayBufferWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'SaveReplayBuffer'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SetCurrentSceneCollectionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sc_name = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sc_name)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetCurrentSceneCollection'
        payload['sc-name'] = self.sc_name.get_data()
        return payload

    def refresh(self):
        self.sc_name.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sc_name.set_data(data['sc_name']) 

    def get_data(self):
        return {
            'sc_name': self.sc_name.get_data(),
        }


class GetCurrentSceneCollectionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetCurrentSceneCollection'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ListSceneCollectionsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'ListSceneCollections'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetSceneItemListWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sceneName = SceneSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sceneName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSceneItemList'
        payload['sceneName'] = self.sceneName.get_data()
        return payload

    def refresh(self):
        self.sceneName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sceneName.set_data(data['sceneName']) 

    def get_data(self):
        return {
            'sceneName': self.sceneName.get_data(),
        }


class GetSceneItemPropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)
        self.item = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)
            layout.add(self.item)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSceneItemProperties'
        payload['scene-name'] = self.scene_name.get_data()
        payload['item'] = self.item.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        self.item.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 
        self.item.set_data(data['item']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
            'item': self.item.get_data(),
        }


class SetSceneItemPropertiesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)
        self.item = UnimplementedField('[field not implemented]')
        self.position = UnimplementedField('[field not implemented]')
        self.rotation = UnimplementedField('[field not implemented]')
        self.scale = UnimplementedField('[field not implemented]')
        self.crop = UnimplementedField('[field not implemented]')
        self.visible = UnimplementedField('[field not implemented]')
        self.locked = UnimplementedField('[field not implemented]')
        self.bounds = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)
            layout.add(self.item)
            layout.add(self.position)
            layout.add(self.rotation)
            layout.add(self.scale)
            layout.add(self.crop)
            layout.add(self.visible)
            layout.add(self.locked)
            layout.add(self.bounds)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSceneItemProperties'
        payload['scene-name'] = self.scene_name.get_data()
        payload['item'] = self.item.get_data()
        payload['position'] = self.position.get_data()
        payload['rotation'] = self.rotation.get_data()
        payload['scale'] = self.scale.get_data()
        payload['crop'] = self.crop.get_data()
        payload['visible'] = self.visible.get_data()
        payload['locked'] = self.locked.get_data()
        payload['bounds'] = self.bounds.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        self.item.refresh()
        self.position.refresh()
        self.rotation.refresh()
        self.scale.refresh()
        self.crop.refresh()
        self.visible.refresh()
        self.locked.refresh()
        self.bounds.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 
        self.item.set_data(data['item']) 
        self.position.set_data(data['position']) 
        self.rotation.set_data(data['rotation']) 
        self.scale.set_data(data['scale']) 
        self.crop.set_data(data['crop']) 
        self.visible.set_data(data['visible']) 
        self.locked.set_data(data['locked']) 
        self.bounds.set_data(data['bounds']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
            'item': self.item.get_data(),
            'position': self.position.get_data(),
            'rotation': self.rotation.get_data(),
            'scale': self.scale.get_data(),
            'crop': self.crop.get_data(),
            'visible': self.visible.get_data(),
            'locked': self.locked.get_data(),
            'bounds': self.bounds.get_data(),
        }


class ResetSceneItemWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)
        self.item = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)
            layout.add(self.item)

    def payload(self):
        payload = {}
        payload['request-type'] = 'ResetSceneItem'
        payload['scene-name'] = self.scene_name.get_data()
        payload['item'] = self.item.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        self.item.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 
        self.item.set_data(data['item']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
            'item': self.item.get_data(),
        }


class SetSceneItemRenderWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)
        self.source = SourceSelector(changed, parent=self)
        self.item = UnimplementedField('[field not implemented]')
        self.render = BoolSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)
            layout.add(self.source)
            layout.add(self.item)
            layout.add(self.render)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSceneItemRender'
        payload['scene-name'] = self.scene_name.get_data()
        payload['source'] = self.source.get_data()
        payload['item'] = self.item.get_data()
        payload['render'] = self.render.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        self.source.refresh()
        self.item.refresh()
        self.render.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 
        self.source.set_data(data['source']) 
        self.item.set_data(data['item']) 
        self.render.set_data(data['render']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
            'source': self.source.get_data(),
            'item': self.item.get_data(),
            'render': self.render.get_data(),
        }


class SetSceneItemPositionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)
        self.item = UnimplementedField('[field not implemented]')
        self.x = UnimplementedField('[field not implemented]')
        self.y = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)
            layout.add(self.item)
            layout.add(self.x)
            layout.add(self.y)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSceneItemPosition'
        payload['scene-name'] = self.scene_name.get_data()
        payload['item'] = self.item.get_data()
        payload['x'] = self.x.get_data()
        payload['y'] = self.y.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        self.item.refresh()
        self.x.refresh()
        self.y.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 
        self.item.set_data(data['item']) 
        self.x.set_data(data['x']) 
        self.y.set_data(data['y']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
            'item': self.item.get_data(),
            'x': self.x.get_data(),
            'y': self.y.get_data(),
        }


class SetSceneItemTransformWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)
        self.item = UnimplementedField('[field not implemented]')
        self.x_scale = UnimplementedField('[field not implemented]')
        self.y_scale = UnimplementedField('[field not implemented]')
        self.rotation = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)
            layout.add(self.item)
            layout.add(self.x_scale)
            layout.add(self.y_scale)
            layout.add(self.rotation)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSceneItemTransform'
        payload['scene-name'] = self.scene_name.get_data()
        payload['item'] = self.item.get_data()
        payload['x-scale'] = self.x_scale.get_data()
        payload['y-scale'] = self.y_scale.get_data()
        payload['rotation'] = self.rotation.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        self.item.refresh()
        self.x_scale.refresh()
        self.y_scale.refresh()
        self.rotation.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 
        self.item.set_data(data['item']) 
        self.x_scale.set_data(data['x_scale']) 
        self.y_scale.set_data(data['y_scale']) 
        self.rotation.set_data(data['rotation']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
            'item': self.item.get_data(),
            'x_scale': self.x_scale.get_data(),
            'y_scale': self.y_scale.get_data(),
            'rotation': self.rotation.get_data(),
        }


class SetSceneItemCropWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)
        self.item = UnimplementedField('[field not implemented]')
        self.top = UnimplementedField('[field not implemented]')
        self.bottom = UnimplementedField('[field not implemented]')
        self.left = UnimplementedField('[field not implemented]')
        self.right = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)
            layout.add(self.item)
            layout.add(self.top)
            layout.add(self.bottom)
            layout.add(self.left)
            layout.add(self.right)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSceneItemCrop'
        payload['scene-name'] = self.scene_name.get_data()
        payload['item'] = self.item.get_data()
        payload['top'] = self.top.get_data()
        payload['bottom'] = self.bottom.get_data()
        payload['left'] = self.left.get_data()
        payload['right'] = self.right.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        self.item.refresh()
        self.top.refresh()
        self.bottom.refresh()
        self.left.refresh()
        self.right.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 
        self.item.set_data(data['item']) 
        self.top.set_data(data['top']) 
        self.bottom.set_data(data['bottom']) 
        self.left.set_data(data['left']) 
        self.right.set_data(data['right']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
            'item': self.item.get_data(),
            'top': self.top.get_data(),
            'bottom': self.bottom.get_data(),
            'left': self.left.get_data(),
            'right': self.right.get_data(),
        }


class DeleteSceneItemWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene = UnimplementedField('[field not implemented]')
        self.item = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene)
            layout.add(self.item)

    def payload(self):
        payload = {}
        payload['request-type'] = 'DeleteSceneItem'
        payload['scene'] = self.scene.get_data()
        payload['item'] = self.item.get_data()
        return payload

    def refresh(self):
        self.scene.refresh()
        self.item.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene.set_data(data['scene']) 
        self.item.set_data(data['item']) 

    def get_data(self):
        return {
            'scene': self.scene.get_data(),
            'item': self.item.get_data(),
        }


class AddSceneItemWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sceneName = SceneSelector(changed, parent=self)
        self.sourceName = SourceSelector(changed, parent=self)
        self.setVisible = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sceneName)
            layout.add(self.sourceName)
            layout.add(self.setVisible)

    def payload(self):
        payload = {}
        payload['request-type'] = 'AddSceneItem'
        payload['sceneName'] = self.sceneName.get_data()
        payload['sourceName'] = self.sourceName.get_data()
        payload['setVisible'] = self.setVisible.get_data()
        return payload

    def refresh(self):
        self.sceneName.refresh()
        self.sourceName.refresh()
        self.setVisible.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sceneName.set_data(data['sceneName']) 
        self.sourceName.set_data(data['sourceName']) 
        self.setVisible.set_data(data['setVisible']) 

    def get_data(self):
        return {
            'sceneName': self.sceneName.get_data(),
            'sourceName': self.sourceName.get_data(),
            'setVisible': self.setVisible.get_data(),
        }


class DuplicateSceneItemWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.fromScene = UnimplementedField('[field not implemented]')
        self.toScene = UnimplementedField('[field not implemented]')
        self.item = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.fromScene)
            layout.add(self.toScene)
            layout.add(self.item)

    def payload(self):
        payload = {}
        payload['request-type'] = 'DuplicateSceneItem'
        payload['fromScene'] = self.fromScene.get_data()
        payload['toScene'] = self.toScene.get_data()
        payload['item'] = self.item.get_data()
        return payload

    def refresh(self):
        self.fromScene.refresh()
        self.toScene.refresh()
        self.item.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.fromScene.set_data(data['fromScene']) 
        self.toScene.set_data(data['toScene']) 
        self.item.set_data(data['item']) 

    def get_data(self):
        return {
            'fromScene': self.fromScene.get_data(),
            'toScene': self.toScene.get_data(),
            'item': self.item.get_data(),
        }


class SetCurrentSceneWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetCurrentScene'
        payload['scene-name'] = self.scene_name.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
        }


class GetCurrentSceneWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetCurrentScene'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetSceneListWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSceneList'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class CreateSceneWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sceneName = SceneSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sceneName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'CreateScene'
        payload['sceneName'] = self.sceneName.get_data()
        return payload

    def refresh(self):
        self.sceneName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sceneName.set_data(data['sceneName']) 

    def get_data(self):
        return {
            'sceneName': self.sceneName.get_data(),
        }


class ReorderSceneItemsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene = UnimplementedField('[field not implemented]')
        self.items = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene)
            layout.add(self.items)

    def payload(self):
        payload = {}
        payload['request-type'] = 'ReorderSceneItems'
        payload['scene'] = self.scene.get_data()
        payload['items'] = self.items.get_data()
        return payload

    def refresh(self):
        self.scene.refresh()
        self.items.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene.set_data(data['scene']) 
        self.items.set_data(data['items']) 

    def get_data(self):
        return {
            'scene': self.scene.get_data(),
            'items': self.items.get_data(),
        }


class SetSceneTransitionOverrideWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sceneName = SceneSelector(changed, parent=self)
        self.transitionName = UnimplementedField('[field not implemented]')
        self.transitionDuration = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sceneName)
            layout.add(self.transitionName)
            layout.add(self.transitionDuration)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetSceneTransitionOverride'
        payload['sceneName'] = self.sceneName.get_data()
        payload['transitionName'] = self.transitionName.get_data()
        payload['transitionDuration'] = self.transitionDuration.get_data()
        return payload

    def refresh(self):
        self.sceneName.refresh()
        self.transitionName.refresh()
        self.transitionDuration.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sceneName.set_data(data['sceneName']) 
        self.transitionName.set_data(data['transitionName']) 
        self.transitionDuration.set_data(data['transitionDuration']) 

    def get_data(self):
        return {
            'sceneName': self.sceneName.get_data(),
            'transitionName': self.transitionName.get_data(),
            'transitionDuration': self.transitionDuration.get_data(),
        }


class RemoveSceneTransitionOverrideWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sceneName = SceneSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sceneName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'RemoveSceneTransitionOverride'
        payload['sceneName'] = self.sceneName.get_data()
        return payload

    def refresh(self):
        self.sceneName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sceneName.set_data(data['sceneName']) 

    def get_data(self):
        return {
            'sceneName': self.sceneName.get_data(),
        }


class GetSceneTransitionOverrideWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.sceneName = SceneSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.sceneName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetSceneTransitionOverride'
        payload['sceneName'] = self.sceneName.get_data()
        return payload

    def refresh(self):
        self.sceneName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.sceneName.set_data(data['sceneName']) 

    def get_data(self):
        return {
            'sceneName': self.sceneName.get_data(),
        }


class GetStreamingStatusWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetStreamingStatus'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartStopStreamingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartStopStreaming'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartStreamingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.stream = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.stream)

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartStreaming'
        payload['stream'] = self.stream.get_data()
        return payload

    def refresh(self):
        self.stream.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.stream.set_data(data['stream']) 

    def get_data(self):
        return {
            'stream': self.stream.get_data(),
        }


class StopStreamingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StopStreaming'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SetStreamSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.type = UnimplementedField('[field not implemented]')
        self.settings = UnimplementedField('[field not implemented]')
        self.save = BoolSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.settings)
            layout.add(self.save)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetStreamSettings'
        payload['type'] = self.type.get_data()
        payload['settings'] = self.settings.get_data()
        payload['save'] = self.save.get_data()
        return payload

    def refresh(self):
        self.type.refresh()
        self.settings.refresh()
        self.save.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.type.set_data(data['type']) 
        self.settings.set_data(data['settings']) 
        self.save.set_data(data['save']) 

    def get_data(self):
        return {
            'type': self.type.get_data(),
            'settings': self.settings.get_data(),
            'save': self.save.get_data(),
        }


class GetStreamSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetStreamSettings'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SaveStreamSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'SaveStreamSettings'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SendCaptionsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.text = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.text)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SendCaptions'
        payload['text'] = self.text.get_data()
        return payload

    def refresh(self):
        self.text.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.text.set_data(data['text']) 

    def get_data(self):
        return {
            'text': self.text.get_data(),
        }


class GetStudioModeStatusWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetStudioModeStatus'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetPreviewSceneWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetPreviewScene'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SetPreviewSceneWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.scene_name = SceneSelector(changed, parent=self)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.scene_name)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetPreviewScene'
        payload['scene-name'] = self.scene_name.get_data()
        return payload

    def refresh(self):
        self.scene_name.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.scene_name.set_data(data['scene_name']) 

    def get_data(self):
        return {
            'scene_name': self.scene_name.get_data(),
        }


class TransitionToProgramWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.with_transition = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.with_transition)

    def payload(self):
        payload = {}
        payload['request-type'] = 'TransitionToProgram'
        payload['with-transition'] = self.with_transition.get_data()
        return payload

    def refresh(self):
        self.with_transition.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.with_transition.set_data(data['with_transition']) 

    def get_data(self):
        return {
            'with_transition': self.with_transition.get_data(),
        }


class EnableStudioModeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'EnableStudioMode'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class DisableStudioModeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'DisableStudioMode'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ToggleStudioModeWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'ToggleStudioMode'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetTransitionListWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetTransitionList'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetCurrentTransitionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetCurrentTransition'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SetCurrentTransitionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.transition_name = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.transition_name)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetCurrentTransition'
        payload['transition-name'] = self.transition_name.get_data()
        return payload

    def refresh(self):
        self.transition_name.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.transition_name.set_data(data['transition_name']) 

    def get_data(self):
        return {
            'transition_name': self.transition_name.get_data(),
        }


class SetTransitionDurationWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.duration = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.duration)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetTransitionDuration'
        payload['duration'] = self.duration.get_data()
        return payload

    def refresh(self):
        self.duration.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.duration.set_data(data['duration']) 

    def get_data(self):
        return {
            'duration': self.duration.get_data(),
        }


class GetTransitionDurationWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetTransitionDuration'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetTransitionPositionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetTransitionPosition'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class GetTransitionSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.transitionName = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.transitionName)

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetTransitionSettings'
        payload['transitionName'] = self.transitionName.get_data()
        return payload

    def refresh(self):
        self.transitionName.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.transitionName.set_data(data['transitionName']) 

    def get_data(self):
        return {
            'transitionName': self.transitionName.get_data(),
        }


class SetTransitionSettingsWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.transitionName = UnimplementedField('[field not implemented]')
        self.transitionSettings = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.transitionName)
            layout.add(self.transitionSettings)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetTransitionSettings'
        payload['transitionName'] = self.transitionName.get_data()
        payload['transitionSettings'] = self.transitionSettings.get_data()
        return payload

    def refresh(self):
        self.transitionName.refresh()
        self.transitionSettings.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.transitionName.set_data(data['transitionName']) 
        self.transitionSettings.set_data(data['transitionSettings']) 

    def get_data(self):
        return {
            'transitionName': self.transitionName.get_data(),
            'transitionSettings': self.transitionSettings.get_data(),
        }


class ReleaseTBarWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'ReleaseTBar'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SetTBarPositionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        self.position = UnimplementedField('[field not implemented]')
        self.release = UnimplementedField('[field not implemented]')

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.position)
            layout.add(self.release)

    def payload(self):
        payload = {}
        payload['request-type'] = 'SetTBarPosition'
        payload['position'] = self.position.get_data()
        payload['release'] = self.release.get_data()
        return payload

    def refresh(self):
        self.position.refresh()
        self.release.refresh()
        return

    def set_data(self, data):
        self._data = data
        self.position.set_data(data['position']) 
        self.release.set_data(data['release']) 

    def get_data(self):
        return {
            'position': self.position.get_data(),
            'release': self.release.get_data(),
        }


class GetVirtualCamStatusWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'GetVirtualCamStatus'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartStopVirtualCamWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartStopVirtualCam'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StartVirtualCamWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StartVirtualCam'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StopVirtualCamWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('[ request has no fields ]'))

    def payload(self):
        payload = {}
        payload['request-type'] = 'StopVirtualCam'
        return payload

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }



widgets = {
    'GetVersion': GetVersionWidget,
    'GetAuthRequired': GetAuthRequiredWidget,
    'Authenticate': AuthenticateWidget,
    'SetHeartbeat': SetHeartbeatWidget,
    'SetFilenameFormatting': SetFilenameFormattingWidget,
    'GetFilenameFormatting': GetFilenameFormattingWidget,
    'GetStats': GetStatsWidget,
    'BroadcastCustomMessage': BroadcastCustomMessageWidget,
    'GetVideoInfo': GetVideoInfoWidget,
    'OpenProjector': OpenProjectorWidget,
    'TriggerHotkeyByName': TriggerHotkeyByNameWidget,
    'TriggerHotkeyBySequence': TriggerHotkeyBySequenceWidget,
    'ExecuteBatch': ExecuteBatchWidget,
    'Sleep': SleepWidget,
    'PlayPauseMedia': PlayPauseMediaWidget,
    'RestartMedia': RestartMediaWidget,
    'StopMedia': StopMediaWidget,
    'NextMedia': NextMediaWidget,
    'PreviousMedia': PreviousMediaWidget,
    'GetMediaDuration': GetMediaDurationWidget,
    'GetMediaTime': GetMediaTimeWidget,
    'SetMediaTime': SetMediaTimeWidget,
    'ScrubMedia': ScrubMediaWidget,
    'GetMediaState': GetMediaStateWidget,
    'GetMediaSourcesList': GetMediaSourcesListWidget,
    'CreateSource': CreateSourceWidget,
    'GetSourcesList': GetSourcesListWidget,
    'GetSourceTypesList': GetSourceTypesListWidget,
    'GetVolume': GetVolumeWidget,
    'SetVolume': SetVolumeWidget,
    'SetAudioTracks': SetAudioTracksWidget,
    'GetAudioTracks': GetAudioTracksWidget,
    'GetMute': GetMuteWidget,
    'SetMute': SetMuteWidget,
    'ToggleMute': ToggleMuteWidget,
    'GetSourceActive': GetSourceActiveWidget,
    'GetAudioActive': GetAudioActiveWidget,
    'SetSourceName': SetSourceNameWidget,
    'SetSyncOffset': SetSyncOffsetWidget,
    'GetSyncOffset': GetSyncOffsetWidget,
    'GetSourceSettings': GetSourceSettingsWidget,
    'SetSourceSettings': SetSourceSettingsWidget,
    'GetTextGDIPlusProperties': GetTextGDIPlusPropertiesWidget,
    'SetTextGDIPlusProperties': SetTextGDIPlusPropertiesWidget,
    'GetTextFreetype2Properties': GetTextFreetype2PropertiesWidget,
    'SetTextFreetype2Properties': SetTextFreetype2PropertiesWidget,
    'GetBrowserSourceProperties': GetBrowserSourcePropertiesWidget,
    'SetBrowserSourceProperties': SetBrowserSourcePropertiesWidget,
    'GetSpecialSources': GetSpecialSourcesWidget,
    'GetSourceFilters': GetSourceFiltersWidget,
    'GetSourceFilterInfo': GetSourceFilterInfoWidget,
    'AddFilterToSource': AddFilterToSourceWidget,
    'RemoveFilterFromSource': RemoveFilterFromSourceWidget,
    'ReorderSourceFilter': ReorderSourceFilterWidget,
    'MoveSourceFilter': MoveSourceFilterWidget,
    'SetSourceFilterSettings': SetSourceFilterSettingsWidget,
    'SetSourceFilterVisibility': SetSourceFilterVisibilityWidget,
    'GetAudioMonitorType': GetAudioMonitorTypeWidget,
    'SetAudioMonitorType': SetAudioMonitorTypeWidget,
    'GetSourceDefaultSettings': GetSourceDefaultSettingsWidget,
    'TakeSourceScreenshot': TakeSourceScreenshotWidget,
    'RefreshBrowserSource': RefreshBrowserSourceWidget,
    'ListOutputs': ListOutputsWidget,
    'GetOutputInfo': GetOutputInfoWidget,
    'StartOutput': StartOutputWidget,
    'StopOutput': StopOutputWidget,
    'SetCurrentProfile': SetCurrentProfileWidget,
    'GetCurrentProfile': GetCurrentProfileWidget,
    'ListProfiles': ListProfilesWidget,
    'GetRecordingStatus': GetRecordingStatusWidget,
    'StartStopRecording': StartStopRecordingWidget,
    'StartRecording': StartRecordingWidget,
    'StopRecording': StopRecordingWidget,
    'PauseRecording': PauseRecordingWidget,
    'ResumeRecording': ResumeRecordingWidget,
    'SetRecordingFolder': SetRecordingFolderWidget,
    'GetRecordingFolder': GetRecordingFolderWidget,
    'GetReplayBufferStatus': GetReplayBufferStatusWidget,
    'StartStopReplayBuffer': StartStopReplayBufferWidget,
    'StartReplayBuffer': StartReplayBufferWidget,
    'StopReplayBuffer': StopReplayBufferWidget,
    'SaveReplayBuffer': SaveReplayBufferWidget,
    'SetCurrentSceneCollection': SetCurrentSceneCollectionWidget,
    'GetCurrentSceneCollection': GetCurrentSceneCollectionWidget,
    'ListSceneCollections': ListSceneCollectionsWidget,
    'GetSceneItemList': GetSceneItemListWidget,
    'GetSceneItemProperties': GetSceneItemPropertiesWidget,
    'SetSceneItemProperties': SetSceneItemPropertiesWidget,
    'ResetSceneItem': ResetSceneItemWidget,
    'SetSceneItemRender': SetSceneItemRenderWidget,
    'SetSceneItemPosition': SetSceneItemPositionWidget,
    'SetSceneItemTransform': SetSceneItemTransformWidget,
    'SetSceneItemCrop': SetSceneItemCropWidget,
    'DeleteSceneItem': DeleteSceneItemWidget,
    'AddSceneItem': AddSceneItemWidget,
    'DuplicateSceneItem': DuplicateSceneItemWidget,
    'SetCurrentScene': SetCurrentSceneWidget,
    'GetCurrentScene': GetCurrentSceneWidget,
    'GetSceneList': GetSceneListWidget,
    'CreateScene': CreateSceneWidget,
    'ReorderSceneItems': ReorderSceneItemsWidget,
    'SetSceneTransitionOverride': SetSceneTransitionOverrideWidget,
    'RemoveSceneTransitionOverride': RemoveSceneTransitionOverrideWidget,
    'GetSceneTransitionOverride': GetSceneTransitionOverrideWidget,
    'GetStreamingStatus': GetStreamingStatusWidget,
    'StartStopStreaming': StartStopStreamingWidget,
    'StartStreaming': StartStreamingWidget,
    'StopStreaming': StopStreamingWidget,
    'SetStreamSettings': SetStreamSettingsWidget,
    'GetStreamSettings': GetStreamSettingsWidget,
    'SaveStreamSettings': SaveStreamSettingsWidget,
    'SendCaptions': SendCaptionsWidget,
    'GetStudioModeStatus': GetStudioModeStatusWidget,
    'GetPreviewScene': GetPreviewSceneWidget,
    'SetPreviewScene': SetPreviewSceneWidget,
    'TransitionToProgram': TransitionToProgramWidget,
    'EnableStudioMode': EnableStudioModeWidget,
    'DisableStudioMode': DisableStudioModeWidget,
    'ToggleStudioMode': ToggleStudioModeWidget,
    'GetTransitionList': GetTransitionListWidget,
    'GetCurrentTransition': GetCurrentTransitionWidget,
    'SetCurrentTransition': SetCurrentTransitionWidget,
    'SetTransitionDuration': SetTransitionDurationWidget,
    'GetTransitionDuration': GetTransitionDurationWidget,
    'GetTransitionPosition': GetTransitionPositionWidget,
    'GetTransitionSettings': GetTransitionSettingsWidget,
    'SetTransitionSettings': SetTransitionSettingsWidget,
    'ReleaseTBar': ReleaseTBarWidget,
    'SetTBarPosition': SetTBarPositionWidget,
    'GetVirtualCamStatus': GetVirtualCamStatusWidget,
    'StartStopVirtualCam': StartStopVirtualCamWidget,
    'StartVirtualCam': StartVirtualCamWidget,
    'StopVirtualCam': StopVirtualCamWidget,
}
