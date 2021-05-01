from .base_classes import *
from qtstrap import *


categories = [
    'scenes',
    'transitions',
    'profiles',
    'streaming',
    'recording',
    'replay buffer',
    'other',
    'general',
    'sources',
    'media',
    'scene items',
    'studio mode',
]


class SwitchScenes(BaseEvent):
    """Indicates a scene change.

    :Returns:
       *scene_name*
            type: String
            The new scene.
       *sources*
            type: Array<SceneItem>
            List of scene items in the new scene. Same specification as [`GetCurrentScene`](#getcurrentscene).
    """

    fields = [
    ]

    category = 'scenes'
    
    def __init__(self):
        super().__init__()
        self.name = 'SwitchScenes'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SwitchScenes'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ScenesChanged(BaseEvent):
    """

Note: This event is not fired when the scenes are reordered.

    :Returns:
       *scenes*
            type: Array<Scene>
            Scenes list.
    """

    fields = [
    ]

    category = 'scenes'
    
    def __init__(self):
        super().__init__()
        self.name = 'ScenesChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ScenesChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneCollectionChanged(BaseEvent):
    """Triggered when switching to another scene collection or when renaming the current scene collection.

    :Returns:
       *sceneCollection*
            type: String
            Name of the new current scene collection.
    """

    fields = [
    ]

    category = 'scenes'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneCollectionChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneCollectionChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneCollectionListChanged(BaseEvent):
    """Triggered when a scene collection is created, added, renamed, or removed.

    :Returns:
       *sceneCollections*
            type: Array<Object>
            Scene collections list.
       *sceneCollections.*.name*
            type: String
            Scene collection name.
    """

    fields = [
    ]

    category = 'scenes'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneCollectionListChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneCollectionListChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SwitchTransition(BaseEvent):
    """The active transition has been changed.

    :Returns:
       *transition_name*
            type: String
            The name of the new active transition.
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'SwitchTransition'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SwitchTransition'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class TransitionListChanged(BaseEvent):
    """The list of available transitions has been modified.
