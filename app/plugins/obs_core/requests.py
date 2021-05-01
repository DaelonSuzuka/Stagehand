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

    fields = [
    ]

    category = 'general'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetVersion'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetVersion'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
    ]

    category = 'general'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetAuthRequired'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetAuthRequired'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class Authenticate(BaseRequest):
    """Attempt to authenticate the client to the server.

    :Arguments:
       *auth*
            type: String
            Response to the auth challenge (see "Authentication" for more information).
    """

    fields = [
        'auth',
    ]

    category = 'general'
    
    def __init__(self, auth):
        super().__init__()
        self.name = 'Authenticate'
        self.dataout = {}
        self.dataout['auth'] = None

    @staticmethod
    def payload(auth):
        payload = {}
        payload['request-type'] = 'Authenticate'
        payload['auth'] = auth
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('auth'))
        
        return w

class SetHeartbeat(BaseRequest):
    """Enable/disable sending of the Heartbeat event

    :Arguments:
       *enable*
            type: boolean
            Starts/Stops emitting heartbeat messages
    """

    fields = [
        'enable',
    ]

    category = 'general'
    
    def __init__(self, enable):
        super().__init__()
        self.name = 'SetHeartbeat'
        self.dataout = {}
        self.dataout['enable'] = None

    @staticmethod
    def payload(enable):
        payload = {}
        payload['request-type'] = 'SetHeartbeat'
        payload['enable'] = enable
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('enable'))
        
        return w

class SetFilenameFormatting(BaseRequest):
    """Set the filename formatting string

    :Arguments:
       *filename_formatting*
            type: String
            Filename formatting string to set.
    """

    fields = [
        'filename_formatting',
    ]

    category = 'general'
    
    def __init__(self, filename_formatting):
        super().__init__()
        self.name = 'SetFilenameFormatting'
        self.dataout = {}
        self.dataout['filename-formatting'] = None

    @staticmethod
    def payload(filename_formatting):
        payload = {}
        payload['request-type'] = 'SetFilenameFormatting'
        payload['filename_formatting'] = filename_formatting
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('filename_formatting'))
        
        return w

class GetFilenameFormatting(BaseRequest):
    """Get the filename formatting string

    :Returns:
       *filename_formatting*
            type: String
            Current filename formatting string.
    """

    fields = [
    ]

    category = 'general'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetFilenameFormatting'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetFilenameFormatting'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class GetStats(BaseRequest):
    """Get OBS stats (almost the same info as provided in OBS' stats window)

    :Returns:
       *stats*
            type: OBSStats
            [OBS stats](#obsstats)
    """

    fields = [
    ]

    category = 'general'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetStats'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStats'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'realm',
        'data',
    ]

    category = 'general'
    
    def __init__(self, realm, data):
        super().__init__()
        self.name = 'BroadcastCustomMessage'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('realm'))
            layout.add(QLabel('data'))
        
        return w

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

    fields = [
    ]

    category = 'general'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetVideoInfo'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetVideoInfo'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'type',
        'monitor',
        'geometry',
        'name',
    ]

    category = 'general'
    
    def __init__(self, type, monitor, geometry, name):
        super().__init__()
        self.name = 'OpenProjector'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('type'))
            layout.add(QLabel('monitor'))
            layout.add(QLabel('geometry'))
            layout.add(QLabel('name'))
        
        return w

class TriggerHotkeyByName(BaseRequest):
    """Executes hotkey routine, identified by hotkey unique name

    :Arguments:
       *hotkeyName*
            type: String
            Unique name of the hotkey, as defined when registering the hotkey (e.g. "ReplayBuffer.Save")
    """

    fields = [
        'hotkeyName',
    ]

    category = 'general'
    
    def __init__(self, hotkeyName):
        super().__init__()
        self.name = 'TriggerHotkeyByName'
        self.dataout = {}
        self.dataout['hotkeyName'] = None

    @staticmethod
    def payload(hotkeyName):
        payload = {}
        payload['request-type'] = 'TriggerHotkeyByName'
        payload['hotkeyName'] = hotkeyName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('hotkeyName'))
        
        return w

class TriggerHotkeyBySequence(BaseRequest):
    """Executes hotkey routine, identified by bound combination of keys. A single key combination might trigger multiple hotkey routines depending on user settings

    :Arguments:
       *keyId*
            type: String
            Main key identifier (e.g. `OBS_KEY_A` for key "A"). Available identifiers [here](https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h)
       *keyModifiers*
            type: Object (Optional)
            Optional key modifiers object. False entries can be ommitted
       *keyModifiers.shift*
            type: boolean
            Trigger Shift Key
       *keyModifiers.alt*
            type: boolean
            Trigger Alt Key
       *keyModifiers.control*
            type: boolean
            Trigger Control (Ctrl) Key
       *keyModifiers.command*
            type: boolean
            Trigger Command Key (Mac)
    """

    fields = [
        'keyId',
        'keyModifiers',
    ]

    category = 'general'
    
    def __init__(self, keyId, keyModifiers):
        super().__init__()
        self.name = 'TriggerHotkeyBySequence'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('keyId'))
            layout.add(QLabel('keyModifiers'))
        
        return w

class ExecuteBatch(BaseRequest):
    """Executes a list of requests sequentially (one-by-one on the same thread).

    :Arguments:
       *requests*
            type: Array<Object>
            Array of requests to perform. Executed in order.
       *requests.*.request_type*
            type: String
            Request type. Eg. `GetVersion`.
       *requests.*.message_id*
            type: String (Optional)
            ID of the individual request. Can be any string and not required to be unique. Defaults to empty string if not specified.
       *abortOnFail*
            type: boolean (Optional)
            Stop processing batch requests if one returns a failure.
    :Returns:
       *results*
            type: Array<Object>
            Batch requests results, ordered sequentially.
       *results.*.message_id*
            type: String
            ID of the individual request which was originally provided by the client.
       *results.*.status*
            type: String
            Status response as string. Either `ok` or `error`.
       *results.*.error*
            type: String (Optional)
            Error message accompanying an `error` status.
    """

    fields = [
        'requests',
        'abortOnFail',
    ]

    category = 'general'
    
    def __init__(self, requests, abortOnFail):
        super().__init__()
        self.name = 'ExecuteBatch'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('requests'))
            layout.add(QLabel('abortOnFail'))
        
        return w

class Sleep(BaseRequest):
    """Waits for the specified duration. Designed to be used in `ExecuteBatch` operations.

    :Arguments:
       *sleepMillis*
            type: int
            Delay in milliseconds to wait before continuing.
    """

    fields = [
        'sleepMillis',
    ]

    category = 'general'
    
    def __init__(self, sleepMillis):
        super().__init__()
        self.name = 'Sleep'
        self.dataout = {}
        self.dataout['sleepMillis'] = None

    @staticmethod
    def payload(sleepMillis):
        payload = {}
        payload['request-type'] = 'Sleep'
        payload['sleepMillis'] = sleepMillis
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('sleepMillis'))
        
        return w

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

    fields = [
        'sourceName',
        'playPause',
    ]

    category = 'media control'
    
    def __init__(self, sourceName, playPause):
        super().__init__()
        self.name = 'PlayPauseMedia'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('playPause'))
        
        return w

