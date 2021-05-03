from stagehand.sandbox import Sandbox
from .obs_socket import ObsSocket


class BaseRequest:
    def __init__(self):
        pass


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetVersion'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetVersion'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetAuthRequired'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetAuthRequired'
        return payload


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

    def __call__(self, auth, cb=None):
        payload = {}
        payload['request-type'] = 'Authenticate'
        payload['auth'] = auth
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(auth):
        payload = {}
        payload['request-type'] = 'Authenticate'
        payload['auth'] = auth
        return payload


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

    def __call__(self, enable, cb=None):
        payload = {}
        payload['request-type'] = 'SetHeartbeat'
        payload['enable'] = enable
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(enable):
        payload = {}
        payload['request-type'] = 'SetHeartbeat'
        payload['enable'] = enable
        return payload


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

    def __call__(self, filename_formatting, cb=None):
        payload = {}
        payload['request-type'] = 'SetFilenameFormatting'
        payload['filename-formatting'] = filename_formatting
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(filename_formatting):
        payload = {}
        payload['request-type'] = 'SetFilenameFormatting'
        payload['filename-formatting'] = filename_formatting
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetFilenameFormatting'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetFilenameFormatting'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetStats'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStats'
        return payload


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

    def __call__(self, realm, data, cb=None):
        payload = {}
        payload['request-type'] = 'BroadcastCustomMessage'
        payload['realm'] = realm
        payload['data'] = data
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(realm, data):
        payload = {}
        payload['request-type'] = 'BroadcastCustomMessage'
        payload['realm'] = realm
        payload['data'] = data
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetVideoInfo'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetVideoInfo'
        return payload


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

    def __call__(self, type, monitor, geometry, name, cb=None):
        payload = {}
        payload['request-type'] = 'OpenProjector'
        payload['type'] = type
        payload['monitor'] = monitor
        payload['geometry'] = geometry
        payload['name'] = name
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(type, monitor, geometry, name):
        payload = {}
        payload['request-type'] = 'OpenProjector'
        payload['type'] = type
        payload['monitor'] = monitor
        payload['geometry'] = geometry
        payload['name'] = name
        return payload


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

    def __call__(self, hotkeyName, cb=None):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyByName'
        payload['hotkeyName'] = hotkeyName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(hotkeyName):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyByName'
        payload['hotkeyName'] = hotkeyName
        return payload


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

    def __call__(self, keyId, keyModifiers, cb=None):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyBySequence'
        payload['keyId'] = keyId
        payload['keyModifiers'] = keyModifiers
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(keyId, keyModifiers):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyBySequence'
        payload['keyId'] = keyId
        payload['keyModifiers'] = keyModifiers
        return payload


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

    def __call__(self, requests, abortOnFail, cb=None):
        payload = {}
        payload['request-type'] = 'ExecuteBatch'
        payload['requests'] = requests
        payload['abortOnFail'] = abortOnFail
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(requests, abortOnFail):
        payload = {}
        payload['request-type'] = 'ExecuteBatch'
        payload['requests'] = requests
        payload['abortOnFail'] = abortOnFail
        return payload


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

    def __call__(self, sleepMillis, cb=None):
        payload = {}
        payload['request-type'] = 'Sleep'
        payload['sleepMillis'] = sleepMillis
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sleepMillis):
        payload = {}
        payload['request-type'] = 'Sleep'
        payload['sleepMillis'] = sleepMillis
        return payload


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

    def __call__(self, sourceName, playPause, cb=None):
        payload = {}
        payload['request-type'] = 'PlayPauseMedia'
        payload['sourceName'] = sourceName
        payload['playPause'] = playPause
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, playPause):
        payload = {}
        payload['request-type'] = 'PlayPauseMedia'
        payload['sourceName'] = sourceName
        payload['playPause'] = playPause
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'RestartMedia'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'RestartMedia'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'StopMedia'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'StopMedia'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'NextMedia'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'NextMedia'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'PreviousMedia'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'PreviousMedia'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetMediaDuration'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaDuration'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetMediaTime'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaTime'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, timestamp, cb=None):
        payload = {}
        payload['request-type'] = 'SetMediaTime'
        payload['sourceName'] = sourceName
        payload['timestamp'] = timestamp
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, timestamp):
        payload = {}
        payload['request-type'] = 'SetMediaTime'
        payload['sourceName'] = sourceName
        payload['timestamp'] = timestamp
        return payload


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

    def __call__(self, sourceName, timeOffset, cb=None):
        payload = {}
        payload['request-type'] = 'ScrubMedia'
        payload['sourceName'] = sourceName
        payload['timeOffset'] = timeOffset
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, timeOffset):
        payload = {}
        payload['request-type'] = 'ScrubMedia'
        payload['sourceName'] = sourceName
        payload['timeOffset'] = timeOffset
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetMediaState'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaState'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetMediaSourcesList'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetMediaSourcesList'
        return payload


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

    def __call__(self, sourceName, sourceKind, sceneName, sourceSettings=None, setVisible=None, cb=None):
        payload = {}
        payload['request-type'] = 'CreateSource'
        payload['sourceName'] = sourceName
        payload['sourceKind'] = sourceKind
        payload['sceneName'] = sceneName
        payload['sourceSettings'] = sourceSettings
        payload['setVisible'] = setVisible
        ObsSocket().send(payload, cb)

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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetSourcesList'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSourcesList'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetSourceTypesList'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSourceTypesList'
        return payload


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

    def __call__(self, source, useDecibel=None, cb=None):
        payload = {}
        payload['request-type'] = 'GetVolume'
        payload['source'] = source
        payload['useDecibel'] = useDecibel
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source, useDecibel=None):
        payload = {}
        payload['request-type'] = 'GetVolume'
        payload['source'] = source
        payload['useDecibel'] = useDecibel
        return payload


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

    def __call__(self, source, volume, useDecibel=None, cb=None):
        payload = {}
        payload['request-type'] = 'SetVolume'
        payload['source'] = source
        payload['volume'] = volume
        payload['useDecibel'] = useDecibel
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source, volume, useDecibel=None):
        payload = {}
        payload['request-type'] = 'SetVolume'
        payload['source'] = source
        payload['volume'] = volume
        payload['useDecibel'] = useDecibel
        return payload


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

    def __call__(self, sourceName, track, active, cb=None):
        payload = {}
        payload['request-type'] = 'SetTracks'
        payload['sourceName'] = sourceName
        payload['track'] = track
        payload['active'] = active
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, track, active):
        payload = {}
        payload['request-type'] = 'SetTracks'
        payload['sourceName'] = sourceName
        payload['track'] = track
        payload['active'] = active
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetTracks'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetTracks'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, source, cb=None):
        payload = {}
        payload['request-type'] = 'GetMute'
        payload['source'] = source
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetMute'
        payload['source'] = source
        return payload


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

    def __call__(self, source, mute, cb=None):
        payload = {}
        payload['request-type'] = 'SetMute'
        payload['source'] = source
        payload['mute'] = mute
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source, mute):
        payload = {}
        payload['request-type'] = 'SetMute'
        payload['source'] = source
        payload['mute'] = mute
        return payload


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

    def __call__(self, source, cb=None):
        payload = {}
        payload['request-type'] = 'ToggleMute'
        payload['source'] = source
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'ToggleMute'
        payload['source'] = source
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetSourceActive'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetSourceActive'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetAudioActive'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetAudioActive'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, newName, cb=None):
        payload = {}
        payload['request-type'] = 'SetSourceName'
        payload['sourceName'] = sourceName
        payload['newName'] = newName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, newName):
        payload = {}
        payload['request-type'] = 'SetSourceName'
        payload['sourceName'] = sourceName
        payload['newName'] = newName
        return payload


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

    def __call__(self, source, offset, cb=None):
        payload = {}
        payload['request-type'] = 'SetSyncOffset'
        payload['source'] = source
        payload['offset'] = offset
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source, offset):
        payload = {}
        payload['request-type'] = 'SetSyncOffset'
        payload['source'] = source
        payload['offset'] = offset
        return payload


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

    def __call__(self, source, cb=None):
        payload = {}
        payload['request-type'] = 'GetSyncOffset'
        payload['source'] = source
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetSyncOffset'
        payload['source'] = source
        return payload


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

    def __call__(self, sourceName, sourceType=None, cb=None):
        payload = {}
        payload['request-type'] = 'GetSourceSettings'
        payload['sourceName'] = sourceName
        payload['sourceType'] = sourceType
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, sourceType=None):
        payload = {}
        payload['request-type'] = 'GetSourceSettings'
        payload['sourceName'] = sourceName
        payload['sourceType'] = sourceType
        return payload


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

    def __call__(self, sourceName, sourceSettings, sourceType=None, cb=None):
        payload = {}
        payload['request-type'] = 'SetSourceSettings'
        payload['sourceName'] = sourceName
        payload['sourceType'] = sourceType
        payload['sourceSettings'] = sourceSettings
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, sourceSettings, sourceType=None):
        payload = {}
        payload['request-type'] = 'SetSourceSettings'
        payload['sourceName'] = sourceName
        payload['sourceType'] = sourceType
        payload['sourceSettings'] = sourceSettings
        return payload


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

    def __call__(self, source, cb=None):
        payload = {}
        payload['request-type'] = 'GetTextGDIPlusProperties'
        payload['source'] = source
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetTextGDIPlusProperties'
        payload['source'] = source
        return payload


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

    def __call__(self, source, align=None, bk_color=None, bk_opacity=None, chatlog=None, chatlog_lines=None, color=None, extents=None, extents_cx=None, extents_cy=None, file=None, read_from_file=None, font=None, gradient=None, gradient_color=None, gradient_dir=None, gradient_opacity=None, outline=None, outline_color=None, outline_size=None, outline_opacity=None, text=None, valign=None, vertical=None, render=None, cb=None):
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
        ObsSocket().send(payload, cb)

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

    def __call__(self, source, cb=None):
        payload = {}
        payload['request-type'] = 'GetTextFreetype2Properties'
        payload['source'] = source
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetTextFreetype2Properties'
        payload['source'] = source
        return payload


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

    def __call__(self, source, color1=None, color2=None, custom_width=None, drop_shadow=None, font=None, from_file=None, log_mode=None, outline=None, text=None, text_file=None, word_wrap=None, cb=None):
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
        ObsSocket().send(payload, cb)

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

    def __call__(self, source, cb=None):
        payload = {}
        payload['request-type'] = 'GetBrowserSourceProperties'
        payload['source'] = source
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetBrowserSourceProperties'
        payload['source'] = source
        return payload


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

    def __call__(self, source, is_local_file=None, local_file=None, url=None, css=None, width=None, height=None, fps=None, shutdown=None, render=None, cb=None):
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
        ObsSocket().send(payload, cb)

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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetSpecialSources'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSpecialSources'
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetSourceFilters'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetSourceFilters'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, filterName, cb=None):
        payload = {}
        payload['request-type'] = 'GetSourceFilterInfo'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, filterName):
        payload = {}
        payload['request-type'] = 'GetSourceFilterInfo'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        return payload


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

    def __call__(self, sourceName, filterName, filterType, filterSettings, cb=None):
        payload = {}
        payload['request-type'] = 'AddFilterToSource'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterType'] = filterType
        payload['filterSettings'] = filterSettings
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, filterName, filterType, filterSettings):
        payload = {}
        payload['request-type'] = 'AddFilterToSource'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterType'] = filterType
        payload['filterSettings'] = filterSettings
        return payload


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

    def __call__(self, sourceName, filterName, cb=None):
        payload = {}
        payload['request-type'] = 'RemoveFilterFromSource'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, filterName):
        payload = {}
        payload['request-type'] = 'RemoveFilterFromSource'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        return payload


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

    def __call__(self, sourceName, filterName, newIndex, cb=None):
        payload = {}
        payload['request-type'] = 'ReorderSourceFilter'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['newIndex'] = newIndex
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, filterName, newIndex):
        payload = {}
        payload['request-type'] = 'ReorderSourceFilter'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['newIndex'] = newIndex
        return payload


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

    def __call__(self, sourceName, filterName, movementType, cb=None):
        payload = {}
        payload['request-type'] = 'MoveSourceFilter'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['movementType'] = movementType
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, filterName, movementType):
        payload = {}
        payload['request-type'] = 'MoveSourceFilter'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['movementType'] = movementType
        return payload


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

    def __call__(self, sourceName, filterName, filterSettings, cb=None):
        payload = {}
        payload['request-type'] = 'SetSourceFilterSettings'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterSettings'] = filterSettings
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, filterName, filterSettings):
        payload = {}
        payload['request-type'] = 'SetSourceFilterSettings'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterSettings'] = filterSettings
        return payload


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

    def __call__(self, sourceName, filterName, filterEnabled, cb=None):
        payload = {}
        payload['request-type'] = 'SetSourceFilterVisibility'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterEnabled'] = filterEnabled
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, filterName, filterEnabled):
        payload = {}
        payload['request-type'] = 'SetSourceFilterVisibility'
        payload['sourceName'] = sourceName
        payload['filterName'] = filterName
        payload['filterEnabled'] = filterEnabled
        return payload


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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'GetAudioMonitorType'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetAudioMonitorType'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, sourceName, monitorType, cb=None):
        payload = {}
        payload['request-type'] = 'SetAudioMonitorType'
        payload['sourceName'] = sourceName
        payload['monitorType'] = monitorType
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName, monitorType):
        payload = {}
        payload['request-type'] = 'SetAudioMonitorType'
        payload['sourceName'] = sourceName
        payload['monitorType'] = monitorType
        return payload


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

    def __call__(self, sourceKind, cb=None):
        payload = {}
        payload['request-type'] = 'GetSourceDefaultSettings'
        payload['sourceKind'] = sourceKind
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceKind):
        payload = {}
        payload['request-type'] = 'GetSourceDefaultSettings'
        payload['sourceKind'] = sourceKind
        return payload


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

    def __call__(self, sourceName=None, embedPictureFormat=None, saveToFilePath=None, fileFormat=None, compressionQuality=None, width=None, height=None, cb=None):
        payload = {}
        payload['request-type'] = 'TakeSourceScreenshot'
        payload['sourceName'] = sourceName
        payload['embedPictureFormat'] = embedPictureFormat
        payload['saveToFilePath'] = saveToFilePath
        payload['fileFormat'] = fileFormat
        payload['compressionQuality'] = compressionQuality
        payload['width'] = width
        payload['height'] = height
        ObsSocket().send(payload, cb)

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

    def __call__(self, sourceName, cb=None):
        payload = {}
        payload['request-type'] = 'RefreshBrowserSource'
        payload['sourceName'] = sourceName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'RefreshBrowserSource'
        payload['sourceName'] = sourceName
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'ListOutputs'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListOutputs'
        return payload


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

    def __call__(self, outputName, cb=None):
        payload = {}
        payload['request-type'] = 'GetOutputInfo'
        payload['outputName'] = outputName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(outputName):
        payload = {}
        payload['request-type'] = 'GetOutputInfo'
        payload['outputName'] = outputName
        return payload


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

    def __call__(self, outputName, cb=None):
        payload = {}
        payload['request-type'] = 'StartOutput'
        payload['outputName'] = outputName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(outputName):
        payload = {}
        payload['request-type'] = 'StartOutput'
        payload['outputName'] = outputName
        return payload


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

    def __call__(self, outputName, force=None, cb=None):
        payload = {}
        payload['request-type'] = 'StopOutput'
        payload['outputName'] = outputName
        payload['force'] = force
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(outputName, force=None):
        payload = {}
        payload['request-type'] = 'StopOutput'
        payload['outputName'] = outputName
        payload['force'] = force
        return payload


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

    def __call__(self, profile_name, cb=None):
        payload = {}
        payload['request-type'] = 'SetCurrentProfile'
        payload['profile-name'] = profile_name
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(profile_name):
        payload = {}
        payload['request-type'] = 'SetCurrentProfile'
        payload['profile-name'] = profile_name
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetCurrentProfile'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentProfile'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'ListProfiles'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListProfiles'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetRecordingStatus'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetRecordingStatus'
        return payload