Transitions have been added, removed, or renamed.

    :Returns:
       *transitions*
            type: Array<Object>
            Transitions list.
       *transitions.*.name*
            type: String
            Transition name.
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'TransitionListChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionListChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class TransitionDurationChanged(BaseEvent):
    """The active transition duration has been changed.

    :Returns:
       *new_duration*
            type: int
            New transition duration.
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'TransitionDurationChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionDurationChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class TransitionBegin(BaseEvent):
    """A transition (other than "cut") has begun.

    :Returns:
       *name*
            type: String
            Transition name.
       *type*
            type: String
            Transition type.
       *duration*
            type: int
            Transition duration (in milliseconds). Will be -1 for any transition with a fixed duration, such as a Stinger, due to limitations of the OBS API.
       *from_scene*
            type: String (optional)
            Source scene of the transition
       *to_scene*
            type: String
            Destination scene of the transition
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'TransitionBegin'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionBegin'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class TransitionEnd(BaseEvent):
    """A transition (other than "cut") has ended.
Note: The `from-scene` field is not available in TransitionEnd.

    :Returns:
       *name*
            type: String
            Transition name.
       *type*
            type: String
            Transition type.
       *duration*
            type: int
            Transition duration (in milliseconds).
       *to_scene*
            type: String
            Destination scene of the transition
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'TransitionEnd'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionEnd'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class TransitionVideoEnd(BaseEvent):
    """A stinger transition has finished playing its video.

    :Returns:
       *name*
            type: String
            Transition name.
       *type*
            type: String
            Transition type.
       *duration*
            type: int
            Transition duration (in milliseconds).
       *from_scene*
            type: String (optional)
            Source scene of the transition
       *to_scene*
            type: String
            Destination scene of the transition
    """

    fields = [
    ]

    category = 'transitions'
    
    def __init__(self):
        super().__init__()
        self.name = 'TransitionVideoEnd'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionVideoEnd'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ProfileChanged(BaseEvent):
    """Triggered when switching to another profile or when renaming the current profile.

    :Returns:
       *profile*
            type: String
            Name of the new current profile.
    """

    fields = [
    ]

    category = 'profiles'
    
    def __init__(self):
        super().__init__()
        self.name = 'ProfileChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ProfileChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ProfileListChanged(BaseEvent):
    """Triggered when a profile is created, added, renamed, or removed.

    :Returns:
       *profiles*
            type: Array<Object>
            Profiles list.
       *profiles.*.name*
            type: String
            Profile name.
    """

    fields = [
    ]

    category = 'profiles'
    
    def __init__(self):
        super().__init__()
        self.name = 'ProfileListChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ProfileListChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StreamStarting(BaseEvent):
    """A request to start streaming has been issued.

    :Returns:
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'StreamStarting'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStarting'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StreamStarted(BaseEvent):
    """Streaming started successfully.

    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'StreamStarted'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStarted'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StreamStopping(BaseEvent):
    """A request to stop streaming has been issued.

    :Returns:
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'StreamStopping'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStopping'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StreamStopped(BaseEvent):
    """Streaming stopped successfully.

    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'StreamStopped'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStopped'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StreamStatus(BaseEvent):
    """Emitted every 2 seconds when stream is active.

    :Returns:
       *streaming*
            type: boolean
            Current streaming state.
       *recording*
            type: boolean
            Current recording state.
       *replay_buffer_active*
            type: boolean
            Replay Buffer status
       *bytes_per_sec*
            type: int
            Amount of data per second (in bytes) transmitted by the stream encoder.
       *kbits_per_sec*
            type: int
            Amount of data per second (in kilobits) transmitted by the stream encoder.
       *strain*
            type: double
            Percentage of dropped frames.
       *total_stream_time*
            type: int
            Total time (in seconds) since the stream started.
       *num_total_frames*
            type: int
            Total number of frames transmitted since the stream started.
       *num_dropped_frames*
            type: int
            Number of frames dropped by the encoder since the stream started.
       *fps*
            type: double
            Current framerate.
       *render_total_frames*
            type: int
            Number of frames rendered
       *render_missed_frames*
            type: int
            Number of frames missed due to rendering lag
       *output_total_frames*
            type: int
            Number of frames outputted
       *output_skipped_frames*
            type: int
            Number of frames skipped due to encoding lag
       *average_frame_time*
            type: double
            Average frame time (in milliseconds)
       *cpu_usage*
            type: double
            Current CPU usage (percentage)
       *memory_usage*
            type: double
            Current RAM usage (in megabytes)
       *free_disk_space*
            type: double
            Free recording disk space (in megabytes)
       *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    fields = [
    ]

    category = 'streaming'
    
    def __init__(self):
        super().__init__()
        self.name = 'StreamStatus'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStatus'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class RecordingStarting(BaseEvent):
    """

Note: `recordingFilename` is not provided in this event because this information
is not available at the time this event is emitted.

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'RecordingStarting'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStarting'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class RecordingStarted(BaseEvent):
    """Recording started successfully.

    :Returns:
       *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'RecordingStarted'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStarted'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class RecordingStopping(BaseEvent):
    """A request to stop recording has been issued.

    :Returns:
       *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'RecordingStopping'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStopping'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class RecordingStopped(BaseEvent):
    """Recording stopped successfully.

    :Returns:
       *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'RecordingStopped'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStopped'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class RecordingPaused(BaseEvent):
    """Current recording paused

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'RecordingPaused'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingPaused'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class RecordingResumed(BaseEvent):
    """Current recording resumed

    """

    fields = [
    ]

    category = 'recording'
    
    def __init__(self):
        super().__init__()
        self.name = 'RecordingResumed'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingResumed'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ReplayStarting(BaseEvent):
    """A request to start the replay buffer has been issued.

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'ReplayStarting'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStarting'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ReplayStarted(BaseEvent):
    """Replay Buffer started successfully

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'ReplayStarted'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStarted'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ReplayStopping(BaseEvent):
    """A request to stop the replay buffer has been issued.

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'ReplayStopping'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStopping'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class ReplayStopped(BaseEvent):
    """Replay Buffer stopped successfully

    """

    fields = [
    ]

    category = 'replay buffer'
    
    def __init__(self):
        super().__init__()
        self.name = 'ReplayStopped'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStopped'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class Exiting(BaseEvent):
    """OBS is exiting.

    """

    fields = [
    ]

    category = 'other'
    
    def __init__(self):
        super().__init__()
        self.name = 'Exiting'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'Exiting'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class Heartbeat(BaseEvent):
    """Emitted every 2 seconds after enabling it by calling SetHeartbeat.

    :Returns:
       *pulse*
            type: boolean
            Toggles between every JSON message as an "I am alive" indicator.
       *current_profile*
            type: string (optional)
            Current active profile.
       *current_scene*
            type: string (optional)
            Current active scene.
       *streaming*
            type: boolean (optional)
            Current streaming state.
       *total_stream_time*
            type: int (optional)
            Total time (in seconds) since the stream started.
       *total_stream_bytes*
            type: int (optional)
            Total bytes sent since the stream started.
       *total_stream_frames*
            type: int (optional)
            Total frames streamed since the stream started.
       *recording*
            type: boolean (optional)
            Current recording state.
       *total_record_time*
            type: int (optional)
            Total time (in seconds) since recording started.
       *total_record_bytes*
            type: int (optional)
            Total bytes recorded since the recording started.
       *total_record_frames*
            type: int (optional)
            Total frames recorded since the recording started.
       *stats*
            type: OBSStats
            OBS Stats
    """

    fields = [
    ]

    category = 'general'
    
    def __init__(self):
        super().__init__()
        self.name = 'Heartbeat'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'Heartbeat'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class BroadcastCustomMessage(BaseEvent):
    """A custom broadcast message, sent by the server, requested by one of the websocket clients.

    :Returns:
       *realm*
            type: String
            Identifier provided by the sender
       *data*
            type: Object
            User-defined data
    """

    fields = [
    ]

    category = 'general'
    
    def __init__(self):
        super().__init__()
        self.name = 'BroadcastCustomMessage'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'BroadcastCustomMessage'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceCreated(BaseEvent):
    """A source has been created. A source can be an input, a scene or a transition.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceType*
            type: String
            Source type. Can be "input", "scene", "transition" or "filter".
       *sourceKind*
            type: String
            Source kind.
       *sourceSettings*
            type: Object
            Source settings
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceCreated'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceCreated'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceDestroyed(BaseEvent):
    """A source has been destroyed/removed. A source can be an input, a scene or a transition.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceType*
            type: String
            Source type. Can be "input", "scene", "transition" or "filter".
       *sourceKind*
            type: String
            Source kind.
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceDestroyed'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceDestroyed'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceVolumeChanged(BaseEvent):
    """The volume of a source has changed.

    :Returns:
       *sourceName*
            type: String
            Source name
       *volume*
            type: float
            Source volume
       *volumeDb*
            type: float
            Source volume in Decibel
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceVolumeChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceVolumeChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceMuteStateChanged(BaseEvent):
    """A source has been muted or unmuted.

    :Returns:
       *sourceName*
            type: String
            Source name
       *muted*
            type: boolean
            Mute status of the source
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceMuteStateChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceMuteStateChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceAudioDeactivated(BaseEvent):
    """A source has removed audio.

    :Returns:
       *sourceName*
            type: String
            Source name
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceAudioDeactivated'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioDeactivated'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceAudioActivated(BaseEvent):
    """A source has added audio.

    :Returns:
       *sourceName*
            type: String
            Source name
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceAudioActivated'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioActivated'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceAudioSyncOffsetChanged(BaseEvent):
    """The audio sync offset of a source has changed.

    :Returns:
       *sourceName*
            type: String
            Source name
       *syncOffset*
            type: int
            Audio sync offset of the source (in nanoseconds)
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceAudioSyncOffsetChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioSyncOffsetChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceAudioMixersChanged(BaseEvent):
    """Audio mixer routing changed on a source.

    :Returns:
       *sourceName*
            type: String
            Source name
       *mixers*
            type: Array<Object>
            Routing status of the source for each audio mixer (array of 6 values)
       *mixers.*.id*
            type: int
            Mixer number
       *mixers.*.enabled*
            type: boolean
            Routing status
       *hexMixersValue*
            type: String
            Raw mixer flags (little-endian, one bit per mixer) as an hexadecimal value
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceAudioMixersChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioMixersChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceRenamed(BaseEvent):
    """A source has been renamed.

    :Returns:
       *previousName*
            type: String
            Previous source name
       *newName*
            type: String
            New source name
       *sourceType*
            type: String
            Type of source (input, scene, filter, transition)
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceRenamed'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceRenamed'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceFilterAdded(BaseEvent):
    """A filter was added to a source.

    :Returns:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Filter name
       *filterType*
            type: String
            Filter type
       *filterSettings*
            type: Object
            Filter settings
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceFilterAdded'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFilterAdded'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceFilterRemoved(BaseEvent):
    """A filter was removed from a source.

    :Returns:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Filter name
       *filterType*
            type: String
            Filter type
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceFilterRemoved'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFilterRemoved'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceFilterVisibilityChanged(BaseEvent):
    """The visibility/enabled state of a filter changed

    :Returns:
       *sourceName*
            type: String
            Source name
       *filterName*
            type: String
            Filter name
       *filterEnabled*
            type: Boolean
            New filter state
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceFilterVisibilityChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFilterVisibilityChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceFiltersReordered(BaseEvent):
    """Filters in a source have been reordered.

    :Returns:
       *sourceName*
            type: String
            Source name
       *filters*
            type: Array<Object>
            Ordered Filters list
       *filters.*.name*
            type: String
            Filter name
       *filters.*.type*
            type: String
            Filter type
       *filters.*.enabled*
            type: boolean
            Filter visibility status
    """

    fields = [
    ]

    category = 'sources'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceFiltersReordered'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFiltersReordered'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaPlaying(BaseEvent):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaPlaying'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaPlaying'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaPaused(BaseEvent):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaPaused'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaPaused'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaRestarted(BaseEvent):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaRestarted'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaRestarted'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaStopped(BaseEvent):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaStopped'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaStopped'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaNext(BaseEvent):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaNext'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaNext'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaPrevious(BaseEvent):
    """

Note: This event is only emitted when something actively controls the media/VLC source. In other words, the source will never emit this on its own naturally.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaPrevious'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaPrevious'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaStarted(BaseEvent):
    """