class RestartMedia(BaseRequest):
    """Restart a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    fields = [
        'sourceName',
    ]

    category = 'media control'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'RestartMedia'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'RestartMedia'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

class StopMedia(BaseRequest):
    """Stop a media source. Supports ffmpeg and vlc media sources (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    fields = [
        'sourceName',
    ]

    category = 'media control'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'StopMedia'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'StopMedia'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

class NextMedia(BaseRequest):
    """Skip to the next media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    fields = [
        'sourceName',
    ]

    category = 'media control'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'NextMedia'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'NextMedia'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

class PreviousMedia(BaseRequest):
    """Go to the previous media item in the playlist. Supports only vlc media source (as of OBS v25.0.8)

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    fields = [
        'sourceName',
    ]

    category = 'media control'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'PreviousMedia'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'PreviousMedia'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'sourceName',
    ]

    category = 'media control'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetMediaDuration'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaDuration'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'sourceName',
    ]

    category = 'media control'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetMediaTime'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaTime'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'sourceName',
        'timestamp',
    ]

    category = 'media control'
    
    def __init__(self, sourceName, timestamp):
        super().__init__()
        self.name = 'SetMediaTime'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('timestamp'))
        
        return w

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

    fields = [
        'sourceName',
        'timeOffset',
    ]

    category = 'media control'
    
    def __init__(self, sourceName, timeOffset):
        super().__init__()
        self.name = 'ScrubMedia'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('timeOffset'))
        
        return w

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

    fields = [
        'sourceName',
    ]

    category = 'media control'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetMediaState'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetMediaState'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