class StartStopRecording(BaseRequest):
    """Toggle recording on or off (depending on the current recording state).

    """

    name = 'StartStopRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StartStopRecording'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopRecording'
        return payload


class StartRecording(BaseRequest):
    """Start recording.
Will return an `error` if recording is already active.

    """

    name = 'StartRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StartRecording'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartRecording'
        return payload


class StopRecording(BaseRequest):
    """Stop recording.
Will return an `error` if recording is not active.

    """

    name = 'StopRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StopRecording'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopRecording'
        return payload


class PauseRecording(BaseRequest):
    """Pause the current recording.
Returns an error if recording is not active or already paused.

    """

    name = 'PauseRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'PauseRecording'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'PauseRecording'
        return payload


class ResumeRecording(BaseRequest):
    """Resume/unpause the current recording (if paused).
Returns an error if recording is not active or not paused.

    """

    name = 'ResumeRecording'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'ResumeRecording'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ResumeRecording'
        return payload


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

    def __call__(self, rec_folder, cb=None):
        payload = {}
        payload['request-type'] = 'SetRecordingFolder'
        payload['rec-folder'] = rec_folder
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(rec_folder):
        payload = {}
        payload['request-type'] = 'SetRecordingFolder'
        payload['rec-folder'] = rec_folder
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetRecordingFolder'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetRecordingFolder'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetReplayBufferStatus'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetReplayBufferStatus'
        return payload