Note: These events are emitted by the OBS sources themselves. For example when the media file starts playing. The behavior depends on the type of media source being used.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaStarted'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaStarted'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class MediaEnded(BaseEvent):
    """

Note: These events are emitted by the OBS sources themselves. For example when the media file ends. The behavior depends on the type of media source being used.

    :Returns:
       *sourceName*
            type: String
            Source name
       *sourceKind*
            type: String
            The ID type of the source (Eg. `vlc_source` or `ffmpeg_source`)
    """

    fields = [
    ]

    category = 'media'
    
    def __init__(self):
        super().__init__()
        self.name = 'MediaEnded'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaEnded'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SourceOrderChanged(BaseEvent):
    """Scene items within a scene have been reordered.

    :Returns:
       *scene_name*
            type: String
            Name of the scene where items have been reordered.
       *scene_items*
            type: Array<Object>
            Ordered list of scene items
       *scene_items.*.source_name*
            type: String
            Item source name
       *scene_items.*.item_id*
            type: int
            Scene item unique ID
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SourceOrderChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceOrderChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneItemAdded(BaseEvent):
    """A scene item has been added to a scene.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item added to the scene.
       *item_id*
            type: int
            Scene item ID
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneItemAdded'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemAdded'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneItemRemoved(BaseEvent):
    """A scene item has been removed from a scene.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item removed from the scene.
       *item_id*
            type: int
            Scene item ID
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneItemRemoved'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemRemoved'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneItemVisibilityChanged(BaseEvent):
    """A scene item's visibility has been toggled.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *item_visible*
            type: boolean
            New visibility state of the item.
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneItemVisibilityChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemVisibilityChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneItemLockChanged(BaseEvent):
    """A scene item's locked status has been toggled.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *item_locked*
            type: boolean
            New locked state of the item.
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneItemLockChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemLockChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneItemTransformChanged(BaseEvent):
    """A scene item's transform has been changed.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Scene item ID
       *transform*
            type: SceneItemTransform
            Scene item transform properties
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneItemTransformChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemTransformChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneItemSelected(BaseEvent):
    """A scene item is selected.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Name of the item in the scene.
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneItemSelected'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemSelected'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class SceneItemDeselected(BaseEvent):
    """A scene item is deselected.

    :Returns:
       *scene_name*
            type: String
            Name of the scene.
       *item_name*
            type: String
            Name of the item in the scene.
       *item_id*
            type: int
            Name of the item in the scene.
    """

    fields = [
    ]

    category = 'scene items'
    
    def __init__(self):
        super().__init__()
        self.name = 'SceneItemDeselected'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemDeselected'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class PreviewSceneChanged(BaseEvent):
    """The selected preview scene has changed (only available in Studio Mode).

    :Returns:
       *scene_name*
            type: String
            Name of the scene being previewed.
       *sources*
            type: Array<SceneItem>
            List of sources composing the scene. Same specification as [`GetCurrentScene`](#getcurrentscene).
    """

    fields = [
    ]

    category = 'studio mode'
    
    def __init__(self):
        super().__init__()
        self.name = 'PreviewSceneChanged'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'PreviewSceneChanged'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

class StudioModeSwitched(BaseEvent):
    """Studio Mode has been enabled or disabled.

    :Returns:
       *new_state*
            type: boolean
            The new enabled state of Studio Mode.
    """

    fields = [
    ]

    category = 'studio mode'
    
    def __init__(self):
        super().__init__()
        self.name = 'StudioModeSwitched'

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StudioModeSwitched'
        return payload

    @staticmethod
    def widget(changed):
        w = QWidget()
        
        return w