class GetMediaSourcesList(BaseRequest):
    """List the media state of all media sources (vlc and media source)

    :Returns:
       *mediaSources*
            type: Array<Object>
            Array of sources
       *mediaSources.*.sourceName*
            type: String
            Unique source name
       *mediaSources.*.sourceKind*
            type: String
            Unique source internal type (a.k.a `ffmpeg_source` or `vlc_source`)
       *mediaSources.*.mediaState*
            type: String
            The current state of media for that source. States: `none`, `playing`, `opening`, `buffering`, `paused`, `stopped`, `ended`, `error`, `unknown`
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetMediaSourcesList'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetMediaSourcesList'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'sourceName',
        'sourceKind',
        'sceneName',
        'sourceSettings',
        'setVisible',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, sourceKind, sceneName, sourceSettings=None, setVisible=None):
        super().__init__()
        self.name = 'CreateSource'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        sceneName = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('sourceKind'))
            layout.add(sceneName)
            layout.add(QLabel('sourceSettings'))
            layout.add(QLabel('setVisible'))
        
        return w

class GetSourcesList(BaseRequest):
    """List all sources available in the running OBS instance

    :Returns:
       *sources*
            type: Array<Object>
            Array of sources
       *sources.*.name*
            type: String
            Unique source name
       *sources.*.typeId*
            type: String
            Non-unique source internal type (a.k.a kind)
       *sources.*.type*
            type: String
            Source type. Value is one of the following: "input", "filter", "transition", "scene" or "unknown"
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetSourcesList'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSourcesList'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class GetSourceTypesList(BaseRequest):
    """Get a list of all available sources types

    :Returns:
       *types*
            type: Array<Object>
            Array of source types
       *types.*.typeId*
            type: String
            Non-unique internal source type ID
       *types.*.displayName*
            type: String
            Display name of the source type
       *types.*.type*
            type: String
            Type. Value is one of the following: "input", "filter", "transition" or "other"
       *types.*.defaultSettings*
            type: Object
            Default settings of this source type
       *types.*.caps*
            type: Object
            Source type capabilities
       *types.*.caps.isAsync*
            type: Boolean
            True if source of this type provide frames asynchronously
       *types.*.caps.hasVideo*
            type: Boolean
            True if sources of this type provide video
       *types.*.caps.hasAudio*
            type: Boolean
            True if sources of this type provide audio
       *types.*.caps.canInteract*
            type: Boolean
            True if interaction with this sources of this type is possible
       *types.*.caps.isComposite*
            type: Boolean
            True if sources of this type composite one or more sub-sources
       *types.*.caps.doNotDuplicate*
            type: Boolean
            True if sources of this type should not be fully duplicated
       *types.*.caps.doNotSelfMonitor*
            type: Boolean
            True if sources of this type may cause a feedback loop if it's audio is monitored and shouldn't be
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetSourceTypesList'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSourceTypesList'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'source',
        'useDecibel',
    ]

    category = 'sources'
    
    def __init__(self, source, useDecibel=None):
        super().__init__()
        self.name = 'GetVolume'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
            layout.add(QLabel('useDecibel'))
        
        return w

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

    fields = [
        'source',
        'volume',
        'useDecibel',
    ]

    category = 'sources'
    
    def __init__(self, source, volume, useDecibel=None):
        super().__init__()
        self.name = 'SetVolume'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
            layout.add(QLabel('volume'))
            layout.add(QLabel('useDecibel'))
        
        return w

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

    fields = [
        'sourceName',
        'track',
        'active',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, track, active):
        super().__init__()
        self.name = 'SetTracks'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('track'))
            layout.add(QLabel('active'))
        
        return w

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

    fields = [
        'sourceName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetTracks'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetTracks'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'source',
    ]

    category = 'sources'
    
    def __init__(self, source):
        super().__init__()
        self.name = 'GetMute'
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetMute'
        payload['source'] = source
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
        
        return w

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

    fields = [
        'source',
        'mute',
    ]

    category = 'sources'
    
    def __init__(self, source, mute):
        super().__init__()
        self.name = 'SetMute'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
            layout.add(QLabel('mute'))
        
        return w

class ToggleMute(BaseRequest):
    """Inverts the mute status of a specified source.

    :Arguments:
       *source*
            type: String
            Source name.
    """

    fields = [
        'source',
    ]

    category = 'sources'
    
    def __init__(self, source):
        super().__init__()
        self.name = 'ToggleMute'
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'ToggleMute'
        payload['source'] = source
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
        
        return w

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

    fields = [
        'sourceName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetSourceActive'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetSourceActive'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'sourceName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetAudioActive'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetAudioActive'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'sourceName',
        'newName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, newName):
        super().__init__()
        self.name = 'SetSourceName'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('newName'))
        
        return w

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

    fields = [
        'source',
        'offset',
    ]

    category = 'sources'
    
    def __init__(self, source, offset):
        super().__init__()
        self.name = 'SetSyncOffset'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
            layout.add(QLabel('offset'))
        
        return w

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

    fields = [
        'source',
    ]

    category = 'sources'
    
    def __init__(self, source):
        super().__init__()
        self.name = 'GetSyncOffset'
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetSyncOffset'
        payload['source'] = source
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
        
        return w

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

    fields = [
        'sourceName',
        'sourceType',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, sourceType=None):
        super().__init__()
        self.name = 'GetSourceSettings'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('sourceType'))
        
        return w

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

    fields = [
        'sourceName',
        'sourceType',
        'sourceSettings',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, sourceSettings, sourceType=None):
        super().__init__()
        self.name = 'SetSourceSettings'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('sourceType'))
            layout.add(QLabel('sourceSettings'))
        
        return w

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
       *font.face*
            type: String
            Font face.
       *font.flags*
            type: int
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int
            Font text size.
       *font.style*
            type: String
            Font Style (unknown function).
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

    fields = [
        'source',
    ]

    category = 'sources'
    
    def __init__(self, source):
        super().__init__()
        self.name = 'GetTextGDIPlusProperties'
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetTextGDIPlusProperties'
        payload['source'] = source
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
        
        return w

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
       *font.face*
            type: String (optional)
            Font face.
       *font.flags*
            type: int (optional)
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int (optional)
            Font text size.
       *font.style*
            type: String (optional)
            Font Style (unknown function).
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

    category = 'sources'
    
    def __init__(self, source, align=None, bk_color=None, bk_opacity=None, chatlog=None, chatlog_lines=None, color=None, extents=None, extents_cx=None, extents_cy=None, file=None, read_from_file=None, font=None, gradient=None, gradient_color=None, gradient_dir=None, gradient_opacity=None, outline=None, outline_color=None, outline_size=None, outline_opacity=None, text=None, valign=None, vertical=None, render=None):
        super().__init__()
        self.name = 'SetTextGDIPlusProperties'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
            layout.add(QLabel('align'))
            layout.add(QLabel('bk_color'))
            layout.add(QLabel('bk_opacity'))
            layout.add(QLabel('chatlog'))
            layout.add(QLabel('chatlog_lines'))
            layout.add(QLabel('color'))
            layout.add(QLabel('extents'))
            layout.add(QLabel('extents_cx'))
            layout.add(QLabel('extents_cy'))
            layout.add(QLabel('file'))
            layout.add(QLabel('read_from_file'))
            layout.add(QLabel('font'))
            layout.add(QLabel('gradient'))
            layout.add(QLabel('gradient_color'))
            layout.add(QLabel('gradient_dir'))
            layout.add(QLabel('gradient_opacity'))
            layout.add(QLabel('outline'))
            layout.add(QLabel('outline_color'))
            layout.add(QLabel('outline_size'))
            layout.add(QLabel('outline_opacity'))
            layout.add(QLabel('text'))
            layout.add(QLabel('valign'))
            layout.add(QLabel('vertical'))
            layout.add(QLabel('render'))
        
        return w

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
       *font.face*
            type: String
            Font face.
       *font.flags*
            type: int
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int
            Font text size.
       *font.style*
            type: String
            Font Style (unknown function).
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

    fields = [
        'source',
    ]

    category = 'sources'
    
    def __init__(self, source):
        super().__init__()
        self.name = 'GetTextFreetype2Properties'
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetTextFreetype2Properties'
        payload['source'] = source
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
        
        return w

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
       *font.face*
            type: String (optional)
            Font face.
       *font.flags*
            type: int (optional)
            Font text styling flag. `Bold=1, Italic=2, Bold Italic=3, Underline=5, Strikeout=8`
       *font.size*
            type: int (optional)
            Font text size.
       *font.style*
            type: String (optional)
            Font Style (unknown function).
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

    category = 'sources'
    
    def __init__(self, source, color1=None, color2=None, custom_width=None, drop_shadow=None, font=None, from_file=None, log_mode=None, outline=None, text=None, text_file=None, word_wrap=None):
        super().__init__()
        self.name = 'SetTextFreetype2Properties'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
            layout.add(QLabel('color1'))
            layout.add(QLabel('color2'))
            layout.add(QLabel('custom_width'))
            layout.add(QLabel('drop_shadow'))
            layout.add(QLabel('font'))
            layout.add(QLabel('from_file'))
            layout.add(QLabel('log_mode'))
            layout.add(QLabel('outline'))
            layout.add(QLabel('text'))
            layout.add(QLabel('text_file'))
            layout.add(QLabel('word_wrap'))
        
        return w

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

    fields = [
        'source',
    ]

    category = 'sources'
    
    def __init__(self, source):
        super().__init__()
        self.name = 'GetBrowserSourceProperties'
        self.dataout = {}
        self.dataout['source'] = None

    @staticmethod
    def payload(source):
        payload = {}
        payload['request-type'] = 'GetBrowserSourceProperties'
        payload['source'] = source
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
        
        return w

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

    category = 'sources'
    
    def __init__(self, source, is_local_file=None, local_file=None, url=None, css=None, width=None, height=None, fps=None, shutdown=None, render=None):
        super().__init__()
        self.name = 'SetBrowserSourceProperties'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('source'))
            layout.add(QLabel('is_local_file'))
            layout.add(QLabel('local_file'))
            layout.add(QLabel('url'))
            layout.add(QLabel('css'))
            layout.add(QLabel('width'))
            layout.add(QLabel('height'))
            layout.add(QLabel('fps'))
            layout.add(QLabel('shutdown'))
            layout.add(QLabel('render'))
        
        return w

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

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetSpecialSources'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSpecialSources'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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
       *filters.*.enabled*
            type: Boolean
            Filter status (enabled or not)
       *filters.*.type*
            type: String
            Filter type
       *filters.*.name*
            type: String
            Filter name
       *filters.*.settings*
            type: Object
            Filter settings
    """

    fields = [
        'sourceName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetSourceFilters'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetSourceFilters'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'sourceName',
        'filterName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, filterName):
        super().__init__()
        self.name = 'GetSourceFilterInfo'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        filterName = FilterSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(filterName)
        
        return w

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

    fields = [
        'sourceName',
        'filterName',
        'filterType',
        'filterSettings',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, filterName, filterType, filterSettings):
        super().__init__()
        self.name = 'AddFilterToSource'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        filterName = FilterSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(filterName)
            layout.add(QLabel('filterType'))
            layout.add(QLabel('filterSettings'))
        
        return w

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

    fields = [
        'sourceName',
        'filterName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, filterName):
        super().__init__()
        self.name = 'RemoveFilterFromSource'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        filterName = FilterSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(filterName)
        
        return w

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

    fields = [
        'sourceName',
        'filterName',
        'newIndex',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, filterName, newIndex):
        super().__init__()
        self.name = 'ReorderSourceFilter'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        filterName = FilterSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(filterName)
            layout.add(QLabel('newIndex'))
        
        return w

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

    fields = [
        'sourceName',
        'filterName',
        'movementType',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, filterName, movementType):
        super().__init__()
        self.name = 'MoveSourceFilter'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        filterName = FilterSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(filterName)
            layout.add(QLabel('movementType'))
        
        return w

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

    fields = [
        'sourceName',
        'filterName',
        'filterSettings',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, filterName, filterSettings):
        super().__init__()
        self.name = 'SetSourceFilterSettings'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        filterName = FilterSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(filterName)
            layout.add(QLabel('filterSettings'))
        
        return w

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

    fields = [
        'sourceName',
        'filterName',
        'filterEnabled',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, filterName, filterEnabled):
        super().__init__()
        self.name = 'SetSourceFilterVisibility'
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
        payload['filterEnabled'] = bool(filterEnabled)
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        filterName = FilterSelector(changed)
        filterEnabled = BoolSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(filterName)
            layout.add(filterEnabled)
        
        return w

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

    fields = [
        'sourceName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'GetAudioMonitorType'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'GetAudioMonitorType'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

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

    fields = [
        'sourceName',
        'monitorType',
    ]

    category = 'sources'
    
    def __init__(self, sourceName, monitorType):
        super().__init__()
        self.name = 'SetAudioMonitorType'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('monitorType'))
        
        return w

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

    fields = [
        'sourceKind',
    ]

    category = 'sources'
    
    def __init__(self, sourceKind):
        super().__init__()
        self.name = 'GetSourceDefaultSettings'
        self.dataout = {}
        self.dataout['sourceKind'] = None

    @staticmethod
    def payload(sourceKind):
        payload = {}
        payload['request-type'] = 'GetSourceDefaultSettings'
        payload['sourceKind'] = sourceKind
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('sourceKind'))
        
        return w

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

    fields = [
        'sourceName',
        'embedPictureFormat',
        'saveToFilePath',
        'fileFormat',
        'compressionQuality',
        'width',
        'height',
    ]

    category = 'sources'
    
    def __init__(self, sourceName=None, embedPictureFormat=None, saveToFilePath=None, fileFormat=None, compressionQuality=None, width=None, height=None):
        super().__init__()
        self.name = 'TakeSourceScreenshot'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
            layout.add(QLabel('embedPictureFormat'))
            layout.add(QLabel('saveToFilePath'))
            layout.add(QLabel('fileFormat'))
            layout.add(QLabel('compressionQuality'))
            layout.add(QLabel('width'))
            layout.add(QLabel('height'))
        
        return w

class RefreshBrowserSource(BaseRequest):
    """Refreshes the specified browser source.

    :Arguments:
       *sourceName*
            type: String
            Source name.
    """

    fields = [
        'sourceName',
    ]

    category = 'sources'
    
    def __init__(self, sourceName):
        super().__init__()
        self.name = 'RefreshBrowserSource'
        self.dataout = {}
        self.dataout['sourceName'] = None

    @staticmethod
    def payload(sourceName):
        payload = {}
        payload['request-type'] = 'RefreshBrowserSource'
        payload['sourceName'] = sourceName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sourceName)
        
        return w