class StartStopReplayBuffer(BaseRequest):
    """Toggle the Replay Buffer on/off (depending on the current state of the replay buffer).

    """

    name = 'StartStopReplayBuffer'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StartStopReplayBuffer'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopReplayBuffer'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StartReplayBuffer'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartReplayBuffer'
        return payload


class StopReplayBuffer(BaseRequest):
    """Stop recording into the Replay Buffer.
Will return an `error` if the Replay Buffer is not active.

    """

    name = 'StopReplayBuffer'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StopReplayBuffer'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopReplayBuffer'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'SaveReplayBuffer'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SaveReplayBuffer'
        return payload


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

    def __call__(self, sc_name, cb=None):
        payload = {}
        payload['request-type'] = 'SetCurrentSceneCollection'
        payload['sc-name'] = sc_name
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sc_name):
        payload = {}
        payload['request-type'] = 'SetCurrentSceneCollection'
        payload['sc-name'] = sc_name
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetCurrentSceneCollection'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentSceneCollection'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'ListSceneCollections'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListSceneCollections'
        return payload


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

    def __call__(self, sceneName=None, cb=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemList'
        payload['sceneName'] = sceneName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sceneName=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemList'
        payload['sceneName'] = sceneName
        return payload


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

    def __call__(self, item, scene_name=None, cb=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemProperties'
        payload['scene-name'] = scene_name
        payload['item'] = item
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(item, scene_name=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemProperties'
        payload['scene-name'] = scene_name
        payload['item'] = item
        return payload


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

    def __call__(self, item, scene_name=None, position=None, rotation=None, scale=None, crop=None, visible=None, locked=None, bounds=None, cb=None):
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
        ObsSocket().send(payload, cb)

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

    def __call__(self, item, scene_name=None, cb=None):
        payload = {}
        payload['request-type'] = 'ResetSceneItem'
        payload['scene-name'] = scene_name
        payload['item'] = item
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(item, scene_name=None):
        payload = {}
        payload['request-type'] = 'ResetSceneItem'
        payload['scene-name'] = scene_name
        payload['item'] = item
        return payload


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

    def __call__(self, render, scene_name=None, source=None, item=None, cb=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemRender'
        payload['scene-name'] = scene_name
        payload['source'] = source
        payload['item'] = item
        payload['render'] = render
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(render, scene_name=None, source=None, item=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemRender'
        payload['scene-name'] = scene_name
        payload['source'] = source
        payload['item'] = item
        payload['render'] = render
        return payload


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

    def __call__(self, item, x, y, scene_name=None, cb=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemPosition'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['x'] = x
        payload['y'] = y
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(item, x, y, scene_name=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemPosition'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['x'] = x
        payload['y'] = y
        return payload


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

    def __call__(self, item, x_scale, y_scale, rotation, scene_name=None, cb=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemTransform'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['x-scale'] = x_scale
        payload['y-scale'] = y_scale
        payload['rotation'] = rotation
        ObsSocket().send(payload, cb)

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

    def __call__(self, item, top, bottom, left, right, scene_name=None, cb=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemCrop'
        payload['scene-name'] = scene_name
        payload['item'] = item
        payload['top'] = top
        payload['bottom'] = bottom
        payload['left'] = left
        payload['right'] = right
        ObsSocket().send(payload, cb)

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

    def __call__(self, item, scene=None, cb=None):
        payload = {}
        payload['request-type'] = 'DeleteSceneItem'
        payload['scene'] = scene
        payload['item'] = item
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(item, scene=None):
        payload = {}
        payload['request-type'] = 'DeleteSceneItem'
        payload['scene'] = scene
        payload['item'] = item
        return payload


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

    def __call__(self, sceneName, sourceName, setVisible=None, cb=None):
        payload = {}
        payload['request-type'] = 'AddSceneItem'
        payload['sceneName'] = sceneName
        payload['sourceName'] = sourceName
        payload['setVisible'] = setVisible
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sceneName, sourceName, setVisible=None):
        payload = {}
        payload['request-type'] = 'AddSceneItem'
        payload['sceneName'] = sceneName
        payload['sourceName'] = sourceName
        payload['setVisible'] = setVisible
        return payload


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

    def __call__(self, item, fromScene=None, toScene=None, cb=None):
        payload = {}
        payload['request-type'] = 'DuplicateSceneItem'
        payload['fromScene'] = fromScene
        payload['toScene'] = toScene
        payload['item'] = item
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(item, fromScene=None, toScene=None):
        payload = {}
        payload['request-type'] = 'DuplicateSceneItem'
        payload['fromScene'] = fromScene
        payload['toScene'] = toScene
        payload['item'] = item
        return payload


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

    def __call__(self, scene_name, cb=None):
        payload = {}
        payload['request-type'] = 'SetCurrentScene'
        payload['scene-name'] = scene_name
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(scene_name):
        payload = {}
        payload['request-type'] = 'SetCurrentScene'
        payload['scene-name'] = scene_name
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetCurrentScene'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentScene'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetSceneList'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSceneList'
        return payload


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

    def __call__(self, sceneName, cb=None):
        payload = {}
        payload['request-type'] = 'CreateScene'
        payload['sceneName'] = sceneName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'CreateScene'
        payload['sceneName'] = sceneName
        return payload


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

    def __call__(self, items, scene=None, cb=None):
        payload = {}
        payload['request-type'] = 'ReorderSceneItems'
        payload['scene'] = scene
        payload['items'] = items
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(items, scene=None):
        payload = {}
        payload['request-type'] = 'ReorderSceneItems'
        payload['scene'] = scene
        payload['items'] = items
        return payload


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

    def __call__(self, sceneName, transitionName, transitionDuration, cb=None):
        payload = {}
        payload['request-type'] = 'SetSceneTransitionOverride'
        payload['sceneName'] = sceneName
        payload['transitionName'] = transitionName
        payload['transitionDuration'] = transitionDuration
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sceneName, transitionName, transitionDuration):
        payload = {}
        payload['request-type'] = 'SetSceneTransitionOverride'
        payload['sceneName'] = sceneName
        payload['transitionName'] = transitionName
        payload['transitionDuration'] = transitionDuration
        return payload


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

    def __call__(self, sceneName, cb=None):
        payload = {}
        payload['request-type'] = 'RemoveSceneTransitionOverride'
        payload['sceneName'] = sceneName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'RemoveSceneTransitionOverride'
        payload['sceneName'] = sceneName
        return payload


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

    def __call__(self, sceneName, cb=None):
        payload = {}
        payload['request-type'] = 'GetSceneTransitionOverride'
        payload['sceneName'] = sceneName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'GetSceneTransitionOverride'
        payload['sceneName'] = sceneName
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetStreamingStatus'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStreamingStatus'
        return payload


class StartStopStreaming(BaseRequest):
    """Toggle streaming on or off (depending on the current stream state).

    """

    name = 'StartStopStreaming'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StartStopStreaming'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopStreaming'
        return payload


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

    def __call__(self, stream=None, cb=None):
        payload = {}
        payload['request-type'] = 'StartStreaming'
        payload['stream'] = stream
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(stream=None):
        payload = {}
        payload['request-type'] = 'StartStreaming'
        payload['stream'] = stream
        return payload


class StopStreaming(BaseRequest):
    """Stop streaming.
Will return an `error` if streaming is not active.

    """

    name = 'StopStreaming'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'StopStreaming'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopStreaming'
        return payload


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

    def __call__(self, type, settings, save, cb=None):
        payload = {}
        payload['request-type'] = 'SetStreamSettings'
        payload['type'] = type
        payload['settings'] = settings
        payload['save'] = save
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(type, settings, save):
        payload = {}
        payload['request-type'] = 'SetStreamSettings'
        payload['type'] = type
        payload['settings'] = settings
        payload['save'] = save
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetStreamSettings'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStreamSettings'
        return payload


class SaveStreamSettings(BaseRequest):
    """Save the current streaming server settings to disk.

    """

    name = 'SaveStreamSettings'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'SaveStreamSettings'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SaveStreamSettings'
        return payload


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

    def __call__(self, text, cb=None):
        payload = {}
        payload['request-type'] = 'SendCaptions'
        payload['text'] = text
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(text):
        payload = {}
        payload['request-type'] = 'SendCaptions'
        payload['text'] = text
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetStudioModeStatus'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStudioModeStatus'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetPreviewScene'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetPreviewScene'
        return payload


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

    def __call__(self, scene_name, cb=None):
        payload = {}
        payload['request-type'] = 'SetPreviewScene'
        payload['scene-name'] = scene_name
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(scene_name):
        payload = {}
        payload['request-type'] = 'SetPreviewScene'
        payload['scene-name'] = scene_name
        return payload


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

    def __call__(self, with_transition=None, cb=None):
        payload = {}
        payload['request-type'] = 'TransitionToProgram'
        payload['with-transition'] = with_transition
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(with_transition=None):
        payload = {}
        payload['request-type'] = 'TransitionToProgram'
        payload['with-transition'] = with_transition
        return payload


class EnableStudioMode(BaseRequest):
    """Enables Studio Mode.

    """

    name = 'EnableStudioMode'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'EnableStudioMode'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'EnableStudioMode'
        return payload


class DisableStudioMode(BaseRequest):
    """Disables Studio Mode.

    """

    name = 'DisableStudioMode'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'DisableStudioMode'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'DisableStudioMode'
        return payload


class ToggleStudioMode(BaseRequest):
    """Toggles Studio Mode (depending on the current state of studio mode).

    """

    name = 'ToggleStudioMode'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'ToggleStudioMode'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ToggleStudioMode'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetTransitionList'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionList'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetCurrentTransition'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentTransition'
        return payload


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

    def __call__(self, transition_name, cb=None):
        payload = {}
        payload['request-type'] = 'SetCurrentTransition'
        payload['transition-name'] = transition_name
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(transition_name):
        payload = {}
        payload['request-type'] = 'SetCurrentTransition'
        payload['transition-name'] = transition_name
        return payload


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

    def __call__(self, duration, cb=None):
        payload = {}
        payload['request-type'] = 'SetTransitionDuration'
        payload['duration'] = duration
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(duration):
        payload = {}
        payload['request-type'] = 'SetTransitionDuration'
        payload['duration'] = duration
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetTransitionDuration'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionDuration'
        return payload


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

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'GetTransitionPosition'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionPosition'
        return payload


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

    def __call__(self, transitionName, cb=None):
        payload = {}
        payload['request-type'] = 'GetTransitionSettings'
        payload['transitionName'] = transitionName
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(transitionName):
        payload = {}
        payload['request-type'] = 'GetTransitionSettings'
        payload['transitionName'] = transitionName
        return payload


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

    def __call__(self, transitionName, transitionSettings, cb=None):
        payload = {}
        payload['request-type'] = 'SetTransitionSettings'
        payload['transitionName'] = transitionName
        payload['transitionSettings'] = transitionSettings
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(transitionName, transitionSettings):
        payload = {}
        payload['request-type'] = 'SetTransitionSettings'
        payload['transitionName'] = transitionName
        payload['transitionSettings'] = transitionSettings
        return payload


class ReleaseTBar(BaseRequest):
    """Release the T-Bar (like a user releasing their mouse button after moving it).
*YOU MUST CALL THIS if you called `SetTBarPosition` with the `release` parameter set to `false`.*

    """

    name = 'ReleaseTBar'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()

    def __call__(self, cb=None):
        payload = {}
        payload['request-type'] = 'ReleaseTBar'
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReleaseTBar'
        return payload


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

    def __call__(self, position, release=None, cb=None):
        payload = {}
        payload['request-type'] = 'SetTBarPosition'
        payload['position'] = position
        payload['release'] = release
        ObsSocket().send(payload, cb)

    @staticmethod
    def payload(position, release=None):
        payload = {}
        payload['request-type'] = 'SetTBarPosition'
        payload['position'] = position
        payload['release'] = release
        return payload




requests = {
    'GetVersion': GetVersion(),
    'GetAuthRequired': GetAuthRequired(),
    'Authenticate': Authenticate(),
    'SetHeartbeat': SetHeartbeat(),
    'SetFilenameFormatting': SetFilenameFormatting(),
    'GetFilenameFormatting': GetFilenameFormatting(),
    'GetStats': GetStats(),
    'BroadcastCustomMessage': BroadcastCustomMessage(),
    'GetVideoInfo': GetVideoInfo(),
    'OpenProjector': OpenProjector(),
    'TriggerHotkeyByName': TriggerHotkeyByName(),
    'TriggerHotkeyBySequence': TriggerHotkeyBySequence(),
    'ExecuteBatch': ExecuteBatch(),
    'Sleep': Sleep(),
    'PlayPauseMedia': PlayPauseMedia(),
    'RestartMedia': RestartMedia(),
    'StopMedia': StopMedia(),
    'NextMedia': NextMedia(),
    'PreviousMedia': PreviousMedia(),
    'GetMediaDuration': GetMediaDuration(),
    'GetMediaTime': GetMediaTime(),
    'SetMediaTime': SetMediaTime(),
    'ScrubMedia': ScrubMedia(),
    'GetMediaState': GetMediaState(),
    'GetMediaSourcesList': GetMediaSourcesList(),
    'CreateSource': CreateSource(),
    'GetSourcesList': GetSourcesList(),
    'GetSourceTypesList': GetSourceTypesList(),
    'GetVolume': GetVolume(),
    'SetVolume': SetVolume(),
    'SetTracks': SetTracks(),
    'GetTracks': GetTracks(),
    'GetMute': GetMute(),
    'SetMute': SetMute(),
    'ToggleMute': ToggleMute(),
    'GetSourceActive': GetSourceActive(),
    'GetAudioActive': GetAudioActive(),
    'SetSourceName': SetSourceName(),
    'SetSyncOffset': SetSyncOffset(),
    'GetSyncOffset': GetSyncOffset(),
    'GetSourceSettings': GetSourceSettings(),
    'SetSourceSettings': SetSourceSettings(),
    'GetTextGDIPlusProperties': GetTextGDIPlusProperties(),
    'SetTextGDIPlusProperties': SetTextGDIPlusProperties(),
    'GetTextFreetype2Properties': GetTextFreetype2Properties(),
    'SetTextFreetype2Properties': SetTextFreetype2Properties(),
    'GetBrowserSourceProperties': GetBrowserSourceProperties(),
    'SetBrowserSourceProperties': SetBrowserSourceProperties(),
    'GetSpecialSources': GetSpecialSources(),
    'GetSourceFilters': GetSourceFilters(),
    'GetSourceFilterInfo': GetSourceFilterInfo(),
    'AddFilterToSource': AddFilterToSource(),
    'RemoveFilterFromSource': RemoveFilterFromSource(),
    'ReorderSourceFilter': ReorderSourceFilter(),
    'MoveSourceFilter': MoveSourceFilter(),
    'SetSourceFilterSettings': SetSourceFilterSettings(),
    'SetSourceFilterVisibility': SetSourceFilterVisibility(),
    'GetAudioMonitorType': GetAudioMonitorType(),
    'SetAudioMonitorType': SetAudioMonitorType(),
    'GetSourceDefaultSettings': GetSourceDefaultSettings(),
    'TakeSourceScreenshot': TakeSourceScreenshot(),
    'RefreshBrowserSource': RefreshBrowserSource(),
    'ListOutputs': ListOutputs(),
    'GetOutputInfo': GetOutputInfo(),
    'StartOutput': StartOutput(),
    'StopOutput': StopOutput(),
    'SetCurrentProfile': SetCurrentProfile(),
    'GetCurrentProfile': GetCurrentProfile(),
    'ListProfiles': ListProfiles(),
    'GetRecordingStatus': GetRecordingStatus(),
    'StartStopRecording': StartStopRecording(),
    'StartRecording': StartRecording(),
    'StopRecording': StopRecording(),
    'PauseRecording': PauseRecording(),
    'ResumeRecording': ResumeRecording(),
    'SetRecordingFolder': SetRecordingFolder(),
    'GetRecordingFolder': GetRecordingFolder(),
    'GetReplayBufferStatus': GetReplayBufferStatus(),
    'StartStopReplayBuffer': StartStopReplayBuffer(),
    'StartReplayBuffer': StartReplayBuffer(),
    'StopReplayBuffer': StopReplayBuffer(),
    'SaveReplayBuffer': SaveReplayBuffer(),
    'SetCurrentSceneCollection': SetCurrentSceneCollection(),
    'GetCurrentSceneCollection': GetCurrentSceneCollection(),
    'ListSceneCollections': ListSceneCollections(),
    'GetSceneItemList': GetSceneItemList(),
    'GetSceneItemProperties': GetSceneItemProperties(),
    'SetSceneItemProperties': SetSceneItemProperties(),
    'ResetSceneItem': ResetSceneItem(),
    'SetSceneItemRender': SetSceneItemRender(),
    'SetSceneItemPosition': SetSceneItemPosition(),
    'SetSceneItemTransform': SetSceneItemTransform(),
    'SetSceneItemCrop': SetSceneItemCrop(),
    'DeleteSceneItem': DeleteSceneItem(),
    'AddSceneItem': AddSceneItem(),
    'DuplicateSceneItem': DuplicateSceneItem(),
    'SetCurrentScene': SetCurrentScene(),
    'GetCurrentScene': GetCurrentScene(),
    'GetSceneList': GetSceneList(),
    'CreateScene': CreateScene(),
    'ReorderSceneItems': ReorderSceneItems(),
    'SetSceneTransitionOverride': SetSceneTransitionOverride(),
    'RemoveSceneTransitionOverride': RemoveSceneTransitionOverride(),
    'GetSceneTransitionOverride': GetSceneTransitionOverride(),
    'GetStreamingStatus': GetStreamingStatus(),
    'StartStopStreaming': StartStopStreaming(),
    'StartStreaming': StartStreaming(),
    'StopStreaming': StopStreaming(),
    'SetStreamSettings': SetStreamSettings(),
    'GetStreamSettings': GetStreamSettings(),
    'SaveStreamSettings': SaveStreamSettings(),
    'SendCaptions': SendCaptions(),
    'GetStudioModeStatus': GetStudioModeStatus(),
    'GetPreviewScene': GetPreviewScene(),
    'SetPreviewScene': SetPreviewScene(),
    'TransitionToProgram': TransitionToProgram(),
    'EnableStudioMode': EnableStudioMode(),
    'DisableStudioMode': DisableStudioMode(),
    'ToggleStudioMode': ToggleStudioMode(),
    'GetTransitionList': GetTransitionList(),
    'GetCurrentTransition': GetCurrentTransition(),
    'SetCurrentTransition': SetCurrentTransition(),
    'SetTransitionDuration': SetTransitionDuration(),
    'GetTransitionDuration': GetTransitionDuration(),
    'GetTransitionPosition': GetTransitionPosition(),
    'GetTransitionSettings': GetTransitionSettings(),
    'SetTransitionSettings': SetTransitionSettings(),
    'ReleaseTBar': ReleaseTBar(),
    'SetTBarPosition': SetTBarPosition(),
}
