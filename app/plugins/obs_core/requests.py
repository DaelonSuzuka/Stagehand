from .base_classes import *
from qtstrap import *


categories = [
    'general',
    'media control',
    'sources',
    'outputs',
    'profiles',
    'recording',
    'replay buffer',
    'scene collections',
    'scene items',
    'scenes',
    'streaming',
    'studio mode',
    'transitions',
]


class GetVersion(BaseRequest):
    """Returns the latest version of the plugin and the API.

    :Returns:
        *version*
            type: double
            OBSRemote compatible API version. Fixed to 1.1 for retrocompatibility.
        *obs_websocket_version*
            type: String
            obs-websocket plugin version.
        *obs_studio_version*
            type: String
            OBS Studio program version.
        *available_requests*
            type: String
            List of available request types, formatted as a comma-separated list string (e.g. : "Method1,Method2,Method3").
        *supported_image_export_formats*
            type: String
            List of supported formats for features that use image export (like the TakeSourceScreenshot request type) formatted as a comma-separated list string
    """

    name = 'GetVersion'
    category = 'general'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['version'] = None
        self.datain['obs-websocket-version'] = None
        self.datain['obs-studio-version'] = None
        self.datain['available-requests'] = None
        self.datain['supported-image-export-formats'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetVersion'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetAuthRequired(BaseRequest):
    """Tells the client if authentication is required. If so, returns authentication parameters `challenge`
and `salt` (see "Authentication" for more information).

    :Returns:
        *authRequired*
            type: boolean
            Indicates whether authentication is required.
        *challenge*
            type: String (optional)

        *salt*
            type: String (optional)

    """

    name = 'GetAuthRequired'
    category = 'general'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['authRequired'] = None
        self.datain['challenge'] = None
        self.datain['salt'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetAuthRequired'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class Authenticate(BaseRequest):
    """Attempt to authenticate the client to the server.

    :Arguments:
        *auth*
            type: String
            Response to the auth challenge (see "Authentication" for more information).
    """

    name = 'Authenticate'
    category = 'general'
    fields = [
        'auth',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['auth'] = None

    @staticmethod
    def payload(auth):
        payload = {}
        payload['request-type'] = 'Authenticate'
        payload['auth'] = auth
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.auth.set_data(data['auth']) 

        def to_dict(self):
            return {
                'auth': self.auth.get_data(),
            }


class SetHeartbeat(BaseRequest):
    """Enable/disable sending of the Heartbeat event

    :Arguments:
        *enable*
            type: boolean
            Starts/Stops emitting heartbeat messages
    """

    name = 'SetHeartbeat'
    category = 'general'
    fields = [
        'enable',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['enable'] = None

    @staticmethod
    def payload(enable):
        payload = {}
        payload['request-type'] = 'SetHeartbeat'
        payload['enable'] = enable
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.enable.set_data(data['enable']) 

        def to_dict(self):
            return {
                'enable': self.enable.get_data(),
            }


class SetFilenameFormatting(BaseRequest):
    """Set the filename formatting string

    :Arguments:
        *filename_formatting*
            type: String
            Filename formatting string to set.
    """

    name = 'SetFilenameFormatting'
    category = 'general'
    fields = [
        'filename_formatting',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['filename_formatting'] = None

    @staticmethod
    def payload(filename_formatting):
        payload = {}
        payload['request-type'] = 'SetFilenameFormatting'
        payload['filename-formatting'] = filename_formatting
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.filename_formatting.set_data(data['filename_formatting']) 

        def to_dict(self):
            return {
                'filename_formatting': self.filename_formatting.get_data(),
            }


class GetFilenameFormatting(BaseRequest):
    """Get the filename formatting string

    :Returns:
        *filename_formatting*
            type: String
            Current filename formatting string.
    """

    name = 'GetFilenameFormatting'
    category = 'general'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['filename-formatting'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetFilenameFormatting'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetStats(BaseRequest):
    """Get OBS stats (almost the same info as provided in OBS' stats window)

    :Returns:
        *stats*
            type: OBSStats
            [OBS stats](#obsstats)
    """

    name = 'GetStats'
    category = 'general'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['stats'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStats'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class BroadcastCustomMessage(BaseRequest):
    """Broadcast custom message to all connected WebSocket clients

    :Arguments:
        *realm*
            type: String
            Identifier to be choosen by the client
        *data*
            type: Object
            User-defined data
    """

    name = 'BroadcastCustomMessage'
    category = 'general'
    fields = [
        'realm',
        'data',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['realm'] = None
        self.dataout['data'] = None

    @staticmethod
    def payload(realm, data):
        payload = {}
        payload['request-type'] = 'BroadcastCustomMessage'
        payload['realm'] = realm
        payload['data'] = data
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.realm.set_data(data['realm']) 
            self.data.set_data(data['data']) 

        def to_dict(self):
            return {
                'realm': self.realm.get_data(),
                'data': self.data.get_data(),
            }


class GetVideoInfo(BaseRequest):
    """Get basic OBS video information

    :Returns:
        *baseWidth*
            type: int
            Base (canvas) width
        *baseHeight*
            type: int
            Base (canvas) height
        *outputWidth*
            type: int
            Output width
        *outputHeight*
            type: int
            Output height
        *scaleType*
            type: String
            Scaling method used if output size differs from base size
        *fps*
            type: double
            Frames rendered per second
        *videoFormat*
            type: String
            Video color format
        *colorSpace*
            type: String
            Color space for YUV
        *colorRange*
            type: String
            Color range (full or partial)
    """

    name = 'GetVideoInfo'
    category = 'general'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['baseWidth'] = None
        self.datain['baseHeight'] = None
        self.datain['outputWidth'] = None
        self.datain['outputHeight'] = None
        self.datain['scaleType'] = None
        self.datain['fps'] = None
        self.datain['videoFormat'] = None
        self.datain['colorSpace'] = None
        self.datain['colorRange'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetVideoInfo'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class OpenProjector(BaseRequest):
    """Open a projector window or create a projector on a monitor. Requires OBS v24.0.4 or newer.

    :Arguments:
        *type*
            type: String (Optional)
            Type of projector: `Preview` (default), `Source`, `Scene`, `StudioProgram`, or `Multiview` (case insensitive).
        *monitor*
            type: int (Optional)
            Monitor to open the projector on. If -1 or omitted, opens a window.
        *geometry*
            type: String (Optional)
            Size and position of the projector window (only if monitor is -1). Encoded in Base64 using [Qt's geometry encoding](https://doc.qt.io/qt-5/qwidget.html#saveGeometry). Corresponds to OBS's saved projectors.
        *name*
            type: String (Optional)
            Name of the source or scene to be displayed (ignored for other projector types).
    """

    name = 'OpenProjector'
    category = 'general'
    fields = [
        'type',
        'monitor',
        'geometry',
        'name',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['type'] = None
        self.dataout['monitor'] = None
        self.dataout['geometry'] = None
        self.dataout['name'] = None

    @staticmethod
    def payload(type, monitor, geometry, name):
        payload = {}
        payload['request-type'] = 'OpenProjector'
        payload['type'] = type
        payload['monitor'] = monitor
        payload['geometry'] = geometry
        payload['name'] = name
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.type.set_data(data['type']) 
            self.monitor.set_data(data['monitor']) 
            self.geometry.set_data(data['geometry']) 
            self.name.set_data(data['name']) 

        def to_dict(self):
            return {
                'type': self.type.get_data(),
                'monitor': self.monitor.get_data(),
                'geometry': self.geometry.get_data(),
                'name': self.name.get_data(),
            }


class TriggerHotkeyByName(BaseRequest):
    """Executes hotkey routine, identified by hotkey unique name

    :Arguments:
        *hotkeyName*
            type: String
            Unique name of the hotkey, as defined when registering the hotkey (e.g. "ReplayBuffer.Save")
    """

    name = 'TriggerHotkeyByName'
    category = 'general'
    fields = [
        'hotkeyName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['hotkeyName'] = None

    @staticmethod
    def payload(hotkeyName):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyByName'
        payload['hotkeyName'] = hotkeyName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.hotkeyName.set_data(data['hotkeyName']) 

        def to_dict(self):
            return {
                'hotkeyName': self.hotkeyName.get_data(),
            }


class TriggerHotkeyBySequence(BaseRequest):
    """Executes hotkey routine, identified by bound combination of keys. A single key combination might trigger multiple hotkey routines depending on user settings

    :Arguments:
        *keyId*
            type: String
            Main key identifier (e.g. `OBS_KEY_A` for key "A"). Available identifiers [here](https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h)
        *keyModifiers*
            type: Object (Optional)
            Optional key modifiers object. False entries can be ommitted
    """

    name = 'TriggerHotkeyBySequence'
    category = 'general'
    fields = [
        'keyId',
        'keyModifiers',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['keyId'] = None
        self.dataout['keyModifiers'] = None

    @staticmethod
    def payload(keyId, keyModifiers):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyBySequence'
        payload['keyId'] = keyId
        payload['keyModifiers'] = keyModifiers
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.keyId.set_data(data['keyId']) 
            self.keyModifiers.set_data(data['keyModifiers']) 

        def to_dict(self):
            return {
                'keyId': self.keyId.get_data(),
                'keyModifiers': self.keyModifiers.get_data(),
            }


class ExecuteBatch(BaseRequest):
    """Executes a list of requests sequentially (one-by-one on the same thread).

    :Arguments:
        *requests*
            type: Array<Object>
            Array of requests to perform. Executed in order.
        *abortOnFail*
            type: boolean (Optional)
            Stop processing batch requests if one returns a failure.
    :Returns:
        *results*
            type: Array<Object>
            Batch requests results, ordered sequentially.
    """

    name = 'ExecuteBatch'
    category = 'general'
    fields = [
        'requests',
        'abortOnFail',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['results'] = None
        self.dataout = {}
        self.dataout['requests'] = None
        self.dataout['abortOnFail'] = None

    @staticmethod
    def payload(requests, abortOnFail):
        payload = {}
        payload['request-type'] = 'ExecuteBatch'
        payload['requests'] = requests
        payload['abortOnFail'] = abortOnFail
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.requests.set_data(data['requests']) 
            self.abortOnFail.set_data(data['abortOnFail']) 

        def to_dict(self):
            return {
                'requests': self.requests.get_data(),
                'abortOnFail': self.abortOnFail.get_data(),
            }


class Sleep(BaseRequest):
    """Waits for the specified duration. Designed to be used in `ExecuteBatch` operations.

    :Arguments:
        *sleepMillis*
            type: int
            Delay in milliseconds to wait before continuing.
    """

    name = 'Sleep'
    category = 'general'
    fields = [
        'sleepMillis',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sleepMillis'] = None

    @staticmethod
    def payload(sleepMillis):
        payload = {}
        payload['request-type'] = 'Sleep'
        payload['sleepMillis'] = sleepMillis
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sleepMillis.set_data(data['sleepMillis']) 

        def to_dict(self):
            return {
                'sleepMillis': self.sleepMillis.get_data(),
            }


class PlayPauseMedia(BaseRequest):
    """Pause or play a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
Note :Leaving out `playPause` toggles the current pause state

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *playPause*
            type: boolean
            (optional) Whether to pause or play the source. `false` for play, `true` for pause.
    """

    name = 'PlayPauseMedia'
    category = 'media control'
    fields = [
        'sourceName',
        'playPause',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['playPause'] = None

    @staticmethod
    def payload(sourceName, playPause):
        payload = {}
        payload['request-type'] = 'PlayPauseMedia'
        payload['sourceName'] = sourceName
        payload['playPause'] = playPause
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.playPause.set_data(data['playPause']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'playPause': self.playPause.get_data(),
            }


class RestartMedia(BaseRequest):
    """Restart a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
        *sourceName*
            type: String
            Source name.
    """

    name = 'RestartMedia'
    category = 'media control'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'RestartMedia'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class StopMedia(BaseRequest):
    """Stop a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
        *sourceName*
            type: String
            Source name.
    """

    name = 'StopMedia'
    category = 'media control'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'StopMedia'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class NextMedia(BaseRequest):
    """Skip to the next media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

    :Arguments:
        *sourceName*
            type: String
            Source name.
    """

    name = 'NextMedia'
    category = 'media control'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'NextMedia'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class PreviousMedia(BaseRequest):
    """Go to the previous media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

    :Arguments:
        *sourceName*
            type: String
            Source name.
    """

    name = 'PreviousMedia'
    category = 'media control'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'PreviousMedia'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class GetMediaDuration(BaseRequest):
    """Get the length of media in milliseconds. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
Note: For some reason, for the first 5 or so seconds that the media is playing, the total duration can be off by upwards of 50ms.

    :Arguments:
        *sourceName*
            type: String
            Source name.
    :Returns:
        *mediaDuration*
            type: int
            The total length of media in milliseconds..
    """

    name = 'GetMediaDuration'
    category = 'media control'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['mediaDuration'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaDuration'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class GetMediaTime(BaseRequest):
    """Get the current timestamp of media in milliseconds. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
        *sourceName*
            type: String
            Source name.
    :Returns:
        *timestamp*
            type: int
            The time in milliseconds since the start of the media.
    """

    name = 'GetMediaTime'
    category = 'media control'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['timestamp'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaTime'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class SetMediaTime(BaseRequest):
    """Set the timestamp of a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *timestamp*
            type: int
            Milliseconds to set the timestamp to.
    """

    name = 'SetMediaTime'
    category = 'media control'
    fields = [
        'sourceName',
        'timestamp',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['timestamp'] = None

    @staticmethod
    def payload(sourceName, timestamp):
        payload = {}
        payload['request-type'] = 'SetMediaTime'
        payload['sourceName'] = sourceName
        payload['timestamp'] = timestamp
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.timestamp.set_data(data['timestamp']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'timestamp': self.timestamp.get_data(),
            }


class ScrubMedia(BaseRequest):
    """Scrub media using a supplied offset. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)
Note: Due to processing/network delays, this request is not perfect. The processing rate of this request has also not been tested.

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *timeOffset*
            type: int
            Millisecond offset (positive or negative) to offset the current media position.
    """

    name = 'ScrubMedia'
    category = 'media control'
    fields = [
        'sourceName',
        'timeOffset',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['timeOffset'] = None

    @staticmethod
    def payload(sourceName, timeOffset):
        payload = {}
        payload['request-type'] = 'ScrubMedia'
        payload['sourceName'] = sourceName
        payload['timeOffset'] = timeOffset
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.timeOffset.set_data(data['timeOffset']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'timeOffset': self.timeOffset.get_data(),
            }


class GetMediaState(BaseRequest):
    """Get the current playing state of a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
        *sourceName*
            type: String
            Source name.
    :Returns:
        *mediaState*
            type: String
            The media state of the provided source. States: `none`, `playing`, `opening`, `buffering`, `paused`, `stopped`, `ended`, `error`, `unknown`
    """

    name = 'GetMediaState'
    category = 'media control'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['mediaState'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaState'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class GetMediaSourcesList(BaseRequest):
    """List the media state of all media sources (vlc and media source)

    :Returns:
        *mediaSources*
            type: Array<Object>
            Array of sources
    """

    name = 'GetMediaSourcesList'
    category = 'sources'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['mediaSources'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetMediaSourcesList'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class CreateSource(BaseRequest):
    """Create a source and add it as a sceneitem to a scene.

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *sourceKind*
            type: String
            Source kind, Eg. `vlc_source`.
        *sceneName*
            type: String
            Scene to add the new source to.
        *sourceSettings*
            type: Object (optional)
            Source settings data.
        *setVisible*
            type: boolean (optional)
            Set the created SceneItem as visible or not. Defaults to true
    :Returns:
        *itemId*
            type: int
            ID of the SceneItem in the scene.
    """

    name = 'CreateSource'
    category = 'sources'
    fields = [
        'sourceName',
        'sourceKind',
        'sceneName',
        'sourceSettings',
        'setVisible',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['itemId'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['sourceKind'] = None
        self.dataout['sceneName'] = None
        self.dataout['sourceSettings'] = None
        self.dataout['setVisible'] = None

    @staticmethod
    def payload(sourceName, sourceKind, sceneName, sourceSettings=None, setVisible=None):
        payload = {}
        payload['request-type'] = 'CreateSource'
        payload['sourceName'] = sourceName
        payload['sourceKind'] = sourceKind
        payload['sceneName'] = sceneName
        payload['sourceSettings'] = sourceSettings
        payload['setVisible'] = setVisible
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.sourceKind.set_data(data['sourceKind']) 
            self.sceneName.set_data(data['sceneName']) 
            self.sourceSettings.set_data(data['sourceSettings']) 
            self.setVisible.set_data(data['setVisible']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'sourceKind': self.sourceKind.get_data(),
                'sceneName': self.sceneName.get_data(),
                'sourceSettings': self.sourceSettings.get_data(),
                'setVisible': self.setVisible.get_data(),
            }


class GetSourcesList(BaseRequest):
    """List all sources available in the running OBS instance

    :Returns:
        *sources*
            type: Array<Object>
            Array of sources
    """

    name = 'GetSourcesList'
    category = 'sources'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sources'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSourcesList'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetSourceTypesList(BaseRequest):
    """Get a list of all available sources types

    :Returns:
        *types*
            type: Array<Object>
            Array of source types
    """

    name = 'GetSourceTypesList'
    category = 'sources'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['types'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSourceTypesList'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetVolume(BaseRequest):
    """Get the volume of the specified source. Default response uses mul format, NOT SLIDER PERCENTAGE.

    :Arguments:
        *source*
            type: String
            Source name.
        *useDecibel*
            type: boolean (optional)
            Output volume in decibels of attenuation instead of amplitude/mul.
    :Returns:
        *name*
            type: String
            Source name.
        *volume*
            type: double
            Volume of the source. Between `0.0` and `20.0` if using mul, under `26.0` if using dB.
        *muted*
            type: boolean
            Indicates whether the source is muted.
    """

    name = 'GetVolume'
    category = 'sources'
    fields = [
        'source',
        'useDecibel',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['volume'] = None
        self.datain['muted'] = None
        self.dataout = {}
        self.dataout['source'] = None
        self.dataout['useDecibel'] = None

    @staticmethod
    def payload(source, useDecibel=None):
        payload = {}
        payload['request-type'] = 'GetVolume'
        payload['source'] = source
        payload['useDecibel'] = useDecibel
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 
            self.useDecibel.set_data(data['useDecibel']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
                'useDecibel': self.useDecibel.get_data(),
            }


class SetVolume(BaseRequest):
    """Set the volume of the specified source. Default request format uses mul, NOT SLIDER PERCENTAGE.

    :Arguments:
        *source*
            type: String
            Source name.
        *volume*
            type: double
            Desired volume. Must be between `0.0` and `20.0` for mul, and under 26.0 for dB. OBS will interpret dB values under -100.0 as Inf. Note: The OBS volume sliders only reach a maximum of 1.0mul/0.0dB, however OBS actually supports larger values.
        *useDecibel*
            type: boolean (optional)
            Interperet `volume` data as decibels instead of amplitude/mul.
    """

    name = 'SetVolume'
    category = 'sources'
    fields = [
        'source',
        'volume',
        'useDecibel',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['source'] = None
        self.dataout['volume'] = None
        self.dataout['useDecibel'] = None

    @staticmethod
    def payload(source, volume, useDecibel=None):
        payload = {}
        payload['request-type'] = 'SetVolume'
        payload['source'] = source
        payload['volume'] = volume
        payload['useDecibel'] = useDecibel
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 
            self.volume.set_data(data['volume']) 
            self.useDecibel.set_data(data['useDecibel']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
                'volume': self.volume.get_data(),
                'useDecibel': self.useDecibel.get_data(),
            }


class SetTracks(BaseRequest):
    """Changes whether an audio track is active for a source.

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *track*
            type: int
            Audio tracks 1-6.
        *active*
            type: boolean
            Whether audio track is active or not.
    """

    name = 'SetTracks'
    category = 'sources'
    fields = [
        'sourceName',
        'track',
        'active',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['track'] = None
        self.dataout['active'] = None

    @staticmethod
    def payload(sourceName, track, active):
        payload = {}
        payload['request-type'] = 'SetTracks'
        payload['sourceName'] = sourceName
        payload['track'] = track
        payload['active'] = active
        return payload

    class Widget(QWidget):
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
            payload['request-type'] = 'SetTracks'
            payload['sourceName'] = self.sourceName.get_data()
            payload['track'] = self.track.get_data()
            payload['active'] = self.active.get_data()
            return payload

        def refresh(self):
            self.sourceName.refresh()
            self.track.refresh()
            self.active.refresh()
            return

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.track.set_data(data['track']) 
            self.active.set_data(data['active']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'track': self.track.get_data(),
                'active': self.active.get_data(),
            }


class GetTracks(BaseRequest):
    """Gets whether an audio track is active for a source.

    :Arguments:
        *sourceName*
            type: String
            Source name.
    :Returns:
        *track1*
            type: boolean

        *track2*
            type: boolean

        *track3*
            type: boolean

        *track4*
            type: boolean

        *track5*
            type: boolean

        *track6*
            type: boolean

    """

    name = 'GetTracks'
    category = 'sources'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['track1'] = None
        self.datain['track2'] = None
        self.datain['track3'] = None
        self.datain['track4'] = None
        self.datain['track5'] = None
        self.datain['track6'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetTracks'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed
            self.sourceName = SourceSelector(changed, parent=self)

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(self.sourceName)

        def payload(self):
            payload = {}
            payload['request-type'] = 'GetTracks'
            payload['sourceName'] = self.sourceName.get_data()
            return payload

        def refresh(self):
            self.sourceName.refresh()
            return

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class GetMute(BaseRequest):
    """Get the mute status of a specified source.

    :Arguments:
        *source*
            type: String
            Source name.
    :Returns:
        *name*
            type: String
            Source name.
        *muted*
            type: boolean
            Mute status of the source.
    """

    name = 'GetMute'
    category = 'sources'
    fields = [
        'source',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['muted'] = None
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetMute'
        payload['source'] = source
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
            }


class SetMute(BaseRequest):
    """Sets the mute status of a specified source.

    :Arguments:
        *source*
            type: String
            Source name.
        *mute*
            type: boolean
            Desired mute status.
    """

    name = 'SetMute'
    category = 'sources'
    fields = [
        'source',
        'mute',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['source'] = None
        self.dataout['mute'] = None

    @staticmethod
    def payload(source, mute):
        payload = {}
        payload['request-type'] = 'SetMute'
        payload['source'] = source
        payload['mute'] = mute
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 
            self.mute.set_data(data['mute']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
                'mute': self.mute.get_data(),
            }


class ToggleMute(BaseRequest):
    """Inverts the mute status of a specified source.

    :Arguments:
        *source*
            type: String
            Source name.
    """

    name = 'ToggleMute'
    category = 'sources'
    fields = [
        'source',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'ToggleMute'
        payload['source'] = source
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
            }


class GetSourceActive(BaseRequest):
    """Get the source's active status of a specified source (if it is showing in the final mix).

    :Arguments:
        *sourceName*
            type: String
            Source name.
    :Returns:
        *sourceActive*
            type: boolean
            Source active status of the source.
    """

    name = 'GetSourceActive'
    category = 'sources'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceActive'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetSourceActive'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class GetAudioActive(BaseRequest):
    """Get the audio's active status of a specified source.

    :Arguments:
        *sourceName*
            type: String
            Source name.
    :Returns:
        *audioActive*
            type: boolean
            Audio active status of the source.
    """

    name = 'GetAudioActive'
    category = 'sources'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['audioActive'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetAudioActive'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class SetSourceName(BaseRequest):
    """

Note: If the new name already exists as a source, obs-websocket will return an error.

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *newName*
            type: String
            New source name.
    """

    name = 'SetSourceName'
    category = 'sources'
    fields = [
        'sourceName',
        'newName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['newName'] = None

    @staticmethod
    def payload(sourceName, newName):
        payload = {}
        payload['request-type'] = 'SetSourceName'
        payload['sourceName'] = sourceName
        payload['newName'] = newName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.newName.set_data(data['newName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'newName': self.newName.get_data(),
            }


class SetSyncOffset(BaseRequest):
    """Set the audio sync offset of a specified source.

    :Arguments:
        *source*
            type: String
            Source name.
        *offset*
            type: int
            The desired audio sync offset (in nanoseconds).
    """

    name = 'SetSyncOffset'
    category = 'sources'
    fields = [
        'source',
        'offset',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['source'] = None
        self.dataout['offset'] = None

    @staticmethod
    def payload(source, offset):
        payload = {}
        payload['request-type'] = 'SetSyncOffset'
        payload['source'] = source
        payload['offset'] = offset
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 
            self.offset.set_data(data['offset']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
                'offset': self.offset.get_data(),
            }


class GetSyncOffset(BaseRequest):
    """Get the audio sync offset of a specified source.

    :Arguments:
        *source*
            type: String
            Source name.
    :Returns:
        *name*
            type: String
            Source name.
        *offset*
            type: int
            The audio sync offset (in nanoseconds).
    """

    name = 'GetSyncOffset'
    category = 'sources'
    fields = [
        'source',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['offset'] = None
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetSyncOffset'
        payload['source'] = source
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
            }


class GetSourceSettings(BaseRequest):
    """Get settings of the specified source

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *sourceType*
            type: String (optional)
            Type of the specified source. Useful for type-checking if you expect a specific settings schema.
    :Returns:
        *sourceName*
            type: String
            Source name
        *sourceType*
            type: String
            Type of the specified source
        *sourceSettings*
            type: Object
            Source settings (varies between source types, may require some probing around).
    """

    name = 'GetSourceSettings'
    category = 'sources'
    fields = [
        'sourceName',
        'sourceType',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None
        self.datain['sourceSettings'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['sourceType'] = None

    @staticmethod
    def payload(sourceName, sourceType=None):
        payload = {}
        payload['request-type'] = 'GetSourceSettings'
        payload['sourceName'] = sourceName
        payload['sourceType'] = sourceType
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.sourceType.set_data(data['sourceType']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'sourceType': self.sourceType.get_data(),
            }


class SetSourceSettings(BaseRequest):
    """Set settings of the specified source.

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *sourceType*
            type: String (optional)
            Type of the specified source. Useful for type-checking to avoid settings a set of settings incompatible with the actual source's type.
        *sourceSettings*
            type: Object
            Source settings (varies between source types, may require some probing around).
    :Returns:
        *sourceName*
            type: String
            Source name
        *sourceType*
            type: String
            Type of the specified source
        *sourceSettings*
            type: Object
            Updated source settings
    """

    name = 'SetSourceSettings'
    category = 'sources'
    fields = [
        'sourceName',
        'sourceType',
        'sourceSettings',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None
        self.datain['sourceSettings'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['sourceSettings'] = None
        self.dataout['sourceType'] = None

    @staticmethod
    def payload(sourceName, sourceSettings, sourceType=None):
        payload = {}
        payload['request-type'] = 'SetSourceSettings'
        payload['sourceName'] = sourceName
        payload['sourceType'] = sourceType
        payload['sourceSettings'] = sourceSettings
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.sourceType.set_data(data['sourceType']) 
            self.sourceSettings.set_data(data['sourceSettings']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'sourceType': self.sourceType.get_data(),
                'sourceSettings': self.sourceSettings.get_data(),
            }


class GetTextGDIPlusProperties(BaseRequest):
    """Get the current properties of a Text GDI Plus source.

    :Arguments:
        *source*
            type: String
            Source name.
    :Returns:
        *source*
            type: String
            Source name.
        *align*
            type: String
            Text Alignment ("left", "center", "right").
        *bk_color*
            type: int
            Background color.
        *bk_opacity*
            type: int
            Background opacity (0-100).
        *chatlog*
            type: boolean
            Chat log.
        *chatlog_lines*
            type: int
            Chat log lines.
        *color*
            type: int
            Text color.
        *extents*
            type: boolean
            Extents wrap.
        *extents_cx*
            type: int
            Extents cx.
        *extents_cy*
            type: int
            Extents cy.
        *file*
            type: String
            File path name.
        *read_from_file*
            type: boolean
            Read text from the specified file.
        *font*
            type: Object
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
        *gradient*
            type: boolean
            Gradient enabled.
        *gradient_color*
            type: int
            Gradient color.
        *gradient_dir*
            type: float
            Gradient direction.
        *gradient_opacity*
            type: int
            Gradient opacity (0-100).
        *outline*
            type: boolean
            Outline.
        *outline_color*
            type: int
            Outline color.
        *outline_size*
            type: int
            Outline size.
        *outline_opacity*
            type: int
            Outline opacity (0-100).
        *text*
            type: String
            Text content to be displayed.
        *valign*
            type: String
            Text vertical alignment ("top", "center", "bottom").
        *vertical*
            type: boolean
            Vertical text enabled.
    """

    name = 'GetTextGDIPlusProperties'
    category = 'sources'
    fields = [
        'source',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['source'] = None
        self.datain['align'] = None
        self.datain['bk_color'] = None
        self.datain['bk_opacity'] = None
        self.datain['chatlog'] = None
        self.datain['chatlog_lines'] = None
        self.datain['color'] = None
        self.datain['extents'] = None
        self.datain['extents_cx'] = None
        self.datain['extents_cy'] = None
        self.datain['file'] = None
        self.datain['read_from_file'] = None
        self.datain['font'] = None
        self.datain['gradient'] = None
        self.datain['gradient_color'] = None
        self.datain['gradient_dir'] = None
        self.datain['gradient_opacity'] = None
        self.datain['outline'] = None
        self.datain['outline_color'] = None
        self.datain['outline_size'] = None
        self.datain['outline_opacity'] = None
        self.datain['text'] = None
        self.datain['valign'] = None
        self.datain['vertical'] = None
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetTextGDIPlusProperties'
        payload['source'] = source
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
            }


class SetTextGDIPlusProperties(BaseRequest):
    """Set the current properties of a Text GDI Plus source.

    :Arguments:
        *source*
            type: String
            Name of the source.
        *align*
            type: String (optional)
            Text Alignment ("left", "center", "right").
        *bk_color*
            type: int (optional)
            Background color.
        *bk_opacity*
            type: int (optional)
            Background opacity (0-100).
        *chatlog*
            type: boolean (optional)
            Chat log.
        *chatlog_lines*
            type: int (optional)
            Chat log lines.
        *color*
            type: int (optional)
            Text color.
        *extents*
            type: boolean (optional)
            Extents wrap.
        *extents_cx*
            type: int (optional)
            Extents cx.
        *extents_cy*
            type: int (optional)
            Extents cy.
        *file*
            type: String (optional)
            File path name.
        *read_from_file*
            type: boolean (optional)
            Read text from the specified file.
        *font*
            type: Object (optional)
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
        *gradient*
            type: boolean (optional)
            Gradient enabled.
        *gradient_color*
            type: int (optional)
            Gradient color.
        *gradient_dir*
            type: float (optional)
            Gradient direction.
        *gradient_opacity*
            type: int (optional)
            Gradient opacity (0-100).
        *outline*
            type: boolean (optional)
            Outline.
        *outline_color*
            type: int (optional)
            Outline color.
        *outline_size*
            type: int (optional)
            Outline size.
        *outline_opacity*
            type: int (optional)
            Outline opacity (0-100).
        *text*
            type: String (optional)
            Text content to be displayed.
        *valign*
            type: String (optional)
            Text vertical alignment ("top", "center", "bottom").
        *vertical*
            type: boolean (optional)
            Vertical text enabled.
        *render*
            type: boolean (optional)
            Visibility of the scene item.
    """

    name = 'SetTextGDIPlusProperties'
    category = 'sources'
    fields = [
        'source',
        'align',
        'bk_color',
        'bk_opacity',
        'chatlog',
        'chatlog_lines',
        'color',
        'extents',
        'extents_cx',
        'extents_cy',
        'file',
        'read_from_file',
        'font',
        'gradient',
        'gradient_color',
        'gradient_dir',
        'gradient_opacity',
        'outline',
        'outline_color',
        'outline_size',
        'outline_opacity',
        'text',
        'valign',
        'vertical',
        'render',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['source'] = None
        self.dataout['align'] = None
        self.dataout['bk_color'] = None
        self.dataout['bk_opacity'] = None
        self.dataout['chatlog'] = None
        self.dataout['chatlog_lines'] = None
        self.dataout['color'] = None
        self.dataout['extents'] = None
        self.dataout['extents_cx'] = None
        self.dataout['extents_cy'] = None
        self.dataout['file'] = None
        self.dataout['read_from_file'] = None
        self.dataout['font'] = None
        self.dataout['gradient'] = None
        self.dataout['gradient_color'] = None
        self.dataout['gradient_dir'] = None
        self.dataout['gradient_opacity'] = None
        self.dataout['outline'] = None
        self.dataout['outline_color'] = None
        self.dataout['outline_size'] = None
        self.dataout['outline_opacity'] = None
        self.dataout['text'] = None
        self.dataout['valign'] = None
        self.dataout['vertical'] = None
        self.dataout['render'] = None

    @staticmethod
    def payload(source, align=None, bk_color=None, bk_opacity=None, chatlog=None, chatlog_lines=None, color=None, extents=None, extents_cx=None, extents_cy=None, file=None, read_from_file=None, font=None, gradient=None, gradient_color=None, gradient_dir=None, gradient_opacity=None, outline=None, outline_color=None, outline_size=None, outline_opacity=None, text=None, valign=None, vertical=None, render=None):
        payload = {}
        payload['request-type'] = 'SetTextGDIPlusProperties'
        payload['source'] = source
        payload['align'] = align
        payload['bk_color'] = bk_color
        payload['bk_opacity'] = bk_opacity
        payload['chatlog'] = chatlog
        payload['chatlog_lines'] = chatlog_lines
        payload['color'] = color
        payload['extents'] = extents
        payload['extents_cx'] = extents_cx
        payload['extents_cy'] = extents_cy
        payload['file'] = file
        payload['read_from_file'] = read_from_file
        payload['font'] = font
        payload['gradient'] = gradient
        payload['gradient_color'] = gradient_color
        payload['gradient_dir'] = gradient_dir
        payload['gradient_opacity'] = gradient_opacity
        payload['outline'] = outline
        payload['outline_color'] = outline_color
        payload['outline_size'] = outline_size
        payload['outline_opacity'] = outline_opacity
        payload['text'] = text
        payload['valign'] = valign
        payload['vertical'] = vertical
        payload['render'] = render
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
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

        def to_dict(self):
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


class GetTextFreetype2Properties(BaseRequest):
    """Get the current properties of a Text Freetype 2 source.

    :Arguments:
        *source*
            type: String
            Source name.
    :Returns:
        *source*
            type: String
            Source name
        *color1*
            type: int
            Gradient top color.
        *color2*
            type: int
            Gradient bottom color.
        *custom_width*
            type: int
            Custom width (0 to disable).
        *drop_shadow*
            type: boolean
            Drop shadow.
        *font*
            type: Object
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
        *from_file*
            type: boolean
            Read text from the specified file.
        *log_mode*
            type: boolean
            Chat log.
        *outline*
            type: boolean
            Outline.
        *text*
            type: String
            Text content to be displayed.
        *text_file*
            type: String
            File path.
        *word_wrap*
            type: boolean
            Word wrap.
    """

    name = 'GetTextFreetype2Properties'
    category = 'sources'
    fields = [
        'source',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['source'] = None
        self.datain['color1'] = None
        self.datain['color2'] = None
        self.datain['custom_width'] = None
        self.datain['drop_shadow'] = None
        self.datain['font'] = None
        self.datain['from_file'] = None
        self.datain['log_mode'] = None
        self.datain['outline'] = None
        self.datain['text'] = None
        self.datain['text_file'] = None
        self.datain['word_wrap'] = None
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetTextFreetype2Properties'
        payload['source'] = source
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
            }


class SetTextFreetype2Properties(BaseRequest):
    """Set the current properties of a Text Freetype 2 source.

    :Arguments:
        *source*
            type: String
            Source name.
        *color1*
            type: int (optional)
            Gradient top color.
        *color2*
            type: int (optional)
            Gradient bottom color.
        *custom_width*
            type: int (optional)
            Custom width (0 to disable).
        *drop_shadow*
            type: boolean (optional)
            Drop shadow.
        *font*
            type: Object (optional)
            Holds data for the font. Ex: `"font": { "face": "Arial", "flags": 0, "size": 150, "style": "" }`
        *from_file*
            type: boolean (optional)
            Read text from the specified file.
        *log_mode*
            type: boolean (optional)
            Chat log.
        *outline*
            type: boolean (optional)
            Outline.
        *text*
            type: String (optional)
            Text content to be displayed.
        *text_file*
            type: String (optional)
            File path.
        *word_wrap*
            type: boolean (optional)
            Word wrap.
    """

    name = 'SetTextFreetype2Properties'
    category = 'sources'
    fields = [
        'source',
        'color1',
        'color2',
        'custom_width',
        'drop_shadow',
        'font',
        'from_file',
        'log_mode',
        'outline',
        'text',
        'text_file',
        'word_wrap',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['source'] = None
        self.dataout['color1'] = None
        self.dataout['color2'] = None
        self.dataout['custom_width'] = None
        self.dataout['drop_shadow'] = None
        self.dataout['font'] = None
        self.dataout['from_file'] = None
        self.dataout['log_mode'] = None
        self.dataout['outline'] = None
        self.dataout['text'] = None
        self.dataout['text_file'] = None
        self.dataout['word_wrap'] = None

    @staticmethod
    def payload(source, color1=None, color2=None, custom_width=None, drop_shadow=None, font=None, from_file=None, log_mode=None, outline=None, text=None, text_file=None, word_wrap=None):
        payload = {}
        payload['request-type'] = 'SetTextFreetype2Properties'
        payload['source'] = source
        payload['color1'] = color1
        payload['color2'] = color2
        payload['custom_width'] = custom_width
        payload['drop_shadow'] = drop_shadow
        payload['font'] = font
        payload['from_file'] = from_file
        payload['log_mode'] = log_mode
        payload['outline'] = outline
        payload['text'] = text
        payload['text_file'] = text_file
        payload['word_wrap'] = word_wrap
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
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

        def to_dict(self):
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


class GetBrowserSourceProperties(BaseRequest):
    """Get current properties for a Browser Source.

    :Arguments:
        *source*
            type: String
            Source name.
    :Returns:
        *source*
            type: String
            Source name.
        *is_local_file*
            type: boolean
            Indicates that a local file is in use.
        *local_file*
            type: String
            file path.
        *url*
            type: String
            Url.
        *css*
            type: String
            CSS to inject.
        *width*
            type: int
            Width.
        *height*
            type: int
            Height.
        *fps*
            type: int
            Framerate.
        *shutdown*
            type: boolean
            Indicates whether the source should be shutdown when not visible.
    """

    name = 'GetBrowserSourceProperties'
    category = 'sources'
    fields = [
        'source',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['source'] = None
        self.datain['is_local_file'] = None
        self.datain['local_file'] = None
        self.datain['url'] = None
        self.datain['css'] = None
        self.datain['width'] = None
        self.datain['height'] = None
        self.datain['fps'] = None
        self.datain['shutdown'] = None
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetBrowserSourceProperties'
        payload['source'] = source
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.source.set_data(data['source']) 

        def to_dict(self):
            return {
                'source': self.source.get_data(),
            }


class SetBrowserSourceProperties(BaseRequest):
    """Set current properties for a Browser Source.

    :Arguments:
        *source*
            type: String
            Name of the source.
        *is_local_file*
            type: boolean (optional)
            Indicates that a local file is in use.
        *local_file*
            type: String (optional)
            file path.
        *url*
            type: String (optional)
            Url.
        *css*
            type: String (optional)
            CSS to inject.
        *width*
            type: int (optional)
            Width.
        *height*
            type: int (optional)
            Height.
        *fps*
            type: int (optional)
            Framerate.
        *shutdown*
            type: boolean (optional)
            Indicates whether the source should be shutdown when not visible.
        *render*
            type: boolean (optional)
            Visibility of the scene item.
    """

    name = 'SetBrowserSourceProperties'
    category = 'sources'
    fields = [
        'source',
        'is_local_file',
        'local_file',
        'url',
        'css',
        'width',
        'height',
        'fps',
        'shutdown',
        'render',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['source'] = None
        self.dataout['is_local_file'] = None
        self.dataout['local_file'] = None
        self.dataout['url'] = None
        self.dataout['css'] = None
        self.dataout['width'] = None
        self.dataout['height'] = None
        self.dataout['fps'] = None
        self.dataout['shutdown'] = None
        self.dataout['render'] = None

    @staticmethod
    def payload(source, is_local_file=None, local_file=None, url=None, css=None, width=None, height=None, fps=None, shutdown=None, render=None):
        payload = {}
        payload['request-type'] = 'SetBrowserSourceProperties'
        payload['source'] = source
        payload['is_local_file'] = is_local_file
        payload['local_file'] = local_file
        payload['url'] = url
        payload['css'] = css
        payload['width'] = width
        payload['height'] = height
        payload['fps'] = fps
        payload['shutdown'] = shutdown
        payload['render'] = render
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
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

        def to_dict(self):
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


class GetSpecialSources(BaseRequest):
    """Get configured special sources like Desktop Audio and Mic/Aux sources.

    :Returns:
        *desktop_1*
            type: String (optional)
            Name of the first Desktop Audio capture source.
        *desktop_2*
            type: String (optional)
            Name of the second Desktop Audio capture source.
        *mic_1*
            type: String (optional)
            Name of the first Mic/Aux input source.
        *mic_2*
            type: String (optional)
            Name of the second Mic/Aux input source.
        *mic_3*
            type: String (optional)
            NAme of the third Mic/Aux input source.
    """

    name = 'GetSpecialSources'
    category = 'sources'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['desktop-1'] = None
        self.datain['desktop-2'] = None
        self.datain['mic-1'] = None
        self.datain['mic-2'] = None
        self.datain['mic-3'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSpecialSources'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetSourceFilters(BaseRequest):
    """List filters applied to a source

    :Arguments:
        *sourceName*
            type: String
            Source name
    :Returns:
        *filters*
            type: Array<Object>
            List of filters for the specified source
    """

    name = 'GetSourceFilters'
    category = 'sources'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['filters'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetSourceFilters'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class GetSourceFilterInfo(BaseRequest):
    """List filters applied to a source

    :Arguments:
        *sourceName*
            type: String
            Source name
        *filterName*
            type: String
            Source filter name
    :Returns:
        *enabled*
            type: Boolean
            Filter status (enabled or not)
        *type*
            type: String
            Filter type
        *name*
            type: String
            Filter name
        *settings*
            type: Object
            Filter settings
    """

    name = 'GetSourceFilterInfo'
    category = 'sources'
    fields = [
        'sourceName',
        'filterName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['enabled'] = None
        self.datain['type'] = None
        self.datain['name'] = None
        self.datain['settings'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['filterName'] = None

    @staticmethod
    def payload(sourceName, filterName):
        payload = {}
        payload['request-type'] = 'GetSourceFilterInfo'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.filterName.set_data(data['filterName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'filterName': self.filterName.get_data(),
            }


class AddFilterToSource(BaseRequest):
    """Add a new filter to a source. Available source types along with their settings properties are available from `GetSourceTypesList`.

    :Arguments:
        *sourceName*
            type: String
            Name of the source on which the filter is added
        *filterName*
            type: String
            Name of the new filter
        *filterType*
            type: String
            Filter type
        *filterSettings*
            type: Object
            Filter settings
    """

    name = 'AddFilterToSource'
    category = 'sources'
    fields = [
        'sourceName',
        'filterName',
        'filterType',
        'filterSettings',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['filterName'] = None
        self.dataout['filterType'] = None
        self.dataout['filterSettings'] = None

    @staticmethod
    def payload(sourceName, filterName, filterType, filterSettings):
        payload = {}
        payload['request-type'] = 'AddFilterToSource'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterType'] = filterType
        payload['filterSettings'] = filterSettings
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.filterName.set_data(data['filterName']) 
            self.filterType.set_data(data['filterType']) 
            self.filterSettings.set_data(data['filterSettings']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'filterName': self.filterName.get_data(),
                'filterType': self.filterType.get_data(),
                'filterSettings': self.filterSettings.get_data(),
            }


class RemoveFilterFromSource(BaseRequest):
    """Remove a filter from a source

    :Arguments:
        *sourceName*
            type: String
            Name of the source from which the specified filter is removed
        *filterName*
            type: String
            Name of the filter to remove
    """

    name = 'RemoveFilterFromSource'
    category = 'sources'
    fields = [
        'sourceName',
        'filterName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['filterName'] = None

    @staticmethod
    def payload(sourceName, filterName):
        payload = {}
        payload['request-type'] = 'RemoveFilterFromSource'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.filterName.set_data(data['filterName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'filterName': self.filterName.get_data(),
            }


class ReorderSourceFilter(BaseRequest):
    """Move a filter in the chain (absolute index positioning)

    :Arguments:
        *sourceName*
            type: String
            Name of the source to which the filter belongs
        *filterName*
            type: String
            Name of the filter to reorder
        *newIndex*
            type: Integer
            Desired position of the filter in the chain
    """

    name = 'ReorderSourceFilter'
    category = 'sources'
    fields = [
        'sourceName',
        'filterName',
        'newIndex',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['filterName'] = None
        self.dataout['newIndex'] = None

    @staticmethod
    def payload(sourceName, filterName, newIndex):
        payload = {}
        payload['request-type'] = 'ReorderSourceFilter'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['newIndex'] = newIndex
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.filterName.set_data(data['filterName']) 
            self.newIndex.set_data(data['newIndex']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'filterName': self.filterName.get_data(),
                'newIndex': self.newIndex.get_data(),
            }


class MoveSourceFilter(BaseRequest):
    """Move a filter in the chain (relative positioning)

    :Arguments:
        *sourceName*
            type: String
            Name of the source to which the filter belongs
        *filterName*
            type: String
            Name of the filter to reorder
        *movementType*
            type: String
            How to move the filter around in the source's filter chain. Either "up", "down", "top" or "bottom".
    """

    name = 'MoveSourceFilter'
    category = 'sources'
    fields = [
        'sourceName',
        'filterName',
        'movementType',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['filterName'] = None
        self.dataout['movementType'] = None

    @staticmethod
    def payload(sourceName, filterName, movementType):
        payload = {}
        payload['request-type'] = 'MoveSourceFilter'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['movementType'] = movementType
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.filterName.set_data(data['filterName']) 
            self.movementType.set_data(data['movementType']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'filterName': self.filterName.get_data(),
                'movementType': self.movementType.get_data(),
            }


class SetSourceFilterSettings(BaseRequest):
    """Update settings of a filter

    :Arguments:
        *sourceName*
            type: String
            Name of the source to which the filter belongs
        *filterName*
            type: String
            Name of the filter to reconfigure
        *filterSettings*
            type: Object
            New settings. These will be merged to the current filter settings.
    """

    name = 'SetSourceFilterSettings'
    category = 'sources'
    fields = [
        'sourceName',
        'filterName',
        'filterSettings',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['filterName'] = None
        self.dataout['filterSettings'] = None

    @staticmethod
    def payload(sourceName, filterName, filterSettings):
        payload = {}
        payload['request-type'] = 'SetSourceFilterSettings'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterSettings'] = filterSettings
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.filterName.set_data(data['filterName']) 
            self.filterSettings.set_data(data['filterSettings']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'filterName': self.filterName.get_data(),
                'filterSettings': self.filterSettings.get_data(),
            }


class SetSourceFilterVisibility(BaseRequest):
    """Change the visibility/enabled state of a filter

    :Arguments:
        *sourceName*
            type: String
            Source name
        *filterName*
            type: String
            Source filter name
        *filterEnabled*
            type: Boolean
            New filter state
    """

    name = 'SetSourceFilterVisibility'
    category = 'sources'
    fields = [
        'sourceName',
        'filterName',
        'filterEnabled',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['filterName'] = None
        self.dataout['filterEnabled'] = None

    @staticmethod
    def payload(sourceName, filterName, filterEnabled):
        payload = {}
        payload['request-type'] = 'SetSourceFilterVisibility'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterEnabled'] = filterEnabled
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.filterName.set_data(data['filterName']) 
            self.filterEnabled.set_data(data['filterEnabled']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'filterName': self.filterName.get_data(),
                'filterEnabled': self.filterEnabled.get_data(),
            }


class GetAudioMonitorType(BaseRequest):
    """Get the audio monitoring type of the specified source.

    :Arguments:
        *sourceName*
            type: String
            Source name.
    :Returns:
        *monitorType*
            type: String
            The monitor type in use. Options: `none`, `monitorOnly`, `monitorAndOutput`.
    """

    name = 'GetAudioMonitorType'
    category = 'sources'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['monitorType'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetAudioMonitorType'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class SetAudioMonitorType(BaseRequest):
    """Set the audio monitoring type of the specified source.

    :Arguments:
        *sourceName*
            type: String
            Source name.
        *monitorType*
            type: String
            The monitor type to use. Options: `none`, `monitorOnly`, `monitorAndOutput`.
    """

    name = 'SetAudioMonitorType'
    category = 'sources'
    fields = [
        'sourceName',
        'monitorType',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['monitorType'] = None

    @staticmethod
    def payload(sourceName, monitorType):
        payload = {}
        payload['request-type'] = 'SetAudioMonitorType'
        payload['sourceName'] = sourceName
        payload['monitorType'] = monitorType
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.monitorType.set_data(data['monitorType']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'monitorType': self.monitorType.get_data(),
            }


class GetSourceDefaultSettings(BaseRequest):
    """Get the default settings for a given source type.

    :Arguments:
        *sourceKind*
            type: String
            Source kind. Also called "source id" in libobs terminology.
    :Returns:
        *sourceKind*
            type: String
            Source kind. Same value as the `sourceKind` parameter.
        *defaultSettings*
            type: Object
            Settings object for source.
    """

    name = 'GetSourceDefaultSettings'
    category = 'sources'
    fields = [
        'sourceKind',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceKind'] = None
        self.datain['defaultSettings'] = None
        self.dataout = {}
        self.dataout['sourceKind'] = None

    @staticmethod
    def payload(sourceKind):
        payload = {}
        payload['request-type'] = 'GetSourceDefaultSettings'
        payload['sourceKind'] = sourceKind
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceKind.set_data(data['sourceKind']) 

        def to_dict(self):
            return {
                'sourceKind': self.sourceKind.get_data(),
            }


class TakeSourceScreenshot(BaseRequest):
    """

At least `embedPictureFormat` or `saveToFilePath` must be specified.

Clients can specify `width` and `height` parameters to receive scaled pictures. Aspect ratio is
preserved if only one of these two parameters is specified.

    :Arguments:
        *sourceName*
            type: String (optional)
            Source name. Note: Since scenes are also sources, you can also provide a scene name. If not provided, the currently active scene is used.
        *embedPictureFormat*
            type: String (optional)
            Format of the Data URI encoded picture. Can be "png", "jpg", "jpeg" or "bmp" (or any other value supported by Qt's Image module)
        *saveToFilePath*
            type: String (optional)
            Full file path (file extension included) where the captured image is to be saved. Can be in a format different from `pictureFormat`. Can be a relative path.
        *fileFormat*
            type: String (optional)
            Format to save the image file as (one of the values provided in the `supported-image-export-formats` response field of `GetVersion`). If not specified, tries to guess based on file extension.
        *compressionQuality*
            type: int (optional)
            Compression ratio between -1 and 100 to write the image with. -1 is automatic, 1 is smallest file/most compression, 100 is largest file/least compression. Varies with image type.
        *width*
            type: int (optional)
            Screenshot width. Defaults to the source's base width.
        *height*
            type: int (optional)
            Screenshot height. Defaults to the source's base height.
    :Returns:
        *sourceName*
            type: String
            Source name
        *img*
            type: String
            Image Data URI (if `embedPictureFormat` was specified in the request)
        *imageFile*
            type: String
            Absolute path to the saved image file (if `saveToFilePath` was specified in the request)
    """

    name = 'TakeSourceScreenshot'
    category = 'sources'
    fields = [
        'sourceName',
        'embedPictureFormat',
        'saveToFilePath',
        'fileFormat',
        'compressionQuality',
        'width',
        'height',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['img'] = None
        self.datain['imageFile'] = None
        self.dataout = {}
        self.dataout['sourceName'] = None
        self.dataout['embedPictureFormat'] = None
        self.dataout['saveToFilePath'] = None
        self.dataout['fileFormat'] = None
        self.dataout['compressionQuality'] = None
        self.dataout['width'] = None
        self.dataout['height'] = None

    @staticmethod
    def payload(sourceName=None, embedPictureFormat=None, saveToFilePath=None, fileFormat=None, compressionQuality=None, width=None, height=None):
        payload = {}
        payload['request-type'] = 'TakeSourceScreenshot'
        payload['sourceName'] = sourceName
        payload['embedPictureFormat'] = embedPictureFormat
        payload['saveToFilePath'] = saveToFilePath
        payload['fileFormat'] = fileFormat
        payload['compressionQuality'] = compressionQuality
        payload['width'] = width
        payload['height'] = height
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 
            self.embedPictureFormat.set_data(data['embedPictureFormat']) 
            self.saveToFilePath.set_data(data['saveToFilePath']) 
            self.fileFormat.set_data(data['fileFormat']) 
            self.compressionQuality.set_data(data['compressionQuality']) 
            self.width.set_data(data['width']) 
            self.height.set_data(data['height']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
                'embedPictureFormat': self.embedPictureFormat.get_data(),
                'saveToFilePath': self.saveToFilePath.get_data(),
                'fileFormat': self.fileFormat.get_data(),
                'compressionQuality': self.compressionQuality.get_data(),
                'width': self.width.get_data(),
                'height': self.height.get_data(),
            }


class RefreshBrowserSource(BaseRequest):
    """Refreshes the specified browser source.

    :Arguments:
        *sourceName*
            type: String
            Source name.
    """

    name = 'RefreshBrowserSource'
    category = 'sources'
    fields = [
        'sourceName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'RefreshBrowserSource'
        payload['sourceName'] = sourceName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sourceName.set_data(data['sourceName']) 

        def to_dict(self):
            return {
                'sourceName': self.sourceName.get_data(),
            }


class ListOutputs(BaseRequest):
    """List existing outputs

    :Returns:
        *outputs*
            type: Array<Output>
            Outputs list
    """

    name = 'ListOutputs'
    category = 'outputs'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['outputs'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListOutputs'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetOutputInfo(BaseRequest):
    """Get information about a single output

    :Arguments:
        *outputName*
            type: String
            Output name
    :Returns:
        *outputInfo*
            type: Output
            Output info
    """

    name = 'GetOutputInfo'
    category = 'outputs'
    fields = [
        'outputName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['outputInfo'] = None
        self.dataout = {}
        self.dataout['outputName'] = None

    @staticmethod
    def payload(outputName):
        payload = {}
        payload['request-type'] = 'GetOutputInfo'
        payload['outputName'] = outputName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.outputName.set_data(data['outputName']) 

        def to_dict(self):
            return {
                'outputName': self.outputName.get_data(),
            }


class StartOutput(BaseRequest):
    """

Note: Controlling outputs is an experimental feature of obs-websocket. Some plugins which add outputs to OBS may not function properly when they are controlled in this way.

    :Arguments:
        *outputName*
            type: String
            Output name
    """

    name = 'StartOutput'
    category = 'outputs'
    fields = [
        'outputName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['outputName'] = None

    @staticmethod
    def payload(outputName):
        payload = {}
        payload['request-type'] = 'StartOutput'
        payload['outputName'] = outputName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.outputName.set_data(data['outputName']) 

        def to_dict(self):
            return {
                'outputName': self.outputName.get_data(),
            }


class StopOutput(BaseRequest):
    """

Note: Controlling outputs is an experimental feature of obs-websocket. Some plugins which add outputs to OBS may not function properly when they are controlled in this way.

    :Arguments:
        *outputName*
            type: String
            Output name
        *force*
            type: boolean (optional)
            Force stop (default: false)
    """

    name = 'StopOutput'
    category = 'outputs'
    fields = [
        'outputName',
        'force',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['outputName'] = None
        self.dataout['force'] = None

    @staticmethod
    def payload(outputName, force=None):
        payload = {}
        payload['request-type'] = 'StopOutput'
        payload['outputName'] = outputName
        payload['force'] = force
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.outputName.set_data(data['outputName']) 
            self.force.set_data(data['force']) 

        def to_dict(self):
            return {
                'outputName': self.outputName.get_data(),
                'force': self.force.get_data(),
            }


class SetCurrentProfile(BaseRequest):
    """Set the currently active profile.

    :Arguments:
        *profile_name*
            type: String
            Name of the desired profile.
    """

    name = 'SetCurrentProfile'
    category = 'profiles'
    fields = [
        'profile_name',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['profile_name'] = None

    @staticmethod
    def payload(profile_name):
        payload = {}
        payload['request-type'] = 'SetCurrentProfile'
        payload['profile-name'] = profile_name
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.profile_name.set_data(data['profile_name']) 

        def to_dict(self):
            return {
                'profile_name': self.profile_name.get_data(),
            }


class GetCurrentProfile(BaseRequest):
    """Get the name of the current profile.

    :Returns:
        *profile_name*
            type: String
            Name of the currently active profile.
    """

    name = 'GetCurrentProfile'
    category = 'profiles'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['profile-name'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentProfile'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ListProfiles(BaseRequest):
    """Get a list of available profiles.

    :Returns:
        *profiles*
            type: Array<Object>
            List of available profiles.
    """

    name = 'ListProfiles'
    category = 'profiles'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['profiles'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListProfiles'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetRecordingStatus(BaseRequest):
    """Get current recording status.

    :Returns:
        *isRecording*
            type: boolean
            Current recording status.
        *isRecordingPaused*
            type: boolean
            Whether the recording is paused or not.
        *recordTimecode*
            type: String (optional)
            Time elapsed since recording started (only present if currently recording).
        *recordingFilename*
            type: String (optional)
            Absolute path to the recording file (only present if currently recording).
    """

    name = 'GetRecordingStatus'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['isRecording'] = None
        self.datain['isRecordingPaused'] = None
        self.datain['recordTimecode'] = None
        self.datain['recordingFilename'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetRecordingStatus'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StartStopRecording(BaseRequest):
    """Toggle recording on or off (depending on the current recording state).

    """

    name = 'StartStopRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopRecording'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StartRecording(BaseRequest):
    """Start recording.
Will return an `error` if recording is already active.

    """

    name = 'StartRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartRecording'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StopRecording(BaseRequest):
    """Stop recording.
Will return an `error` if recording is not active.

    """

    name = 'StopRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopRecording'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class PauseRecording(BaseRequest):
    """Pause the current recording.
Returns an error if recording is not active or already paused.

    """

    name = 'PauseRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'PauseRecording'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ResumeRecording(BaseRequest):
    """Resume/unpause the current recording (if paused).
Returns an error if recording is not active or not paused.

    """

    name = 'ResumeRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ResumeRecording'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SetRecordingFolder(BaseRequest):
    """

Note: If `SetRecordingFolder` is called while a recording is
in progress, the change won't be applied immediately and will be
effective on the next recording.

    :Arguments:
        *rec_folder*
            type: String
            Path of the recording folder.
    """

    name = 'SetRecordingFolder'
    category = 'recording'
    fields = [
        'rec_folder',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['rec_folder'] = None

    @staticmethod
    def payload(rec_folder):
        payload = {}
        payload['request-type'] = 'SetRecordingFolder'
        payload['rec-folder'] = rec_folder
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.rec_folder.set_data(data['rec_folder']) 

        def to_dict(self):
            return {
                'rec_folder': self.rec_folder.get_data(),
            }


class GetRecordingFolder(BaseRequest):
    """Get the path of  the current recording folder.

    :Returns:
        *rec_folder*
            type: String
            Path of the recording folder.
    """

    name = 'GetRecordingFolder'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['rec-folder'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetRecordingFolder'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetReplayBufferStatus(BaseRequest):
    """Get the status of the OBS replay buffer.

    :Returns:
        *isReplayBufferActive*
            type: boolean
            Current recording status.
    """

    name = 'GetReplayBufferStatus'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['isReplayBufferActive'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetReplayBufferStatus'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StartStopReplayBuffer(BaseRequest):
    """Toggle the Replay Buffer on/off (depending on the current state of the replay buffer).

    """

    name = 'StartStopReplayBuffer'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopReplayBuffer'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StartReplayBuffer(BaseRequest):
    """Start recording into the Replay Buffer.
Will return an `error` if the Replay Buffer is already active or if the
"Save Replay Buffer" hotkey is not set in OBS' settings.
Setting this hotkey is mandatory, even when triggering saves only
through obs-websocket.

    """

    name = 'StartReplayBuffer'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartReplayBuffer'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StopReplayBuffer(BaseRequest):
    """Stop recording into the Replay Buffer.
Will return an `error` if the Replay Buffer is not active.

    """

    name = 'StopReplayBuffer'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopReplayBuffer'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SaveReplayBuffer(BaseRequest):
    """Flush and save the contents of the Replay Buffer to disk. This is
basically the same as triggering the "Save Replay Buffer" hotkey.
Will return an `error` if the Replay Buffer is not active.

    """

    name = 'SaveReplayBuffer'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SaveReplayBuffer'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SetCurrentSceneCollection(BaseRequest):
    """Change the active scene collection.

    :Arguments:
        *sc_name*
            type: String
            Name of the desired scene collection.
    """

    name = 'SetCurrentSceneCollection'
    category = 'scene collections'
    fields = [
        'sc_name',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sc_name'] = None

    @staticmethod
    def payload(sc_name):
        payload = {}
        payload['request-type'] = 'SetCurrentSceneCollection'
        payload['sc-name'] = sc_name
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sc_name.set_data(data['sc_name']) 

        def to_dict(self):
            return {
                'sc_name': self.sc_name.get_data(),
            }


class GetCurrentSceneCollection(BaseRequest):
    """Get the name of the current scene collection.

    :Returns:
        *sc_name*
            type: String
            Name of the currently active scene collection.
    """

    name = 'GetCurrentSceneCollection'
    category = 'scene collections'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sc-name'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentSceneCollection'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ListSceneCollections(BaseRequest):
    """List available scene collections

    :Returns:
        *scene_collections*
            type: Array<ScenesCollection>
            Scene collections list
    """

    name = 'ListSceneCollections'
    category = 'scene collections'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-collections'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListSceneCollections'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetSceneItemList(BaseRequest):
    """Get a list of all scene items in a scene.

    :Arguments:
        *sceneName*
            type: String (optional)
            Name of the scene to get the list of scene items from. Defaults to the current scene if not specified.
    :Returns:
        *sceneName*
            type: String
            Name of the requested (or current) scene
        *sceneItems*
            type: Array<Object>
            Array of scene items
    """

    name = 'GetSceneItemList'
    category = 'scene items'
    fields = [
        'sceneName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sceneName'] = None
        self.datain['sceneItems'] = None
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemList'
        payload['sceneName'] = sceneName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sceneName.set_data(data['sceneName']) 

        def to_dict(self):
            return {
                'sceneName': self.sceneName.get_data(),
            }


class GetSceneItemProperties(BaseRequest):
    """Gets the scene specific properties of the specified source item.
Coordinates are relative to the item's parent (the scene or group it belongs to).

    :Arguments:
        *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
        *item*
            type: String | Object
            Scene Item name (if this field is a string) or specification (if it is an object).
    :Returns:
        *name*
            type: String
            Scene Item name.
        *itemId*
            type: int
            Scene Item ID.
        *position*
            type: double
            The x position of the source from the left.
        *rotation*
            type: double
            The clockwise rotation of the item in degrees around the point of alignment.
        *scale*
            type: double
            The x-scale factor of the source.
        *crop*
            type: int
            The number of pixels cropped off the top of the source before scaling.
        *visible*
            type: bool
            If the source is visible.
        *muted*
            type: bool
            If the source is muted.
        *locked*
            type: bool
            If the source's transform is locked.
        *bounds*
            type: String
            Type of bounding box. Can be "OBS_BOUNDS_STRETCH", "OBS_BOUNDS_SCALE_INNER", "OBS_BOUNDS_SCALE_OUTER", "OBS_BOUNDS_SCALE_TO_WIDTH", "OBS_BOUNDS_SCALE_TO_HEIGHT", "OBS_BOUNDS_MAX_ONLY" or "OBS_BOUNDS_NONE".
        *sourceWidth*
            type: int
            Base width (without scaling) of the source
        *sourceHeight*
            type: int
            Base source (without scaling) of the source
        *width*
            type: double
            Scene item width (base source width multiplied by the horizontal scaling factor)
        *height*
            type: double
            Scene item height (base source height multiplied by the vertical scaling factor)
        *parentGroupName*
            type: String (optional)
            Name of the item's parent (if this item belongs to a group)
        *groupChildren*
            type: Array<SceneItemTransform> (optional)
            List of children (if this item is a group)
    """

    name = 'GetSceneItemProperties'
    category = 'scene items'
    fields = [
        'scene_name',
        'item',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['itemId'] = None
        self.datain['position'] = None
        self.datain['rotation'] = None
        self.datain['scale'] = None
        self.datain['crop'] = None
        self.datain['visible'] = None
        self.datain['muted'] = None
        self.datain['locked'] = None
        self.datain['bounds'] = None
        self.datain['sourceWidth'] = None
        self.datain['sourceHeight'] = None
        self.datain['width'] = None
        self.datain['height'] = None
        self.datain['parentGroupName'] = None
        self.datain['groupChildren'] = None
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['scene_name'] = None

    @staticmethod
    def payload(item, scene_name=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemProperties'
        payload['scene-name'] = scene_name
        payload['item'] = item
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 
            self.item.set_data(data['item']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
                'item': self.item.get_data(),
            }


class SetSceneItemProperties(BaseRequest):
    """Sets the scene specific properties of a source. Unspecified properties will remain unchanged.
Coordinates are relative to the item's parent (the scene or group it belongs to).

    :Arguments:
        *scene_name*
            type: String (optional)
            Name of the scene the source item belongs to. Defaults to the current scene.
        *item*
            type: String | Object
            Scene Item name (if this field is a string) or specification (if it is an object).
        *position*
            type: double (optional)
            The new x position of the source.
        *rotation*
            type: double (optional)
            The new clockwise rotation of the item in degrees.
        *scale*
            type: double (optional)
            The new x scale of the item.
        *crop*
            type: int (optional)
            The new amount of pixels cropped off the top of the source before scaling.
        *visible*
            type: bool (optional)
            The new visibility of the source. 'true' shows source, 'false' hides source.
        *locked*
            type: bool (optional)
            The new locked status of the source. 'true' keeps it in its current position, 'false' allows movement.
        *bounds*
            type: String (optional)
            The new bounds type of the source. Can be "OBS_BOUNDS_STRETCH", "OBS_BOUNDS_SCALE_INNER", "OBS_BOUNDS_SCALE_OUTER", "OBS_BOUNDS_SCALE_TO_WIDTH", "OBS_BOUNDS_SCALE_TO_HEIGHT", "OBS_BOUNDS_MAX_ONLY" or "OBS_BOUNDS_NONE".
    """

    name = 'SetSceneItemProperties'
    category = 'scene items'
    fields = [
        'scene_name',
        'item',
        'position',
        'rotation',
        'scale',
        'crop',
        'visible',
        'locked',
        'bounds',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['scene_name'] = None
        self.dataout['position'] = None
        self.dataout['rotation'] = None
        self.dataout['scale'] = None
        self.dataout['crop'] = None
        self.dataout['visible'] = None
        self.dataout['locked'] = None
        self.dataout['bounds'] = None

    @staticmethod
    def payload(item, scene_name=None, position=None, rotation=None, scale=None, crop=None, visible=None, locked=None, bounds=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemProperties'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['position'] = position
        payload['rotation'] = rotation
        payload['scale'] = scale
        payload['crop'] = crop
        payload['visible'] = visible
        payload['locked'] = locked
        payload['bounds'] = bounds
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
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

        def to_dict(self):
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


class ResetSceneItem(BaseRequest):
    """Reset a scene item.

    :Arguments:
        *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
        *item*
            type: String | Object
            Scene Item name (if this field is a string) or specification (if it is an object).
    """

    name = 'ResetSceneItem'
    category = 'scene items'
    fields = [
        'scene_name',
        'item',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['scene_name'] = None

    @staticmethod
    def payload(item, scene_name=None):
        payload = {}
        payload['request-type'] = 'ResetSceneItem'
        payload['scene-name'] = scene_name
        payload['item'] = item
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 
            self.item.set_data(data['item']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
                'item': self.item.get_data(),
            }


class SetSceneItemRender(BaseRequest):
    """Show or hide a specified source item in a specified scene.

    :Arguments:
        *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the currently active scene.
        *source*
            type: String (optional)
            Scene Item name.
        *item*
            type: int (optional)
            Scene Item id
        *render*
            type: boolean
            true = shown ; false = hidden
    """

    name = 'SetSceneItemRender'
    category = 'scene items'
    fields = [
        'scene_name',
        'source',
        'item',
        'render',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['render'] = None
        self.dataout['scene_name'] = None
        self.dataout['source'] = None
        self.dataout['item'] = None

    @staticmethod
    def payload(render, scene_name=None, source=None, item=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemRender'
        payload['scene-name'] = scene_name
        payload['source'] = source
        payload['item'] = item
        payload['render'] = render
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 
            self.source.set_data(data['source']) 
            self.item.set_data(data['item']) 
            self.render.set_data(data['render']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
                'source': self.source.get_data(),
                'item': self.item.get_data(),
                'render': self.render.get_data(),
            }


class SetSceneItemPosition(BaseRequest):
    """Sets the coordinates of a specified source item.

    :Arguments:
        *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
        *item*
            type: String
            Scene Item name.
        *x*
            type: double
            X coordinate.
        *y*
            type: double
            Y coordinate.
    """

    name = 'SetSceneItemPosition'
    category = 'scene items'
    fields = [
        'scene_name',
        'item',
        'x',
        'y',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['x'] = None
        self.dataout['y'] = None
        self.dataout['scene_name'] = None

    @staticmethod
    def payload(item, x, y, scene_name=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemPosition'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['x'] = x
        payload['y'] = y
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 
            self.item.set_data(data['item']) 
            self.x.set_data(data['x']) 
            self.y.set_data(data['y']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
                'item': self.item.get_data(),
                'x': self.x.get_data(),
                'y': self.y.get_data(),
            }


class SetSceneItemTransform(BaseRequest):
    """Set the transform of the specified source item.

    :Arguments:
        *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
        *item*
            type: String
            Scene Item name.
        *x_scale*
            type: double
            Width scale factor.
        *y_scale*
            type: double
            Height scale factor.
        *rotation*
            type: double
            Source item rotation (in degrees).
    """

    name = 'SetSceneItemTransform'
    category = 'scene items'
    fields = [
        'scene_name',
        'item',
        'x_scale',
        'y_scale',
        'rotation',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['x_scale'] = None
        self.dataout['y_scale'] = None
        self.dataout['rotation'] = None
        self.dataout['scene_name'] = None

    @staticmethod
    def payload(item, x_scale, y_scale, rotation, scene_name=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemTransform'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['x-scale'] = x_scale
        payload['y-scale'] = y_scale
        payload['rotation'] = rotation
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 
            self.item.set_data(data['item']) 
            self.x_scale.set_data(data['x_scale']) 
            self.y_scale.set_data(data['y_scale']) 
            self.rotation.set_data(data['rotation']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
                'item': self.item.get_data(),
                'x_scale': self.x_scale.get_data(),
                'y_scale': self.y_scale.get_data(),
                'rotation': self.rotation.get_data(),
            }


class SetSceneItemCrop(BaseRequest):
    """Sets the crop coordinates of the specified source item.

    :Arguments:
        *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
        *item*
            type: String
            Scene Item name.
        *top*
            type: int
            Pixel position of the top of the source item.
        *bottom*
            type: int
            Pixel position of the bottom of the source item.
        *left*
            type: int
            Pixel position of the left of the source item.
        *right*
            type: int
            Pixel position of the right of the source item.
    """

    name = 'SetSceneItemCrop'
    category = 'scene items'
    fields = [
        'scene_name',
        'item',
        'top',
        'bottom',
        'left',
        'right',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['top'] = None
        self.dataout['bottom'] = None
        self.dataout['left'] = None
        self.dataout['right'] = None
        self.dataout['scene_name'] = None

    @staticmethod
    def payload(item, top, bottom, left, right, scene_name=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemCrop'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['top'] = top
        payload['bottom'] = bottom
        payload['left'] = left
        payload['right'] = right
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 
            self.item.set_data(data['item']) 
            self.top.set_data(data['top']) 
            self.bottom.set_data(data['bottom']) 
            self.left.set_data(data['left']) 
            self.right.set_data(data['right']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
                'item': self.item.get_data(),
                'top': self.top.get_data(),
                'bottom': self.bottom.get_data(),
                'left': self.left.get_data(),
                'right': self.right.get_data(),
            }


class DeleteSceneItem(BaseRequest):
    """Deletes a scene item.

    :Arguments:
        *scene*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
        *item*
            type: Object
            Scene item to delete (required)
    """

    name = 'DeleteSceneItem'
    category = 'scene items'
    fields = [
        'scene',
        'item',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['scene'] = None

    @staticmethod
    def payload(item, scene=None):
        payload = {}
        payload['request-type'] = 'DeleteSceneItem'
        payload['scene'] = scene
        payload['item'] = item
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene.set_data(data['scene']) 
            self.item.set_data(data['item']) 

        def to_dict(self):
            return {
                'scene': self.scene.get_data(),
                'item': self.item.get_data(),
            }


class AddSceneItem(BaseRequest):
    """Creates a scene item in a scene. In other words, this is how you add a source into a scene.

    :Arguments:
        *sceneName*
            type: String
            Name of the scene to create the scene item in
        *sourceName*
            type: String
            Name of the source to be added
        *setVisible*
            type: boolean (optional)
            Whether to make the sceneitem visible on creation or not. Default `true`
    :Returns:
        *itemId*
            type: int
            Numerical ID of the created scene item
    """

    name = 'AddSceneItem'
    category = 'scene items'
    fields = [
        'sceneName',
        'sourceName',
        'setVisible',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['itemId'] = None
        self.dataout = {}
        self.dataout['sceneName'] = None
        self.dataout['sourceName'] = None
        self.dataout['setVisible'] = None

    @staticmethod
    def payload(sceneName, sourceName, setVisible=None):
        payload = {}
        payload['request-type'] = 'AddSceneItem'
        payload['sceneName'] = sceneName
        payload['sourceName'] = sourceName
        payload['setVisible'] = setVisible
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sceneName.set_data(data['sceneName']) 
            self.sourceName.set_data(data['sourceName']) 
            self.setVisible.set_data(data['setVisible']) 

        def to_dict(self):
            return {
                'sceneName': self.sceneName.get_data(),
                'sourceName': self.sourceName.get_data(),
                'setVisible': self.setVisible.get_data(),
            }


class DuplicateSceneItem(BaseRequest):
    """Duplicates a scene item.

    :Arguments:
        *fromScene*
            type: String (optional)
            Name of the scene to copy the item from. Defaults to the current scene.
        *toScene*
            type: String (optional)
            Name of the scene to create the item in. Defaults to the current scene.
        *item*
            type: Object
            Scene Item to duplicate from the source scene (required)
    :Returns:
        *scene*
            type: String
            Name of the scene where the new item was created
        *item*
            type: Object
            New item info
    """

    name = 'DuplicateSceneItem'
    category = 'scene items'
    fields = [
        'fromScene',
        'toScene',
        'item',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene'] = None
        self.datain['item'] = None
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['fromScene'] = None
        self.dataout['toScene'] = None

    @staticmethod
    def payload(item, fromScene=None, toScene=None):
        payload = {}
        payload['request-type'] = 'DuplicateSceneItem'
        payload['fromScene'] = fromScene
        payload['toScene'] = toScene
        payload['item'] = item
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.fromScene.set_data(data['fromScene']) 
            self.toScene.set_data(data['toScene']) 
            self.item.set_data(data['item']) 

        def to_dict(self):
            return {
                'fromScene': self.fromScene.get_data(),
                'toScene': self.toScene.get_data(),
                'item': self.item.get_data(),
            }


class SetCurrentScene(BaseRequest):
    """Switch to the specified scene.

    :Arguments:
        *scene_name*
            type: String
            Name of the scene to switch to.
    """

    name = 'SetCurrentScene'
    category = 'scenes'
    fields = [
        'scene_name',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['scene_name'] = None

    @staticmethod
    def payload(scene_name):
        payload = {}
        payload['request-type'] = 'SetCurrentScene'
        payload['scene-name'] = scene_name
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
            }


class GetCurrentScene(BaseRequest):
    """Get the current scene's name and source items.

    :Returns:
        *name*
            type: String
            Name of the currently active scene.
        *sources*
            type: Array<SceneItem>
            Ordered list of the current scene's source items.
    """

    name = 'GetCurrentScene'
    category = 'scenes'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['sources'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentScene'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetSceneList(BaseRequest):
    """Get a list of scenes in the currently active profile.

    :Returns:
        *current_scene*
            type: String
            Name of the currently active scene.
        *scenes*
            type: Array<Scene>
            Ordered list of the current profile's scenes (See [GetCurrentScene](#getcurrentscene) for more information).
    """

    name = 'GetSceneList'
    category = 'scenes'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['current-scene'] = None
        self.datain['scenes'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSceneList'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class CreateScene(BaseRequest):
    """Create a new scene scene.

    :Arguments:
        *sceneName*
            type: String
            Name of the scene to create.
    """

    name = 'CreateScene'
    category = 'scenes'
    fields = [
        'sceneName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'CreateScene'
        payload['sceneName'] = sceneName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sceneName.set_data(data['sceneName']) 

        def to_dict(self):
            return {
                'sceneName': self.sceneName.get_data(),
            }


class ReorderSceneItems(BaseRequest):
    """Changes the order of scene items in the requested scene.

    :Arguments:
        *scene*
            type: String (optional)
            Name of the scene to reorder (defaults to current).
        *items*
            type: Array<Scene>
            Ordered list of objects with name and/or id specified. Id preferred due to uniqueness per scene
    """

    name = 'ReorderSceneItems'
    category = 'scenes'
    fields = [
        'scene',
        'items',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['items'] = None
        self.dataout['scene'] = None

    @staticmethod
    def payload(items, scene=None):
        payload = {}
        payload['request-type'] = 'ReorderSceneItems'
        payload['scene'] = scene
        payload['items'] = items
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene.set_data(data['scene']) 
            self.items.set_data(data['items']) 

        def to_dict(self):
            return {
                'scene': self.scene.get_data(),
                'items': self.items.get_data(),
            }


class SetSceneTransitionOverride(BaseRequest):
    """Set a scene to use a specific transition override.

    :Arguments:
        *sceneName*
            type: String
            Name of the scene to switch to.
        *transitionName*
            type: String
            Name of the transition to use.
        *transitionDuration*
            type: int (Optional)
            Duration in milliseconds of the transition if transition is not fixed. Defaults to the current duration specified in the UI if there is no current override and this value is not given.
    """

    name = 'SetSceneTransitionOverride'
    category = 'scenes'
    fields = [
        'sceneName',
        'transitionName',
        'transitionDuration',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sceneName'] = None
        self.dataout['transitionName'] = None
        self.dataout['transitionDuration'] = None

    @staticmethod
    def payload(sceneName, transitionName, transitionDuration):
        payload = {}
        payload['request-type'] = 'SetSceneTransitionOverride'
        payload['sceneName'] = sceneName
        payload['transitionName'] = transitionName
        payload['transitionDuration'] = transitionDuration
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sceneName.set_data(data['sceneName']) 
            self.transitionName.set_data(data['transitionName']) 
            self.transitionDuration.set_data(data['transitionDuration']) 

        def to_dict(self):
            return {
                'sceneName': self.sceneName.get_data(),
                'transitionName': self.transitionName.get_data(),
                'transitionDuration': self.transitionDuration.get_data(),
            }


class RemoveSceneTransitionOverride(BaseRequest):
    """Remove any transition override on a scene.

    :Arguments:
        *sceneName*
            type: String
            Name of the scene to switch to.
    """

    name = 'RemoveSceneTransitionOverride'
    category = 'scenes'
    fields = [
        'sceneName',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'RemoveSceneTransitionOverride'
        payload['sceneName'] = sceneName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sceneName.set_data(data['sceneName']) 

        def to_dict(self):
            return {
                'sceneName': self.sceneName.get_data(),
            }


class GetSceneTransitionOverride(BaseRequest):
    """Get the current scene transition override.

    :Arguments:
        *sceneName*
            type: String
            Name of the scene to switch to.
    :Returns:
        *transitionName*
            type: String
            Name of the current overriding transition. Empty string if no override is set.
        *transitionDuration*
            type: int
            Transition duration. `-1` if no override is set.
    """

    name = 'GetSceneTransitionOverride'
    category = 'scenes'
    fields = [
        'sceneName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['transitionName'] = None
        self.datain['transitionDuration'] = None
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'GetSceneTransitionOverride'
        payload['sceneName'] = sceneName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.sceneName.set_data(data['sceneName']) 

        def to_dict(self):
            return {
                'sceneName': self.sceneName.get_data(),
            }


class GetStreamingStatus(BaseRequest):
    """Get current streaming and recording status.

    :Returns:
        *streaming*
            type: boolean
            Current streaming status.
        *recording*
            type: boolean
            Current recording status.
        *recording_paused*
            type: boolean
            If recording is paused.
        *preview_only*
            type: boolean
            Always false. Retrocompatibility with OBSRemote.
        *stream_timecode*
            type: String (optional)
            Time elapsed since streaming started (only present if currently streaming).
        *rec_timecode*
            type: String (optional)
            Time elapsed since recording started (only present if currently recording).
    """

    name = 'GetStreamingStatus'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['streaming'] = None
        self.datain['recording'] = None
        self.datain['recording-paused'] = None
        self.datain['preview-only'] = None
        self.datain['stream-timecode'] = None
        self.datain['rec-timecode'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStreamingStatus'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StartStopStreaming(BaseRequest):
    """Toggle streaming on or off (depending on the current stream state).

    """

    name = 'StartStopStreaming'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopStreaming'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StartStreaming(BaseRequest):
    """Start streaming.
Will return an `error` if streaming is already active.

    :Arguments:
        *stream*
            type: Object (optional)
            Special stream configuration. Note: these won't be saved to OBS' configuration.
    """

    name = 'StartStreaming'
    category = 'streaming'
    fields = [
        'stream',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['stream'] = None

    @staticmethod
    def payload(stream=None):
        payload = {}
        payload['request-type'] = 'StartStreaming'
        payload['stream'] = stream
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.stream.set_data(data['stream']) 

        def to_dict(self):
            return {
                'stream': self.stream.get_data(),
            }


class StopStreaming(BaseRequest):
    """Stop streaming.
Will return an `error` if streaming is not active.

    """

    name = 'StopStreaming'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopStreaming'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SetStreamSettings(BaseRequest):
    """Sets one or more attributes of the current streaming server settings. Any options not passed will remain unchanged. Returns the updated settings in response. If 'type' is different than the current streaming service type, all settings are required. Returns the full settings of the stream (the same as GetStreamSettings).

    :Arguments:
        *type*
            type: String
            The type of streaming service configuration, usually `rtmp_custom` or `rtmp_common`.
        *settings*
            type: Object
            The actual settings of the stream.
        *save*
            type: boolean
            Persist the settings to disk.
    """

    name = 'SetStreamSettings'
    category = 'streaming'
    fields = [
        'type',
        'settings',
        'save',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['type'] = None
        self.dataout['settings'] = None
        self.dataout['save'] = None

    @staticmethod
    def payload(type, settings, save):
        payload = {}
        payload['request-type'] = 'SetStreamSettings'
        payload['type'] = type
        payload['settings'] = settings
        payload['save'] = save
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.type.set_data(data['type']) 
            self.settings.set_data(data['settings']) 
            self.save.set_data(data['save']) 

        def to_dict(self):
            return {
                'type': self.type.get_data(),
                'settings': self.settings.get_data(),
                'save': self.save.get_data(),
            }


class GetStreamSettings(BaseRequest):
    """Get the current streaming server settings.

    :Returns:
        *type*
            type: String
            The type of streaming service configuration. Possible values: 'rtmp_custom' or 'rtmp_common'.
        *settings*
            type: Object
            Stream settings object.
    """

    name = 'GetStreamSettings'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['type'] = None
        self.datain['settings'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStreamSettings'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SaveStreamSettings(BaseRequest):
    """Save the current streaming server settings to disk.

    """

    name = 'SaveStreamSettings'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SaveStreamSettings'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SendCaptions(BaseRequest):
    """Send the provided text as embedded CEA-608 caption data.

    :Arguments:
        *text*
            type: String
            Captions text
    """

    name = 'SendCaptions'
    category = 'streaming'
    fields = [
        'text',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['text'] = None

    @staticmethod
    def payload(text):
        payload = {}
        payload['request-type'] = 'SendCaptions'
        payload['text'] = text
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.text.set_data(data['text']) 

        def to_dict(self):
            return {
                'text': self.text.get_data(),
            }


class GetStudioModeStatus(BaseRequest):
    """Indicates if Studio Mode is currently enabled.

    :Returns:
        *studio_mode*
            type: boolean
            Indicates if Studio Mode is enabled.
    """

    name = 'GetStudioModeStatus'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['studio-mode'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStudioModeStatus'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetPreviewScene(BaseRequest):
    """Get the name of the currently previewed scene and its list of sources.
Will return an `error` if Studio Mode is not enabled.

    :Returns:
        *name*
            type: String
            The name of the active preview scene.
        *sources*
            type: Array<SceneItem>

    """

    name = 'GetPreviewScene'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['sources'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetPreviewScene'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SetPreviewScene(BaseRequest):
    """Set the active preview scene.
Will return an `error` if Studio Mode is not enabled.

    :Arguments:
        *scene_name*
            type: String
            The name of the scene to preview.
    """

    name = 'SetPreviewScene'
    category = 'studio mode'
    fields = [
        'scene_name',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['scene_name'] = None

    @staticmethod
    def payload(scene_name):
        payload = {}
        payload['request-type'] = 'SetPreviewScene'
        payload['scene-name'] = scene_name
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.scene_name.set_data(data['scene_name']) 

        def to_dict(self):
            return {
                'scene_name': self.scene_name.get_data(),
            }


class TransitionToProgram(BaseRequest):
    """Transitions the currently previewed scene to the main output.
Will return an `error` if Studio Mode is not enabled.

    :Arguments:
        *with_transition*
            type: Object (optional)
            Change the active transition before switching scenes. Defaults to the active transition.
    """

    name = 'TransitionToProgram'
    category = 'studio mode'
    fields = [
        'with_transition',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['with_transition'] = None

    @staticmethod
    def payload(with_transition=None):
        payload = {}
        payload['request-type'] = 'TransitionToProgram'
        payload['with-transition'] = with_transition
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.with_transition.set_data(data['with_transition']) 

        def to_dict(self):
            return {
                'with_transition': self.with_transition.get_data(),
            }


class EnableStudioMode(BaseRequest):
    """Enables Studio Mode.

    """

    name = 'EnableStudioMode'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'EnableStudioMode'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class DisableStudioMode(BaseRequest):
    """Disables Studio Mode.

    """

    name = 'DisableStudioMode'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'DisableStudioMode'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ToggleStudioMode(BaseRequest):
    """Toggles Studio Mode (depending on the current state of studio mode).

    """

    name = 'ToggleStudioMode'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ToggleStudioMode'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetTransitionList(BaseRequest):
    """List of all transitions available in the frontend's dropdown menu.

    :Returns:
        *current_transition*
            type: String
            Name of the currently active transition.
        *transitions*
            type: Array<Object>
            List of transitions.
    """

    name = 'GetTransitionList'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['current-transition'] = None
        self.datain['transitions'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionList'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetCurrentTransition(BaseRequest):
    """Get the name of the currently selected transition in the frontend's dropdown menu.

    :Returns:
        *name*
            type: String
            Name of the selected transition.
        *duration*
            type: int (optional)
            Transition duration (in milliseconds) if supported by the transition.
    """

    name = 'GetCurrentTransition'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['duration'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentTransition'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SetCurrentTransition(BaseRequest):
    """Set the active transition.

    :Arguments:
        *transition_name*
            type: String
            The name of the transition.
    """

    name = 'SetCurrentTransition'
    category = 'transitions'
    fields = [
        'transition_name',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['transition_name'] = None

    @staticmethod
    def payload(transition_name):
        payload = {}
        payload['request-type'] = 'SetCurrentTransition'
        payload['transition-name'] = transition_name
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.transition_name.set_data(data['transition_name']) 

        def to_dict(self):
            return {
                'transition_name': self.transition_name.get_data(),
            }


class SetTransitionDuration(BaseRequest):
    """Set the duration of the currently selected transition if supported.

    :Arguments:
        *duration*
            type: int
            Desired duration of the transition (in milliseconds).
    """

    name = 'SetTransitionDuration'
    category = 'transitions'
    fields = [
        'duration',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['duration'] = None

    @staticmethod
    def payload(duration):
        payload = {}
        payload['request-type'] = 'SetTransitionDuration'
        payload['duration'] = duration
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.duration.set_data(data['duration']) 

        def to_dict(self):
            return {
                'duration': self.duration.get_data(),
            }


class GetTransitionDuration(BaseRequest):
    """Get the duration of the currently selected transition if supported.

    :Returns:
        *transition_duration*
            type: int
            Duration of the current transition (in milliseconds).
    """

    name = 'GetTransitionDuration'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['transition-duration'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionDuration'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetTransitionPosition(BaseRequest):
    """Get the position of the current transition.

    :Returns:
        *position*
            type: double
            current transition position. This value will be between 0.0 and 1.0. Note: Transition returns 1.0 when not active.
    """

    name = 'GetTransitionPosition'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['position'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionPosition'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class GetTransitionSettings(BaseRequest):
    """Get the current settings of a transition

    :Arguments:
        *transitionName*
            type: String
            Transition name
    :Returns:
        *transitionSettings*
            type: Object
            Current transition settings
    """

    name = 'GetTransitionSettings'
    category = 'transitions'
    fields = [
        'transitionName',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['transitionSettings'] = None
        self.dataout = {}
        self.dataout['transitionName'] = None

    @staticmethod
    def payload(transitionName):
        payload = {}
        payload['request-type'] = 'GetTransitionSettings'
        payload['transitionName'] = transitionName
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.transitionName.set_data(data['transitionName']) 

        def to_dict(self):
            return {
                'transitionName': self.transitionName.get_data(),
            }


class SetTransitionSettings(BaseRequest):
    """Change the current settings of a transition

    :Arguments:
        *transitionName*
            type: String
            Transition name
        *transitionSettings*
            type: Object
            Transition settings (they can be partial)
    :Returns:
        *transitionSettings*
            type: Object
            Updated transition settings
    """

    name = 'SetTransitionSettings'
    category = 'transitions'
    fields = [
        'transitionName',
        'transitionSettings',
    ]

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['transitionSettings'] = None
        self.dataout = {}
        self.dataout['transitionName'] = None
        self.dataout['transitionSettings'] = None

    @staticmethod
    def payload(transitionName, transitionSettings):
        payload = {}
        payload['request-type'] = 'SetTransitionSettings'
        payload['transitionName'] = transitionName
        payload['transitionSettings'] = transitionSettings
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.transitionName.set_data(data['transitionName']) 
            self.transitionSettings.set_data(data['transitionSettings']) 

        def to_dict(self):
            return {
                'transitionName': self.transitionName.get_data(),
                'transitionSettings': self.transitionSettings.get_data(),
            }


class ReleaseTBar(BaseRequest):
    """Release the T-Bar (like a user releasing their mouse button after moving it).
*YOU MUST CALL THIS if you called `SetTBarPosition` with the `release` parameter set to `false`.*

    """

    name = 'ReleaseTBar'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReleaseTBar'
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SetTBarPosition(BaseRequest):
    """

If your code needs to perform multiple successive T-Bar moves (e.g. : in an animation, or in response to a user moving a T-Bar control in your User Interface), set `release` to false and call `ReleaseTBar` later once the animation/interaction is over.

    :Arguments:
        *position*
            type: double
            T-Bar position. This value must be between 0.0 and 1.0.
        *release*
            type: boolean (optional)
            Whether or not the T-Bar gets released automatically after setting its new position (like a user releasing their mouse button after moving the T-Bar). Call `ReleaseTBar` manually if you set `release` to false. Defaults to true.
    """

    name = 'SetTBarPosition'
    category = 'transitions'
    fields = [
        'position',
        'release',
    ]

    def __init__(self):
        super().__init__()
        self.dataout = {}
        self.dataout['position'] = None
        self.dataout['release'] = None

    @staticmethod
    def payload(position, release=None):
        payload = {}
        payload['request-type'] = 'SetTBarPosition'
        payload['position'] = position
        payload['release'] = release
        return payload

    class Widget(QWidget):
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

        def from_dict(self, data):
            self._data = data
            self.position.set_data(data['position']) 
            self.release.set_data(data['release']) 

        def to_dict(self):
            return {
                'position': self.position.get_data(),
                'release': self.release.get_data(),
            }




unimplemented_fields = {
    "Authenticate": [
        {
            "original_name": "auth",
            "name": "auth",
            "type": "String",
            "description": "Response to the auth challenge (see \"Authentication\" for more information).",
            "optional": false
        }
    ],
    "SetFilenameFormatting": [
        {
            "original_name": "filename-formatting",
            "name": "filename_formatting",
            "type": "String",
            "description": "Filename formatting string to set.",
            "optional": false
        }
    ],
    "BroadcastCustomMessage": [
        {
            "original_name": "realm",
            "name": "realm",
            "type": "String",
            "description": "Identifier to be choosen by the client",
            "optional": false
        },
        {
            "original_name": "data",
            "name": "data",
            "type": "Object",
            "description": "User-defined data",
            "optional": false
        }
    ],
    "OpenProjector": [
        {
            "original_name": "type",
            "name": "type",
            "type": "String (Optional)",
            "description": "Type of projector: `Preview` (default), `Source`, `Scene`, `StudioProgram`, or `Multiview` (case insensitive).",
            "optional": false
        },
        {
            "original_name": "monitor",
            "name": "monitor",
            "type": "int (Optional)",
            "description": "Monitor to open the projector on. If -1 or omitted, opens a window.",
            "optional": false
        },
        {
            "original_name": "geometry",
            "name": "geometry",
            "type": "String (Optional)",
            "description": "Size and position of the projector window (only if monitor is -1). Encoded in Base64 using [Qt's geometry encoding](https://doc.qt.io/qt-5/qwidget.html#saveGeometry). Corresponds to OBS's saved projectors.",
            "optional": false
        },
        {
            "original_name": "name",
            "name": "name",
            "type": "String (Optional)",
            "description": "Name of the source or scene to be displayed (ignored for other projector types).",
            "optional": false
        }
    ],
    "TriggerHotkeyByName": [
        {
            "original_name": "hotkeyName",
            "name": "hotkeyName",
            "type": "String",
            "description": "Unique name of the hotkey, as defined when registering the hotkey (e.g. \"ReplayBuffer.Save\")",
            "optional": false
        }
    ],
    "TriggerHotkeyBySequence": [
        {
            "original_name": "keyId",
            "name": "keyId",
            "type": "String",
            "description": "Main key identifier (e.g. `OBS_KEY_A` for key \"A\"). Available identifiers [here](https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h)",
            "optional": false
        },
        {
            "original_name": "keyModifiers",
            "name": "keyModifiers",
            "type": "Object (Optional)",
            "description": "Optional key modifiers object. False entries can be ommitted",
            "optional": false
        }
    ],
    "ExecuteBatch": [
        {
            "original_name": "requests",
            "name": "requests",
            "type": "Array<Object>",
            "description": "Array of requests to perform. Executed in order.",
            "optional": false
        },
        {
            "original_name": "abortOnFail",
            "name": "abortOnFail",
            "type": "boolean (Optional)",
            "description": "Stop processing batch requests if one returns a failure.",
            "optional": false
        }
    ],
    "Sleep": [
        {
            "original_name": "sleepMillis",
            "name": "sleepMillis",
            "type": "int",
            "description": "Delay in milliseconds to wait before continuing.",
            "optional": false
        }
    ],
    "SetMediaTime": [
        {
            "original_name": "timestamp",
            "name": "timestamp",
            "type": "int",
            "description": "Milliseconds to set the timestamp to.",
            "optional": false
        }
    ],
    "ScrubMedia": [
        {
            "original_name": "timeOffset",
            "name": "timeOffset",
            "type": "int",
            "description": "Millisecond offset (positive or negative) to offset the current media position.",
            "optional": false
        }
    ],
    "CreateSource": [
        {
            "original_name": "sourceKind",
            "name": "sourceKind",
            "type": "String",
            "description": "Source kind, Eg. `vlc_source`.",
            "optional": false
        },
        {
            "original_name": "sourceSettings",
            "name": "sourceSettings",
            "type": "Object (optional)",
            "description": "Source settings data.",
            "optional": true
        },
        {
            "original_name": "setVisible",
            "name": "setVisible",
            "type": "boolean (optional)",
            "description": "Set the created SceneItem as visible or not. Defaults to true",
            "optional": true
        }
    ],
    "GetVolume": [
        {
            "original_name": "useDecibel",
            "name": "useDecibel",
            "type": "boolean (optional)",
            "description": "Output volume in decibels of attenuation instead of amplitude/mul.",
            "optional": true
        }
    ],
    "SetVolume": [
        {
            "original_name": "volume",
            "name": "volume",
            "type": "double",
            "description": "Desired volume. Must be between `0.0` and `20.0` for mul, and under 26.0 for dB. OBS will interpret dB values under -100.0 as Inf. Note: The OBS volume sliders only reach a maximum of 1.0mul/0.0dB, however OBS actually supports larger values.",
            "optional": false
        },
        {
            "original_name": "useDecibel",
            "name": "useDecibel",
            "type": "boolean (optional)",
            "description": "Interperet `volume` data as decibels instead of amplitude/mul.",
            "optional": true
        }
    ],
    "SetTracks": [
        {
            "original_name": "track",
            "name": "track",
            "type": "int",
            "description": "Audio tracks 1-6.",
            "optional": false
        }
    ],
    "SetSourceName": [
        {
            "original_name": "newName",
            "name": "newName",
            "type": "String",
            "description": "New source name.",
            "optional": false
        }
    ],
    "SetSyncOffset": [
        {
            "original_name": "offset",
            "name": "offset",
            "type": "int",
            "description": "The desired audio sync offset (in nanoseconds).",
            "optional": false
        }
    ],
    "GetSourceSettings": [
        {
            "original_name": "sourceType",
            "name": "sourceType",
            "type": "String (optional)",
            "description": "Type of the specified source. Useful for type-checking if you expect a specific settings schema.",
            "optional": true
        }
    ],
    "SetSourceSettings": [
        {
            "original_name": "sourceType",
            "name": "sourceType",
            "type": "String (optional)",
            "description": "Type of the specified source. Useful for type-checking to avoid settings a set of settings incompatible with the actual source's type.",
            "optional": true
        },
        {
            "original_name": "sourceSettings",
            "name": "sourceSettings",
            "type": "Object",
            "description": "Source settings (varies between source types, may require some probing around).",
            "optional": false
        }
    ],
    "SetTextGDIPlusProperties": [
        {
            "original_name": "align",
            "name": "align",
            "type": "String (optional)",
            "description": "Text Alignment (\"left\", \"center\", \"right\").",
            "optional": true
        },
        {
            "original_name": "bk_color",
            "name": "bk_color",
            "type": "int (optional)",
            "description": "Background color.",
            "optional": true
        },
        {
            "original_name": "bk_opacity",
            "name": "bk_opacity",
            "type": "int (optional)",
            "description": "Background opacity (0-100).",
            "optional": true
        },
        {
            "original_name": "chatlog",
            "name": "chatlog",
            "type": "boolean (optional)",
            "description": "Chat log.",
            "optional": true
        },
        {
            "original_name": "chatlog_lines",
            "name": "chatlog_lines",
            "type": "int (optional)",
            "description": "Chat log lines.",
            "optional": true
        },
        {
            "original_name": "color",
            "name": "color",
            "type": "int (optional)",
            "description": "Text color.",
            "optional": true
        },
        {
            "original_name": "extents",
            "name": "extents",
            "type": "boolean (optional)",
            "description": "Extents wrap.",
            "optional": true
        },
        {
            "original_name": "extents_cx",
            "name": "extents_cx",
            "type": "int (optional)",
            "description": "Extents cx.",
            "optional": true
        },
        {
            "original_name": "extents_cy",
            "name": "extents_cy",
            "type": "int (optional)",
            "description": "Extents cy.",
            "optional": true
        },
        {
            "original_name": "file",
            "name": "file",
            "type": "String (optional)",
            "description": "File path name.",
            "optional": true
        },
        {
            "original_name": "read_from_file",
            "name": "read_from_file",
            "type": "boolean (optional)",
            "description": "Read text from the specified file.",
            "optional": true
        },
        {
            "original_name": "font",
            "name": "font",
            "type": "Object (optional)",
            "description": "Holds data for the font. Ex: `\"font\": { \"face\": \"Arial\", \"flags\": 0, \"size\": 150, \"style\": \"\" }`",
            "optional": true
        },
        {
            "original_name": "gradient",
            "name": "gradient",
            "type": "boolean (optional)",
            "description": "Gradient enabled.",
            "optional": true
        },
        {
            "original_name": "gradient_color",
            "name": "gradient_color",
            "type": "int (optional)",
            "description": "Gradient color.",
            "optional": true
        },
        {
            "original_name": "gradient_dir",
            "name": "gradient_dir",
            "type": "float (optional)",
            "description": "Gradient direction.",
            "optional": true
        },
        {
            "original_name": "gradient_opacity",
            "name": "gradient_opacity",
            "type": "int (optional)",
            "description": "Gradient opacity (0-100).",
            "optional": true
        },
        {
            "original_name": "outline",
            "name": "outline",
            "type": "boolean (optional)",
            "description": "Outline.",
            "optional": true
        },
        {
            "original_name": "outline_color",
            "name": "outline_color",
            "type": "int (optional)",
            "description": "Outline color.",
            "optional": true
        },
        {
            "original_name": "outline_size",
            "name": "outline_size",
            "type": "int (optional)",
            "description": "Outline size.",
            "optional": true
        },
        {
            "original_name": "outline_opacity",
            "name": "outline_opacity",
            "type": "int (optional)",
            "description": "Outline opacity (0-100).",
            "optional": true
        },
        {
            "original_name": "text",
            "name": "text",
            "type": "String (optional)",
            "description": "Text content to be displayed.",
            "optional": true
        },
        {
            "original_name": "valign",
            "name": "valign",
            "type": "String (optional)",
            "description": "Text vertical alignment (\"top\", \"center\", \"bottom\").",
            "optional": true
        },
        {
            "original_name": "vertical",
            "name": "vertical",
            "type": "boolean (optional)",
            "description": "Vertical text enabled.",
            "optional": true
        },
        {
            "original_name": "render",
            "name": "render",
            "type": "boolean (optional)",
            "description": "Visibility of the scene item.",
            "optional": true
        }
    ],
    "SetTextFreetype2Properties": [
        {
            "original_name": "color1",
            "name": "color1",
            "type": "int (optional)",
            "description": "Gradient top color.",
            "optional": true
        },
        {
            "original_name": "color2",
            "name": "color2",
            "type": "int (optional)",
            "description": "Gradient bottom color.",
            "optional": true
        },
        {
            "original_name": "custom_width",
            "name": "custom_width",
            "type": "int (optional)",
            "description": "Custom width (0 to disable).",
            "optional": true
        },
        {
            "original_name": "drop_shadow",
            "name": "drop_shadow",
            "type": "boolean (optional)",
            "description": "Drop shadow.",
            "optional": true
        },
        {
            "original_name": "font",
            "name": "font",
            "type": "Object (optional)",
            "description": "Holds data for the font. Ex: `\"font\": { \"face\": \"Arial\", \"flags\": 0, \"size\": 150, \"style\": \"\" }`",
            "optional": true
        },
        {
            "original_name": "from_file",
            "name": "from_file",
            "type": "boolean (optional)",
            "description": "Read text from the specified file.",
            "optional": true
        },
        {
            "original_name": "log_mode",
            "name": "log_mode",
            "type": "boolean (optional)",
            "description": "Chat log.",
            "optional": true
        },
        {
            "original_name": "outline",
            "name": "outline",
            "type": "boolean (optional)",
            "description": "Outline.",
            "optional": true
        },
        {
            "original_name": "text",
            "name": "text",
            "type": "String (optional)",
            "description": "Text content to be displayed.",
            "optional": true
        },
        {
            "original_name": "text_file",
            "name": "text_file",
            "type": "String (optional)",
            "description": "File path.",
            "optional": true
        },
        {
            "original_name": "word_wrap",
            "name": "word_wrap",
            "type": "boolean (optional)",
            "description": "Word wrap.",
            "optional": true
        }
    ],
    "SetBrowserSourceProperties": [
        {
            "original_name": "is_local_file",
            "name": "is_local_file",
            "type": "boolean (optional)",
            "description": "Indicates that a local file is in use.",
            "optional": true
        },
        {
            "original_name": "local_file",
            "name": "local_file",
            "type": "String (optional)",
            "description": "file path.",
            "optional": true
        },
        {
            "original_name": "url",
            "name": "url",
            "type": "String (optional)",
            "description": "Url.",
            "optional": true
        },
        {
            "original_name": "css",
            "name": "css",
            "type": "String (optional)",
            "description": "CSS to inject.",
            "optional": true
        },
        {
            "original_name": "width",
            "name": "width",
            "type": "int (optional)",
            "description": "Width.",
            "optional": true
        },
        {
            "original_name": "height",
            "name": "height",
            "type": "int (optional)",
            "description": "Height.",
            "optional": true
        },
        {
            "original_name": "fps",
            "name": "fps",
            "type": "int (optional)",
            "description": "Framerate.",
            "optional": true
        },
        {
            "original_name": "shutdown",
            "name": "shutdown",
            "type": "boolean (optional)",
            "description": "Indicates whether the source should be shutdown when not visible.",
            "optional": true
        },
        {
            "original_name": "render",
            "name": "render",
            "type": "boolean (optional)",
            "description": "Visibility of the scene item.",
            "optional": true
        }
    ],
    "AddFilterToSource": [
        {
            "original_name": "filterType",
            "name": "filterType",
            "type": "String",
            "description": "Filter type",
            "optional": false
        },
        {
            "original_name": "filterSettings",
            "name": "filterSettings",
            "type": "Object",
            "description": "Filter settings",
            "optional": false
        }
    ],
    "ReorderSourceFilter": [
        {
            "original_name": "newIndex",
            "name": "newIndex",
            "type": "Integer",
            "description": "Desired position of the filter in the chain",
            "optional": false
        }
    ],
    "MoveSourceFilter": [
        {
            "original_name": "movementType",
            "name": "movementType",
            "type": "String",
            "description": "How to move the filter around in the source's filter chain. Either \"up\", \"down\", \"top\" or \"bottom\".",
            "optional": false
        }
    ],
    "SetSourceFilterSettings": [
        {
            "original_name": "filterSettings",
            "name": "filterSettings",
            "type": "Object",
            "description": "New settings. These will be merged to the current filter settings.",
            "optional": false
        }
    ],
    "SetAudioMonitorType": [
        {
            "original_name": "monitorType",
            "name": "monitorType",
            "type": "String",
            "description": "The monitor type to use. Options: `none`, `monitorOnly`, `monitorAndOutput`.",
            "optional": false
        }
    ],
    "GetSourceDefaultSettings": [
        {
            "original_name": "sourceKind",
            "name": "sourceKind",
            "type": "String",
            "description": "Source kind. Also called \"source id\" in libobs terminology.",
            "optional": false
        }
    ],
    "TakeSourceScreenshot": [
        {
            "original_name": "embedPictureFormat",
            "name": "embedPictureFormat",
            "type": "String (optional)",
            "description": "Format of the Data URI encoded picture. Can be \"png\", \"jpg\", \"jpeg\" or \"bmp\" (or any other value supported by Qt's Image module)",
            "optional": true
        },
        {
            "original_name": "saveToFilePath",
            "name": "saveToFilePath",
            "type": "String (optional)",
            "description": "Full file path (file extension included) where the captured image is to be saved. Can be in a format different from `pictureFormat`. Can be a relative path.",
            "optional": true
        },
        {
            "original_name": "fileFormat",
            "name": "fileFormat",
            "type": "String (optional)",
            "description": "Format to save the image file as (one of the values provided in the `supported-image-export-formats` response field of `GetVersion`). If not specified, tries to guess based on file extension.",
            "optional": true
        },
        {
            "original_name": "compressionQuality",
            "name": "compressionQuality",
            "type": "int (optional)",
            "description": "Compression ratio between -1 and 100 to write the image with. -1 is automatic, 1 is smallest file/most compression, 100 is largest file/least compression. Varies with image type.",
            "optional": true
        },
        {
            "original_name": "width",
            "name": "width",
            "type": "int (optional)",
            "description": "Screenshot width. Defaults to the source's base width.",
            "optional": true
        },
        {
            "original_name": "height",
            "name": "height",
            "type": "int (optional)",
            "description": "Screenshot height. Defaults to the source's base height.",
            "optional": true
        }
    ],
    "GetOutputInfo": [
        {
            "original_name": "outputName",
            "name": "outputName",
            "type": "String",
            "description": "Output name",
            "optional": false
        }
    ],
    "StartOutput": [
        {
            "original_name": "outputName",
            "name": "outputName",
            "type": "String",
            "description": "Output name",
            "optional": false
        }
    ],
    "StopOutput": [
        {
            "original_name": "outputName",
            "name": "outputName",
            "type": "String",
            "description": "Output name",
            "optional": false
        },
        {
            "original_name": "force",
            "name": "force",
            "type": "boolean (optional)",
            "description": "Force stop (default: false)",
            "optional": true
        }
    ],
    "SetCurrentProfile": [
        {
            "original_name": "profile-name",
            "name": "profile_name",
            "type": "String",
            "description": "Name of the desired profile.",
            "optional": false
        }
    ],
    "SetRecordingFolder": [
        {
            "original_name": "rec-folder",
            "name": "rec_folder",
            "type": "String",
            "description": "Path of the recording folder.",
            "optional": false
        }
    ],
    "SetCurrentSceneCollection": [
        {
            "original_name": "sc-name",
            "name": "sc_name",
            "type": "String",
            "description": "Name of the desired scene collection.",
            "optional": false
        }
    ],
    "GetSceneItemProperties": [
        {
            "original_name": "item",
            "name": "item",
            "type": "String | Object",
            "description": "Scene Item name (if this field is a string) or specification (if it is an object).",
            "optional": false
        }
    ],
    "SetSceneItemProperties": [
        {
            "original_name": "item",
            "name": "item",
            "type": "String | Object",
            "description": "Scene Item name (if this field is a string) or specification (if it is an object).",
            "optional": false
        },
        {
            "original_name": "position",
            "name": "position",
            "type": "double (optional)",
            "description": "The new x position of the source.",
            "optional": true
        },
        {
            "original_name": "rotation",
            "name": "rotation",
            "type": "double (optional)",
            "description": "The new clockwise rotation of the item in degrees.",
            "optional": true
        },
        {
            "original_name": "scale",
            "name": "scale",
            "type": "double (optional)",
            "description": "The new x scale of the item.",
            "optional": true
        },
        {
            "original_name": "crop",
            "name": "crop",
            "type": "int (optional)",
            "description": "The new amount of pixels cropped off the top of the source before scaling.",
            "optional": true
        },
        {
            "original_name": "visible",
            "name": "visible",
            "type": "bool (optional)",
            "description": "The new visibility of the source. 'true' shows source, 'false' hides source.",
            "optional": true
        },
        {
            "original_name": "locked",
            "name": "locked",
            "type": "bool (optional)",
            "description": "The new locked status of the source. 'true' keeps it in its current position, 'false' allows movement.",
            "optional": true
        },
        {
            "original_name": "bounds",
            "name": "bounds",
            "type": "String (optional)",
            "description": "The new bounds type of the source. Can be \"OBS_BOUNDS_STRETCH\", \"OBS_BOUNDS_SCALE_INNER\", \"OBS_BOUNDS_SCALE_OUTER\", \"OBS_BOUNDS_SCALE_TO_WIDTH\", \"OBS_BOUNDS_SCALE_TO_HEIGHT\", \"OBS_BOUNDS_MAX_ONLY\" or \"OBS_BOUNDS_NONE\".",
            "optional": true
        }
    ],
    "ResetSceneItem": [
        {
            "original_name": "item",
            "name": "item",
            "type": "String | Object",
            "description": "Scene Item name (if this field is a string) or specification (if it is an object).",
            "optional": false
        }
    ],
    "SetSceneItemRender": [
        {
            "original_name": "item",
            "name": "item",
            "type": "int (optional)",
            "description": "Scene Item id",
            "optional": true
        }
    ],
    "SetSceneItemPosition": [
        {
            "original_name": "item",
            "name": "item",
            "type": "String",
            "description": "Scene Item name.",
            "optional": false
        },
        {
            "original_name": "x",
            "name": "x",
            "type": "double",
            "description": "X coordinate.",
            "optional": false
        },
        {
            "original_name": "y",
            "name": "y",
            "type": "double",
            "description": "Y coordinate.",
            "optional": false
        }
    ],
    "SetSceneItemTransform": [
        {
            "original_name": "item",
            "name": "item",
            "type": "String",
            "description": "Scene Item name.",
            "optional": false
        },
        {
            "original_name": "x-scale",
            "name": "x_scale",
            "type": "double",
            "description": "Width scale factor.",
            "optional": false
        },
        {
            "original_name": "y-scale",
            "name": "y_scale",
            "type": "double",
            "description": "Height scale factor.",
            "optional": false
        },
        {
            "original_name": "rotation",
            "name": "rotation",
            "type": "double",
            "description": "Source item rotation (in degrees).",
            "optional": false
        }
    ],
    "SetSceneItemCrop": [
        {
            "original_name": "item",
            "name": "item",
            "type": "String",
            "description": "Scene Item name.",
            "optional": false
        },
        {
            "original_name": "top",
            "name": "top",
            "type": "int",
            "description": "Pixel position of the top of the source item.",
            "optional": false
        },
        {
            "original_name": "bottom",
            "name": "bottom",
            "type": "int",
            "description": "Pixel position of the bottom of the source item.",
            "optional": false
        },
        {
            "original_name": "left",
            "name": "left",
            "type": "int",
            "description": "Pixel position of the left of the source item.",
            "optional": false
        },
        {
            "original_name": "right",
            "name": "right",
            "type": "int",
            "description": "Pixel position of the right of the source item.",
            "optional": false
        }
    ],
    "DeleteSceneItem": [
        {
            "original_name": "scene",
            "name": "scene",
            "type": "String (optional)",
            "description": "Name of the scene the scene item belongs to. Defaults to the current scene.",
            "optional": true
        },
        {
            "original_name": "item",
            "name": "item",
            "type": "Object",
            "description": "Scene item to delete (required)",
            "optional": false
        }
    ],
    "AddSceneItem": [
        {
            "original_name": "setVisible",
            "name": "setVisible",
            "type": "boolean (optional)",
            "description": "Whether to make the sceneitem visible on creation or not. Default `true`",
            "optional": true
        }
    ],
    "DuplicateSceneItem": [
        {
            "original_name": "fromScene",
            "name": "fromScene",
            "type": "String (optional)",
            "description": "Name of the scene to copy the item from. Defaults to the current scene.",
            "optional": true
        },
        {
            "original_name": "toScene",
            "name": "toScene",
            "type": "String (optional)",
            "description": "Name of the scene to create the item in. Defaults to the current scene.",
            "optional": true
        },
        {
            "original_name": "item",
            "name": "item",
            "type": "Object",
            "description": "Scene Item to duplicate from the source scene (required)",
            "optional": false
        }
    ],
    "ReorderSceneItems": [
        {
            "original_name": "scene",
            "name": "scene",
            "type": "String (optional)",
            "description": "Name of the scene to reorder (defaults to current).",
            "optional": true
        },
        {
            "original_name": "items",
            "name": "items",
            "type": "Array<Scene>",
            "description": "Ordered list of objects with name and/or id specified. Id preferred due to uniqueness per scene",
            "optional": false
        }
    ],
    "SetSceneTransitionOverride": [
        {
            "original_name": "transitionName",
            "name": "transitionName",
            "type": "String",
            "description": "Name of the transition to use.",
            "optional": false
        },
        {
            "original_name": "transitionDuration",
            "name": "transitionDuration",
            "type": "int (Optional)",
            "description": "Duration in milliseconds of the transition if transition is not fixed. Defaults to the current duration specified in the UI if there is no current override and this value is not given.",
            "optional": false
        }
    ],
    "StartStreaming": [
        {
            "original_name": "stream",
            "name": "stream",
            "type": "Object (optional)",
            "description": "Special stream configuration. Note: these won't be saved to OBS' configuration.",
            "optional": true
        }
    ],
    "SetStreamSettings": [
        {
            "original_name": "type",
            "name": "type",
            "type": "String",
            "description": "The type of streaming service configuration, usually `rtmp_custom` or `rtmp_common`.",
            "optional": false
        },
        {
            "original_name": "settings",
            "name": "settings",
            "type": "Object",
            "description": "The actual settings of the stream.",
            "optional": false
        }
    ],
    "SendCaptions": [
        {
            "original_name": "text",
            "name": "text",
            "type": "String",
            "description": "Captions text",
            "optional": false
        }
    ],
    "TransitionToProgram": [
        {
            "original_name": "with-transition",
            "name": "with_transition",
            "type": "Object (optional)",
            "description": "Change the active transition before switching scenes. Defaults to the active transition.",
            "optional": true
        }
    ],
    "SetCurrentTransition": [
        {
            "original_name": "transition-name",
            "name": "transition_name",
            "type": "String",
            "description": "The name of the transition.",
            "optional": false
        }
    ],
    "SetTransitionDuration": [
        {
            "original_name": "duration",
            "name": "duration",
            "type": "int",
            "description": "Desired duration of the transition (in milliseconds).",
            "optional": false
        }
    ],
    "GetTransitionSettings": [
        {
            "original_name": "transitionName",
            "name": "transitionName",
            "type": "String",
            "description": "Transition name",
            "optional": false
        }
    ],
    "SetTransitionSettings": [
        {
            "original_name": "transitionName",
            "name": "transitionName",
            "type": "String",
            "description": "Transition name",
            "optional": false
        },
        {
            "original_name": "transitionSettings",
            "name": "transitionSettings",
            "type": "Object",
            "description": "Transition settings (they can be partial)",
            "optional": false
        }
    ],
    "SetTBarPosition": [
        {
            "original_name": "position",
            "name": "position",
            "type": "double",
            "description": "T-Bar position. This value must be between 0.0 and 1.0.",
            "optional": false
        },
        {
            "original_name": "release",
            "name": "release",
            "type": "boolean (optional)",
            "description": "Whether or not the T-Bar gets released automatically after setting its new position (like a user releasing their mouse button after moving the T-Bar). Call `ReleaseTBar` manually if you set `release` to false. Defaults to true.",
            "optional": true
        }
    ]
}