class ListOutputs(BaseRequest):
    """List existing outputs

    :Returns:
       *outputs*
            type: Array<Output>
            Outputs list
    """

    fields = [
    ]

    category = 'outputs'
    
    def __init__(self):
        super().__init__()
        self.name = 'ListOutputs'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListOutputs'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'outputName',
    ]

    category = 'outputs'
    
    def __init__(self, outputName):
        super().__init__()
        self.name = 'GetOutputInfo'
        self.dataout = {}
        self.dataout['outputName'] = None

    @staticmethod
    def payload(outputName):
        payload = {}
        payload['request-type'] = 'GetOutputInfo'
        payload['outputName'] = outputName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('outputName'))
        
        return w

class StartOutput(BaseRequest):
    """

Note: Controlling outputs is an experimental feature of obs-websocket. Some plugins which add outputs to OBS may not function properly when they are controlled in this way.

    :Arguments:
       *outputName*
            type: String
            Output name
    """

    fields = [
        'outputName',
    ]

    category = 'outputs'
    
    def __init__(self, outputName):
        super().__init__()
        self.name = 'StartOutput'
        self.dataout = {}
        self.dataout['outputName'] = None

    @staticmethod
    def payload(outputName):
        payload = {}
        payload['request-type'] = 'StartOutput'
        payload['outputName'] = outputName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('outputName'))
        
        return w

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

    fields = [
        'outputName',
        'force',
    ]

    category = 'outputs'
    
    def __init__(self, outputName, force=None):
        super().__init__()
        self.name = 'StopOutput'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('outputName'))
            layout.add(QLabel('force'))
        
        return w

class SetCurrentProfile(BaseRequest):
    """Set the currently active profile.

    :Arguments:
       *profile_name*
            type: String
            Name of the desired profile.
    """

    fields = [
        'profile_name',
    ]

    category = 'profiles'
    
    def __init__(self, profile_name):
        super().__init__()
        self.name = 'SetCurrentProfile'
        self.dataout = {}
        self.dataout['profile-name'] = None

    @staticmethod
    def payload(profile_name):
        payload = {}
        payload['request-type'] = 'SetCurrentProfile'
        payload['profile_name'] = profile_name
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('profile_name'))
        
        return w

class GetCurrentProfile(BaseRequest):
    """Get the name of the current profile.

    :Returns:
       *profile_name*
            type: String
            Name of the currently active profile.
    """

    fields = [
    ]

    category = 'profiles'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetCurrentProfile'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentProfile'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ListProfiles(BaseRequest):
    """Get a list of available profiles.

    :Returns:
       *profiles*
            type: Array<Object>
            List of available profiles.
       *profiles.*.profile_name*
            type: String
            Filter name
    """

    fields = [
    ]

    category = 'profiles'
    
    def __init__(self):
        super().__init__()
        self.name = 'ListProfiles'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListProfiles'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetRecordingStatus'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetRecordingStatus'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StartStopRecording(BaseRequest):
    """Toggle recording on or off (depending on the current recording state).

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'StartStopRecording'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopRecording'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StartRecording(BaseRequest):
    """Start recording.
Will return an `error` if recording is already active.

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'StartRecording'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartRecording'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StopRecording(BaseRequest):
    """Stop recording.
Will return an `error` if recording is not active.

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'StopRecording'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopRecording'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class PauseRecording(BaseRequest):
    """Pause the current recording.
Returns an error if recording is not active or already paused.

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'PauseRecording'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'PauseRecording'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ResumeRecording(BaseRequest):
    """Resume/unpause the current recording (if paused).
Returns an error if recording is not active or not paused.

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'ResumeRecording'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ResumeRecording'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'rec_folder',
    ]

    category = 'recording'
    
    def __init__(self, rec_folder):
        super().__init__()
        self.name = 'SetRecordingFolder'
        self.dataout = {}
        self.dataout['rec-folder'] = None

    @staticmethod
    def payload(rec_folder):
        payload = {}
        payload['request-type'] = 'SetRecordingFolder'
        payload['rec_folder'] = rec_folder
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('rec_folder'))
        
        return w

class GetRecordingFolder(BaseRequest):
    """Get the path of  the current recording folder.

    :Returns:
       *rec_folder*
            type: String
            Path of the recording folder.
    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetRecordingFolder'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetRecordingFolder'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class GetReplayBufferStatus(BaseRequest):
    """Get the status of the OBS replay buffer.

    :Returns:
       *isReplayBufferActive*
            type: boolean
            Current recording status.
    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetReplayBufferStatus'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetReplayBufferStatus'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StartStopReplayBuffer(BaseRequest):
    """Toggle the Replay Buffer on/off (depending on the current state of the replay buffer).

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'StartStopReplayBuffer'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopReplayBuffer'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StartReplayBuffer(BaseRequest):
    """Start recording into the Replay Buffer.
Will return an `error` if the Replay Buffer is already active or if the
"Save Replay Buffer" hotkey is not set in OBS' settings.
Setting this hotkey is mandatory, even when triggering saves only
through obs-websocket.

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'StartReplayBuffer'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartReplayBuffer'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StopReplayBuffer(BaseRequest):
    """Stop recording into the Replay Buffer.
Will return an `error` if the Replay Buffer is not active.

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'StopReplayBuffer'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopReplayBuffer'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SaveReplayBuffer(BaseRequest):
    """Flush and save the contents of the Replay Buffer to disk. This is
basically the same as triggering the "Save Replay Buffer" hotkey.
Will return an `error` if the Replay Buffer is not active.

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'SaveReplayBuffer'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SaveReplayBuffer'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SetCurrentSceneCollection(BaseRequest):
    """Change the active scene collection.

    :Arguments:
       *sc_name*
            type: String
            Name of the desired scene collection.
    """

    fields = [
        'sc_name',
    ]

    category = 'scene collections'
    
    def __init__(self, sc_name):
        super().__init__()
        self.name = 'SetCurrentSceneCollection'
        self.dataout = {}
        self.dataout['sc-name'] = None

    @staticmethod
    def payload(sc_name):
        payload = {}
        payload['request-type'] = 'SetCurrentSceneCollection'
        payload['sc_name'] = sc_name
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('sc_name'))
        
        return w

class GetCurrentSceneCollection(BaseRequest):
    """Get the name of the current scene collection.

    :Returns:
       *sc_name*
            type: String
            Name of the currently active scene collection.
    """

    fields = [
    ]

    category = 'scene collections'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetCurrentSceneCollection'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentSceneCollection'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ListSceneCollections(BaseRequest):
    """List available scene collections

    :Returns:
       *scene_collections*
            type: Array<ScenesCollection>
            Scene collections list
    """

    fields = [
    ]

    category = 'scene collections'
    
    def __init__(self):
        super().__init__()
        self.name = 'ListSceneCollections'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ListSceneCollections'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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
       *sceneItems.*.itemId*
            type: int
            Unique item id of the source item
       *sceneItems.*.sourceKind*
            type: String
            ID if the scene item's source. For example `vlc_source` or `image_source`
       *sceneItems.*.sourceName*
            type: String
            Name of the scene item's source
       *sceneItems.*.sourceType*
            type: String
            Type of the scene item's source. Either `input`, `group`, or `scene`
    """

    fields = [
        'sceneName',
    ]

    category = 'scene items'
    
    def __init__(self, sceneName=None):
        super().__init__()
        self.name = 'GetSceneItemList'
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemList'
        payload['sceneName'] = sceneName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sceneName = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sceneName)
        
        return w

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
       *item.name*
            type: String (optional)
            Scene Item name (if the `item` field is an object)
       *item.id*
            type: int (optional)
            Scene Item ID (if the `item` field is an object)
    :Returns:
       *name*
            type: String
            Scene Item name.
       *itemId*
            type: int
            Scene Item ID.
       *position.x*
            type: double
            The x position of the source from the left.
       *position.y*
            type: double
            The y position of the source from the top.
       *position.alignment*
            type: int
            The point on the source that the item is manipulated from. The sum of 1=Left or 2=Right, and 4=Top or 8=Bottom, or omit to center on that axis.
       *rotation*
            type: double
            The clockwise rotation of the item in degrees around the point of alignment.
       *scale.x*
            type: double
            The x-scale factor of the source.
       *scale.y*
            type: double
            The y-scale factor of the source.
       *scale.filter*
            type: String
            The scale filter of the source. Can be "OBS_SCALE_DISABLE", "OBS_SCALE_POINT", "OBS_SCALE_BICUBIC", "OBS_SCALE_BILINEAR", "OBS_SCALE_LANCZOS" or "OBS_SCALE_AREA".
       *crop.top*
            type: int
            The number of pixels cropped off the top of the source before scaling.
       *crop.right*
            type: int
            The number of pixels cropped off the right of the source before scaling.
       *crop.bottom*
            type: int
            The number of pixels cropped off the bottom of the source before scaling.
       *crop.left*
            type: int
            The number of pixels cropped off the left of the source before scaling.
       *visible*
            type: bool
            If the source is visible.
       *muted*
            type: bool
            If the source is muted.
       *locked*
            type: bool
            If the source's transform is locked.
       *bounds.type*
            type: String
            Type of bounding box. Can be "OBS_BOUNDS_STRETCH", "OBS_BOUNDS_SCALE_INNER", "OBS_BOUNDS_SCALE_OUTER", "OBS_BOUNDS_SCALE_TO_WIDTH", "OBS_BOUNDS_SCALE_TO_HEIGHT", "OBS_BOUNDS_MAX_ONLY" or "OBS_BOUNDS_NONE".
       *bounds.alignment*
            type: int
            Alignment of the bounding box.
       *bounds.x*
            type: double
            Width of the bounding box.
       *bounds.y*
            type: double
            Height of the bounding box.
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

    fields = [
        'scene_name',
        'item',
    ]

    category = 'scene items'
    
    def __init__(self, item, scene_name=None):
        super().__init__()
        self.name = 'GetSceneItemProperties'
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['scene-name'] = None

    @staticmethod
    def payload(item, scene_name=None):
        payload = {}
        payload['request-type'] = 'GetSceneItemProperties'
        payload['scene_name'] = scene_name
        payload['item'] = item
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
            layout.add(QLabel('item'))
        
        return w

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
       *item.name*
            type: String (optional)
            Scene Item name (if the `item` field is an object)
       *item.id*
            type: int (optional)
            Scene Item ID (if the `item` field is an object)
       *position.x*
            type: double (optional)
            The new x position of the source.
       *position.y*
            type: double (optional)
            The new y position of the source.
       *position.alignment*
            type: int (optional)
            The new alignment of the source.
       *rotation*
            type: double (optional)
            The new clockwise rotation of the item in degrees.
       *scale.x*
            type: double (optional)
            The new x scale of the item.
       *scale.y*
            type: double (optional)
            The new y scale of the item.
       *scale.filter*
            type: String (optional)
            The new scale filter of the source. Can be "OBS_SCALE_DISABLE", "OBS_SCALE_POINT", "OBS_SCALE_BICUBIC", "OBS_SCALE_BILINEAR", "OBS_SCALE_LANCZOS" or "OBS_SCALE_AREA".
       *crop.top*
            type: int (optional)
            The new amount of pixels cropped off the top of the source before scaling.
       *crop.bottom*
            type: int (optional)
            The new amount of pixels cropped off the bottom of the source before scaling.
       *crop.left*
            type: int (optional)
            The new amount of pixels cropped off the left of the source before scaling.
       *crop.right*
            type: int (optional)
            The new amount of pixels cropped off the right of the source before scaling.
       *visible*
            type: bool (optional)
            The new visibility of the source. 'true' shows source, 'false' hides source.
       *locked*
            type: bool (optional)
            The new locked status of the source. 'true' keeps it in its current position, 'false' allows movement.
       *bounds.type*
            type: String (optional)
            The new bounds type of the source. Can be "OBS_BOUNDS_STRETCH", "OBS_BOUNDS_SCALE_INNER", "OBS_BOUNDS_SCALE_OUTER", "OBS_BOUNDS_SCALE_TO_WIDTH", "OBS_BOUNDS_SCALE_TO_HEIGHT", "OBS_BOUNDS_MAX_ONLY" or "OBS_BOUNDS_NONE".
       *bounds.alignment*
            type: int (optional)
            The new alignment of the bounding box. (0-2, 4-6, 8-10)
       *bounds.x*
            type: double (optional)
            The new width of the bounding box.
       *bounds.y*
            type: double (optional)
            The new height of the bounding box.
    """

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

    category = 'scene items'
    
    def __init__(self, item, scene_name=None, position=None, rotation=None, scale=None, crop=None, visible=None, locked=None, bounds=None):
        super().__init__()
        self.name = 'SetSceneItemProperties'
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['scene-name'] = None
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
        payload['scene_name'] = scene_name
        payload['item'] = item
        payload['position'] = position
        payload['rotation'] = rotation
        payload['scale'] = scale
        payload['crop'] = crop
        payload['visible'] = visible
        payload['locked'] = locked
        payload['bounds'] = bounds
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
            layout.add(QLabel('item'))
            layout.add(QLabel('position'))
            layout.add(QLabel('rotation'))
            layout.add(QLabel('scale'))
            layout.add(QLabel('crop'))
            layout.add(QLabel('visible'))
            layout.add(QLabel('locked'))
            layout.add(QLabel('bounds'))
        
        return w

class ResetSceneItem(BaseRequest):
    """Reset a scene item.

    :Arguments:
       *scene_name*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: String | Object
            Scene Item name (if this field is a string) or specification (if it is an object).
       *item.name*
            type: String (optional)
            Scene Item name (if the `item` field is an object)
       *item.id*
            type: int (optional)
            Scene Item ID (if the `item` field is an object)
    """

    fields = [
        'scene_name',
        'item',
    ]

    category = 'scene items'
    
    def __init__(self, item, scene_name=None):
        super().__init__()
        self.name = 'ResetSceneItem'
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['scene-name'] = None

    @staticmethod
    def payload(item, scene_name=None):
        payload = {}
        payload['request-type'] = 'ResetSceneItem'
        payload['scene_name'] = scene_name
        payload['item'] = item
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
            layout.add(QLabel('item'))
        
        return w

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

    fields = [
        'scene_name',
        'source',
        'item',
        'render',
    ]

    category = 'scene items'
    
    def __init__(self, render, scene_name=None, source=None, item=None):
        super().__init__()
        self.name = 'SetSceneItemRender'
        self.dataout = {}
        self.dataout['render'] = None
        self.dataout['scene-name'] = None
        self.dataout['source'] = None
        self.dataout['item'] = None

    @staticmethod
    def payload(render, scene_name=None, source=None, item=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemRender'
        payload['scene_name'] = scene_name
        payload['source'] = source
        payload['item'] = item
        payload['render'] = render
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
            layout.add(QLabel('source'))
            layout.add(QLabel('item'))
            layout.add(QLabel('render'))
        
        return w

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

    fields = [
        'scene_name',
        'item',
        'x',
        'y',
    ]

    category = 'scene items'
    
    def __init__(self, item, x, y, scene_name=None):
        super().__init__()
        self.name = 'SetSceneItemPosition'
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['x'] = None
        self.dataout['y'] = None
        self.dataout['scene-name'] = None

    @staticmethod
    def payload(item, x, y, scene_name=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemPosition'
        payload['scene_name'] = scene_name
        payload['item'] = item
        payload['x'] = x
        payload['y'] = y
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
            layout.add(QLabel('item'))
            layout.add(QLabel('x'))
            layout.add(QLabel('y'))
        
        return w

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

    fields = [
        'scene_name',
        'item',
        'x_scale',
        'y_scale',
        'rotation',
    ]

    category = 'scene items'
    
    def __init__(self, item, x_scale, y_scale, rotation, scene_name=None):
        super().__init__()
        self.name = 'SetSceneItemTransform'
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['x-scale'] = None
        self.dataout['y-scale'] = None
        self.dataout['rotation'] = None
        self.dataout['scene-name'] = None

    @staticmethod
    def payload(item, x_scale, y_scale, rotation, scene_name=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemTransform'
        payload['scene_name'] = scene_name
        payload['item'] = item
        payload['x_scale'] = x_scale
        payload['y_scale'] = y_scale
        payload['rotation'] = rotation
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
            layout.add(QLabel('item'))
            layout.add(QLabel('x_scale'))
            layout.add(QLabel('y_scale'))
            layout.add(QLabel('rotation'))
        
        return w

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

    fields = [
        'scene_name',
        'item',
        'top',
        'bottom',
        'left',
        'right',
    ]

    category = 'scene items'
    
    def __init__(self, item, top, bottom, left, right, scene_name=None):
        super().__init__()
        self.name = 'SetSceneItemCrop'
        self.dataout = {}
        self.dataout['item'] = None
        self.dataout['top'] = None
        self.dataout['bottom'] = None
        self.dataout['left'] = None
        self.dataout['right'] = None
        self.dataout['scene-name'] = None

    @staticmethod
    def payload(item, top, bottom, left, right, scene_name=None):
        payload = {}
        payload['request-type'] = 'SetSceneItemCrop'
        payload['scene_name'] = scene_name
        payload['item'] = item
        payload['top'] = top
        payload['bottom'] = bottom
        payload['left'] = left
        payload['right'] = right
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
            layout.add(QLabel('item'))
            layout.add(QLabel('top'))
            layout.add(QLabel('bottom'))
            layout.add(QLabel('left'))
            layout.add(QLabel('right'))
        
        return w

class DeleteSceneItem(BaseRequest):
    """Deletes a scene item.

    :Arguments:
       *scene*
            type: String (optional)
            Name of the scene the scene item belongs to. Defaults to the current scene.
       *item*
            type: Object
            Scene item to delete (required)
       *item.name*
            type: String
            Scene Item name (prefer `id`, including both is acceptable).
       *item.id*
            type: int
            Scene Item ID.
    """

    fields = [
        'scene',
        'item',
    ]

    category = 'scene items'
    
    def __init__(self, item, scene=None):
        super().__init__()
        self.name = 'DeleteSceneItem'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('scene'))
            layout.add(QLabel('item'))
        
        return w

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

    fields = [
        'sceneName',
        'sourceName',
        'setVisible',
    ]

    category = 'scene items'
    
    def __init__(self, sceneName, sourceName, setVisible=None):
        super().__init__()
        self.name = 'AddSceneItem'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sceneName = SceneSelector(changed)
        sourceName = SourceSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sceneName)
            layout.add(sourceName)
            layout.add(QLabel('setVisible'))
        
        return w

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
       *item.name*
            type: String
            Scene Item name (prefer `id`, including both is acceptable).
       *item.id*
            type: int
            Scene Item ID.
    :Returns:
       *scene*
            type: String
            Name of the scene where the new item was created
       *item*
            type: Object
            New item info
       *item.id*
            type: int
            New item ID
       *item.name*
            type: String
            New item name
    """

    fields = [
        'fromScene',
        'toScene',
        'item',
    ]

    category = 'scene items'
    
    def __init__(self, item, fromScene=None, toScene=None):
        super().__init__()
        self.name = 'DuplicateSceneItem'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('fromScene'))
            layout.add(QLabel('toScene'))
            layout.add(QLabel('item'))
        
        return w

class SetCurrentScene(BaseRequest):
    """Switch to the specified scene.

    :Arguments:
       *scene_name*
            type: String
            Name of the scene to switch to.
    """

    fields = [
        'scene_name',
    ]

    category = 'scenes'
    
    def __init__(self, scene_name):
        super().__init__()
        self.name = 'SetCurrentScene'
        self.dataout = {}
        self.dataout['scene-name'] = None

    @staticmethod
    def payload(scene_name):
        payload = {}
        payload['request-type'] = 'SetCurrentScene'
        payload['scene_name'] = scene_name
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
        
        return w

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

    fields = [
    ]

    category = 'scenes'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetCurrentScene'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentScene'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
    ]

    category = 'scenes'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetSceneList'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetSceneList'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class CreateScene(BaseRequest):
    """Create a new scene scene.

    :Arguments:
       *sceneName*
            type: String
            Name of the scene to create.
    """

    fields = [
        'sceneName',
    ]

    category = 'scenes'
    
    def __init__(self, sceneName):
        super().__init__()
        self.name = 'CreateScene'
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'CreateScene'
        payload['sceneName'] = sceneName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sceneName = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sceneName)
        
        return w

class ReorderSceneItems(BaseRequest):
    """Changes the order of scene items in the requested scene.

    :Arguments:
       *scene*
            type: String (optional)
            Name of the scene to reorder (defaults to current).
       *items*
            type: Array<Scene>
            Ordered list of objects with name and/or id specified. Id preferred due to uniqueness per scene
       *items.*.id*
            type: int (optional)
            Id of a specific scene item. Unique on a scene by scene basis.
       *items.*.name*
            type: String (optional)
            Name of a scene item. Sufficiently unique if no scene items share sources within the scene.
    """

    fields = [
        'scene',
        'items',
    ]

    category = 'scenes'
    
    def __init__(self, items, scene=None):
        super().__init__()
        self.name = 'ReorderSceneItems'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('scene'))
            layout.add(QLabel('items'))
        
        return w

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

    fields = [
        'sceneName',
        'transitionName',
        'transitionDuration',
    ]

    category = 'scenes'
    
    def __init__(self, sceneName, transitionName, transitionDuration):
        super().__init__()
        self.name = 'SetSceneTransitionOverride'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        sceneName = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sceneName)
            layout.add(QLabel('transitionName'))
            layout.add(QLabel('transitionDuration'))
        
        return w

class RemoveSceneTransitionOverride(BaseRequest):
    """Remove any transition override on a scene.

    :Arguments:
       *sceneName*
            type: String
            Name of the scene to switch to.
    """

    fields = [
        'sceneName',
    ]

    category = 'scenes'
    
    def __init__(self, sceneName):
        super().__init__()
        self.name = 'RemoveSceneTransitionOverride'
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'RemoveSceneTransitionOverride'
        payload['sceneName'] = sceneName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sceneName = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sceneName)
        
        return w

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

    fields = [
        'sceneName',
    ]

    category = 'scenes'
    
    def __init__(self, sceneName):
        super().__init__()
        self.name = 'GetSceneTransitionOverride'
        self.dataout = {}
        self.dataout['sceneName'] = None

    @staticmethod
    def payload(sceneName):
        payload = {}
        payload['request-type'] = 'GetSceneTransitionOverride'
        payload['sceneName'] = sceneName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        sceneName = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(sceneName)
        
        return w

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

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetStreamingStatus'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStreamingStatus'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StartStopStreaming(BaseRequest):
    """Toggle streaming on or off (depending on the current stream state).

    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'StartStopStreaming'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StartStopStreaming'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StartStreaming(BaseRequest):
    """Start streaming.
Will return an `error` if streaming is already active.

    :Arguments:
       *stream*
            type: Object (optional)
            Special stream configuration. Note: these won't be saved to OBS' configuration.
       *stream.type*
            type: String (optional)
            If specified ensures the type of stream matches the given type (usually 'rtmp_custom' or 'rtmp_common'). If the currently configured stream type does not match the given stream type, all settings must be specified in the `settings` object or an error will occur when starting the stream.
       *stream.metadata*
            type: Object (optional)
            Adds the given object parameters as encoded query string parameters to the 'key' of the RTMP stream. Used to pass data to the RTMP service about the streaming. May be any String, Numeric, or Boolean field.
       *stream.settings*
            type: Object (optional)
            Settings for the stream.
       *stream.settings.server*
            type: String (optional)
            The publish URL.
       *stream.settings.key*
            type: String (optional)
            The publish key of the stream.
       *stream.settings.use_auth*
            type: boolean (optional)
            Indicates whether authentication should be used when connecting to the streaming server.
       *stream.settings.username*
            type: String (optional)
            If authentication is enabled, the username for the streaming server. Ignored if `use_auth` is not set to `true`.
       *stream.settings.password*
            type: String (optional)
            If authentication is enabled, the password for the streaming server. Ignored if `use_auth` is not set to `true`.
    """

    fields = [
        'stream',
    ]

    category = 'streaming'
    
    def __init__(self, stream=None):
        super().__init__()
        self.name = 'StartStreaming'
        self.dataout = {}
        self.dataout['stream'] = None

    @staticmethod
    def payload(stream=None):
        payload = {}
        payload['request-type'] = 'StartStreaming'
        payload['stream'] = stream
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('stream'))
        
        return w

class StopStreaming(BaseRequest):
    """Stop streaming.
Will return an `error` if streaming is not active.

    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'StopStreaming'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StopStreaming'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SetStreamSettings(BaseRequest):
    """Sets one or more attributes of the current streaming server settings. Any options not passed will remain unchanged. Returns the updated settings in response. If 'type' is different than the current streaming service type, all settings are required. Returns the full settings of the stream (the same as GetStreamSettings).

    :Arguments:
       *type*
            type: String
            The type of streaming service configuration, usually `rtmp_custom` or `rtmp_common`.
       *settings*
            type: Object
            The actual settings of the stream.
       *settings.server*
            type: String (optional)
            The publish URL.
       *settings.key*
            type: String (optional)
            The publish key.
       *settings.use_auth*
            type: boolean (optional)
            Indicates whether authentication should be used when connecting to the streaming server.
       *settings.username*
            type: String (optional)
            The username for the streaming service.
       *settings.password*
            type: String (optional)
            The password for the streaming service.
       *save*
            type: boolean
            Persist the settings to disk.
    """

    fields = [
        'type',
        'settings',
        'save',
    ]

    category = 'streaming'
    
    def __init__(self, type, settings, save):
        super().__init__()
        self.name = 'SetStreamSettings'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('type'))
            layout.add(QLabel('settings'))
            layout.add(QLabel('save'))
        
        return w

class GetStreamSettings(BaseRequest):
    """Get the current streaming server settings.

    :Returns:
       *type*
            type: String
            The type of streaming service configuration. Possible values: 'rtmp_custom' or 'rtmp_common'.
       *settings*
            type: Object
            Stream settings object.
       *settings.server*
            type: String
            The publish URL.
       *settings.key*
            type: String
            The publish key of the stream.
       *settings.use_auth*
            type: boolean
            Indicates whether authentication should be used when connecting to the streaming server.
       *settings.username*
            type: String
            The username to use when accessing the streaming server. Only present if `use_auth` is `true`.
       *settings.password*
            type: String
            The password to use when accessing the streaming server. Only present if `use_auth` is `true`.
    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetStreamSettings'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStreamSettings'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SaveStreamSettings(BaseRequest):
    """Save the current streaming server settings to disk.

    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'SaveStreamSettings'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SaveStreamSettings'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SendCaptions(BaseRequest):
    """Send the provided text as embedded CEA-608 caption data.

    :Arguments:
       *text*
            type: String
            Captions text
    """

    fields = [
        'text',
    ]

    category = 'streaming'
    
    def __init__(self, text):
        super().__init__()
        self.name = 'SendCaptions'
        self.dataout = {}
        self.dataout['text'] = None

    @staticmethod
    def payload(text):
        payload = {}
        payload['request-type'] = 'SendCaptions'
        payload['text'] = text
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('text'))
        
        return w

class GetStudioModeStatus(BaseRequest):
    """Indicates if Studio Mode is currently enabled.

    :Returns:
       *studio_mode*
            type: boolean
            Indicates if Studio Mode is enabled.
    """

    fields = [
    ]

    category = 'studio mode'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetStudioModeStatus'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetStudioModeStatus'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
    ]

    category = 'studio mode'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetPreviewScene'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetPreviewScene'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SetPreviewScene(BaseRequest):
    """Set the active preview scene.
Will return an `error` if Studio Mode is not enabled.

    :Arguments:
       *scene_name*
            type: String
            The name of the scene to preview.
    """

    fields = [
        'scene_name',
    ]

    category = 'studio mode'
    
    def __init__(self, scene_name):
        super().__init__()
        self.name = 'SetPreviewScene'
        self.dataout = {}
        self.dataout['scene-name'] = None

    @staticmethod
    def payload(scene_name):
        payload = {}
        payload['request-type'] = 'SetPreviewScene'
        payload['scene_name'] = scene_name
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        scene_name = SceneSelector(changed)
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(scene_name)
        
        return w

class TransitionToProgram(BaseRequest):
    """Transitions the currently previewed scene to the main output.
Will return an `error` if Studio Mode is not enabled.

    :Arguments:
       *with_transition*
            type: Object (optional)
            Change the active transition before switching scenes. Defaults to the active transition.
       *with_transition.name*
            type: String
            Name of the transition.
       *with_transition.duration*
            type: int (optional)
            Transition duration (in milliseconds).
    """

    fields = [
        'with_transition',
    ]

    category = 'studio mode'
    
    def __init__(self, with_transition=None):
        super().__init__()
        self.name = 'TransitionToProgram'
        self.dataout = {}
        self.dataout['with-transition'] = None

    @staticmethod
    def payload(with_transition=None):
        payload = {}
        payload['request-type'] = 'TransitionToProgram'
        payload['with_transition'] = with_transition
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('with_transition'))
        
        return w

class EnableStudioMode(BaseRequest):
    """Enables Studio Mode.

    """

    fields = [
    ]

    category = 'studio mode'
    
    def __init__(self):
        super().__init__()
        self.name = 'EnableStudioMode'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'EnableStudioMode'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class DisableStudioMode(BaseRequest):
    """Disables Studio Mode.

    """

    fields = [
    ]

    category = 'studio mode'
    
    def __init__(self):
        super().__init__()
        self.name = 'DisableStudioMode'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'DisableStudioMode'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ToggleStudioMode(BaseRequest):
    """Toggles Studio Mode (depending on the current state of studio mode).

    """

    fields = [
    ]

    category = 'studio mode'
    
    def __init__(self):
        super().__init__()
        self.name = 'ToggleStudioMode'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ToggleStudioMode'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class GetTransitionList(BaseRequest):
    """List of all transitions available in the frontend's dropdown menu.

    :Returns:
       *current_transition*
            type: String
            Name of the currently active transition.
       *transitions*
            type: Array<Object>
            List of transitions.
       *transitions.*.name*
            type: String
            Name of the transition.
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetTransitionList'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionList'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetCurrentTransition'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetCurrentTransition'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SetCurrentTransition(BaseRequest):
    """Set the active transition.

    :Arguments:
       *transition_name*
            type: String
            The name of the transition.
    """

    fields = [
        'transition_name',
    ]

    category = 'transitions'
    
    def __init__(self, transition_name):
        super().__init__()
        self.name = 'SetCurrentTransition'
        self.dataout = {}
        self.dataout['transition-name'] = None

    @staticmethod
    def payload(transition_name):
        payload = {}
        payload['request-type'] = 'SetCurrentTransition'
        payload['transition_name'] = transition_name
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('transition_name'))
        
        return w

class SetTransitionDuration(BaseRequest):
    """Set the duration of the currently selected transition if supported.

    :Arguments:
       *duration*
            type: int
            Desired duration of the transition (in milliseconds).
    """

    fields = [
        'duration',
    ]

    category = 'transitions'
    
    def __init__(self, duration):
        super().__init__()
        self.name = 'SetTransitionDuration'
        self.dataout = {}
        self.dataout['duration'] = None

    @staticmethod
    def payload(duration):
        payload = {}
        payload['request-type'] = 'SetTransitionDuration'
        payload['duration'] = duration
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('duration'))
        
        return w

class GetTransitionDuration(BaseRequest):
    """Get the duration of the currently selected transition if supported.

    :Returns:
       *transition_duration*
            type: int
            Duration of the current transition (in milliseconds).
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetTransitionDuration'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionDuration'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class GetTransitionPosition(BaseRequest):
    """Get the position of the current transition.

    :Returns:
       *position*
            type: double
            current transition position. This value will be between 0.0 and 1.0. Note: Transition returns 1.0 when not active.
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'GetTransitionPosition'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'GetTransitionPosition'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'transitionName',
    ]

    category = 'transitions'
    
    def __init__(self, transitionName):
        super().__init__()
        self.name = 'GetTransitionSettings'
        self.dataout = {}
        self.dataout['transitionName'] = None

    @staticmethod
    def payload(transitionName):
        payload = {}
        payload['request-type'] = 'GetTransitionSettings'
        payload['transitionName'] = transitionName
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('transitionName'))
        
        return w

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

    fields = [
        'transitionName',
        'transitionSettings',
    ]

    category = 'transitions'
    
    def __init__(self, transitionName, transitionSettings):
        super().__init__()
        self.name = 'SetTransitionSettings'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('transitionName'))
            layout.add(QLabel('transitionSettings'))
        
        return w

class ReleaseTBar(BaseRequest):
    """Release the T-Bar (like a user releasing their mouse button after moving it).
*YOU MUST CALL THIS if you called `SetTBarPosition` with the `release` parameter set to `false`.*

    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'ReleaseTBar'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReleaseTBar'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

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

    fields = [
        'position',
        'release',
    ]

    category = 'transitions'
    
    def __init__(self, position, release=None):
        super().__init__()
        self.name = 'SetTBarPosition'
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

    @staticmethod
    def widget(changed):
        w = QWidget()
        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('position'))
            layout.add(QLabel('release'))
        
        return w

