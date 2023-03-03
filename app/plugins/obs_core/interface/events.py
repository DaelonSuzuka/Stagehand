

class BaseEvent:
    def __init__(self):
        pass


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

    name = 'SwitchScenes'
    category = 'scenes'

    def __init__(self, payload=None):
        super().__init__()


class ScenesChanged(BaseEvent):
    """

Note: This event is not fired when the scenes are reordered.

    :Returns:
        *scenes*
            type: Array<Scene>
            Scenes list.
    """

    name = 'ScenesChanged'
    category = 'scenes'

    def __init__(self, payload=None):
        super().__init__()


class SceneCollectionChanged(BaseEvent):
    """Triggered when switching to another scene collection or when renaming the current scene collection.

    :Returns:
        *sceneCollection*
            type: String
            Name of the new current scene collection.
    """

    name = 'SceneCollectionChanged'
    category = 'scenes'

    def __init__(self, payload=None):
        super().__init__()


class SceneCollectionListChanged(BaseEvent):
    """Triggered when a scene collection is created, added, renamed, or removed.

    :Returns:
        *sceneCollections*
            type: Array<Object>
            Scene collections list.
    """

    name = 'SceneCollectionListChanged'
    category = 'scenes'

    def __init__(self, payload=None):
        super().__init__()


class SwitchTransition(BaseEvent):
    """The active transition has been changed.

    :Returns:
        *transition_name*
            type: String
            The name of the new active transition.
    """

    name = 'SwitchTransition'
    category = 'transitions'

    def __init__(self, payload=None):
        super().__init__()


class TransitionListChanged(BaseEvent):
    """The list of available transitions has been modified.
Transitions have been added, removed, or renamed.

    :Returns:
        *transitions*
            type: Array<Object>
            Transitions list.
    """

    name = 'TransitionListChanged'
    category = 'transitions'

    def __init__(self, payload=None):
        super().__init__()


class TransitionDurationChanged(BaseEvent):
    """The active transition duration has been changed.

    :Returns:
        *new_duration*
            type: int
            New transition duration.
    """

    name = 'TransitionDurationChanged'
    category = 'transitions'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'TransitionBegin'
    category = 'transitions'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'TransitionEnd'
    category = 'transitions'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'TransitionVideoEnd'
    category = 'transitions'

    def __init__(self, payload=None):
        super().__init__()


class ProfileChanged(BaseEvent):
    """Triggered when switching to another profile or when renaming the current profile.

    :Returns:
        *profile*
            type: String
            Name of the new current profile.
    """

    name = 'ProfileChanged'
    category = 'profiles'

    def __init__(self, payload=None):
        super().__init__()


class ProfileListChanged(BaseEvent):
    """Triggered when a profile is created, added, renamed, or removed.

    :Returns:
        *profiles*
            type: Array<Object>
            Profiles list.
    """

    name = 'ProfileListChanged'
    category = 'profiles'

    def __init__(self, payload=None):
        super().__init__()


class StreamStarting(BaseEvent):
    """A request to start streaming has been issued.

    :Returns:
        *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    name = 'StreamStarting'
    category = 'streaming'

    def __init__(self, payload=None):
        super().__init__()


class StreamStarted(BaseEvent):
    """Streaming started successfully.

    """

    name = 'StreamStarted'
    category = 'streaming'

    def __init__(self, payload=None):
        super().__init__()


class StreamStopping(BaseEvent):
    """A request to stop streaming has been issued.

    :Returns:
        *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    name = 'StreamStopping'
    category = 'streaming'

    def __init__(self, payload=None):
        super().__init__()


class StreamStopped(BaseEvent):
    """Streaming stopped successfully.

    """

    name = 'StreamStopped'
    category = 'streaming'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'StreamStatus'
    category = 'streaming'

    def __init__(self, payload=None):
        super().__init__()


class RecordingStarting(BaseEvent):
    """

Note: `recordingFilename` is not provided in this event because this information
is not available at the time this event is emitted.

    """

    name = 'RecordingStarting'
    category = 'recording'

    def __init__(self, payload=None):
        super().__init__()


class RecordingStarted(BaseEvent):
    """Recording started successfully.

    :Returns:
        *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    name = 'RecordingStarted'
    category = 'recording'

    def __init__(self, payload=None):
        super().__init__()


class RecordingStopping(BaseEvent):
    """A request to stop recording has been issued.

    :Returns:
        *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    name = 'RecordingStopping'
    category = 'recording'

    def __init__(self, payload=None):
        super().__init__()


class RecordingStopped(BaseEvent):
    """Recording stopped successfully.

    :Returns:
        *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    name = 'RecordingStopped'
    category = 'recording'

    def __init__(self, payload=None):
        super().__init__()


class RecordingPaused(BaseEvent):
    """Current recording paused

    """

    name = 'RecordingPaused'
    category = 'recording'

    def __init__(self, payload=None):
        super().__init__()


class RecordingResumed(BaseEvent):
    """Current recording resumed

    """

    name = 'RecordingResumed'
    category = 'recording'

    def __init__(self, payload=None):
        super().__init__()


class VirtualCamStarted(BaseEvent):
    """Virtual cam started successfully.

    """

    name = 'VirtualCamStarted'
    category = 'virtual cam'

    def __init__(self, payload=None):
        super().__init__()


class VirtualCamStopped(BaseEvent):
    """Virtual cam stopped successfully.

    """

    name = 'VirtualCamStopped'
    category = 'virtual cam'

    def __init__(self, payload=None):
        super().__init__()


class ReplayStarting(BaseEvent):
    """A request to start the replay buffer has been issued.

    """

    name = 'ReplayStarting'
    category = 'replay buffer'

    def __init__(self, payload=None):
        super().__init__()


class ReplayStarted(BaseEvent):
    """Replay Buffer started successfully

    """

    name = 'ReplayStarted'
    category = 'replay buffer'

    def __init__(self, payload=None):
        super().__init__()


class ReplayStopping(BaseEvent):
    """A request to stop the replay buffer has been issued.

    """

    name = 'ReplayStopping'
    category = 'replay buffer'

    def __init__(self, payload=None):
        super().__init__()


class ReplayStopped(BaseEvent):
    """Replay Buffer stopped successfully

    """

    name = 'ReplayStopped'
    category = 'replay buffer'

    def __init__(self, payload=None):
        super().__init__()


class Exiting(BaseEvent):
    """OBS is exiting.

    """

    name = 'Exiting'
    category = 'other'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'Heartbeat'
    category = 'general'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'BroadcastCustomMessage'
    category = 'general'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceCreated'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceDestroyed'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceVolumeChanged'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceMuteStateChanged'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


class SourceAudioDeactivated(BaseEvent):
    """A source has removed audio.

    :Returns:
        *sourceName*
            type: String
            Source name
    """

    name = 'SourceAudioDeactivated'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


class SourceAudioActivated(BaseEvent):
    """A source has added audio.

    :Returns:
        *sourceName*
            type: String
            Source name
    """

    name = 'SourceAudioActivated'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceAudioSyncOffsetChanged'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


class SourceAudioMixersChanged(BaseEvent):
    """Audio mixer routing changed on a source.

    :Returns:
        *sourceName*
            type: String
            Source name
        *mixers*
            type: Array<Object>
            Routing status of the source for each audio mixer (array of 6 values)
        *hexMixersValue*
            type: String
            Raw mixer flags (little-endian, one bit per mixer) as an hexadecimal value
    """

    name = 'SourceAudioMixersChanged'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceRenamed'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceFilterAdded'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceFilterRemoved'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SourceFilterVisibilityChanged'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


class SourceFiltersReordered(BaseEvent):
    """Filters in a source have been reordered.

    :Returns:
        *sourceName*
            type: String
            Source name
        *filters*
            type: Array<Object>
            Ordered Filters list
    """

    name = 'SourceFiltersReordered'
    category = 'sources'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaPlaying'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaPaused'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaRestarted'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaStopped'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaNext'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaPrevious'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaStarted'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'MediaEnded'
    category = 'media'

    def __init__(self, payload=None):
        super().__init__()


class SourceOrderChanged(BaseEvent):
    """Scene items within a scene have been reordered.

    :Returns:
        *scene_name*
            type: String
            Name of the scene where items have been reordered.
        *scene_items*
            type: Array<Object>
            Ordered list of scene items
    """

    name = 'SourceOrderChanged'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SceneItemAdded'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SceneItemRemoved'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SceneItemVisibilityChanged'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SceneItemLockChanged'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SceneItemTransformChanged'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SceneItemSelected'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'SceneItemDeselected'
    category = 'scene items'

    def __init__(self, payload=None):
        super().__init__()


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

    name = 'PreviewSceneChanged'
    category = 'studio mode'

    def __init__(self, payload=None):
        super().__init__()


class StudioModeSwitched(BaseEvent):
    """Studio Mode has been enabled or disabled.

    :Returns:
        *new_state*
            type: boolean
            The new enabled state of Studio Mode.
    """

    name = 'StudioModeSwitched'
    category = 'studio mode'

    def __init__(self, payload=None):
        super().__init__()




events = {
    'SwitchScenes': SwitchScenes(),
    'ScenesChanged': ScenesChanged(),
    'SceneCollectionChanged': SceneCollectionChanged(),
    'SceneCollectionListChanged': SceneCollectionListChanged(),
    'SwitchTransition': SwitchTransition(),
    'TransitionListChanged': TransitionListChanged(),
    'TransitionDurationChanged': TransitionDurationChanged(),
    'TransitionBegin': TransitionBegin(),
    'TransitionEnd': TransitionEnd(),
    'TransitionVideoEnd': TransitionVideoEnd(),
    'ProfileChanged': ProfileChanged(),
    'ProfileListChanged': ProfileListChanged(),
    'StreamStarting': StreamStarting(),
    'StreamStarted': StreamStarted(),
    'StreamStopping': StreamStopping(),
    'StreamStopped': StreamStopped(),
    'StreamStatus': StreamStatus(),
    'RecordingStarting': RecordingStarting(),
    'RecordingStarted': RecordingStarted(),
    'RecordingStopping': RecordingStopping(),
    'RecordingStopped': RecordingStopped(),
    'RecordingPaused': RecordingPaused(),
    'RecordingResumed': RecordingResumed(),
    'VirtualCamStarted': VirtualCamStarted(),
    'VirtualCamStopped': VirtualCamStopped(),
    'ReplayStarting': ReplayStarting(),
    'ReplayStarted': ReplayStarted(),
    'ReplayStopping': ReplayStopping(),
    'ReplayStopped': ReplayStopped(),
    'Exiting': Exiting(),
    'Heartbeat': Heartbeat(),
    'BroadcastCustomMessage': BroadcastCustomMessage(),
    'SourceCreated': SourceCreated(),
    'SourceDestroyed': SourceDestroyed(),
    'SourceVolumeChanged': SourceVolumeChanged(),
    'SourceMuteStateChanged': SourceMuteStateChanged(),
    'SourceAudioDeactivated': SourceAudioDeactivated(),
    'SourceAudioActivated': SourceAudioActivated(),
    'SourceAudioSyncOffsetChanged': SourceAudioSyncOffsetChanged(),
    'SourceAudioMixersChanged': SourceAudioMixersChanged(),
    'SourceRenamed': SourceRenamed(),
    'SourceFilterAdded': SourceFilterAdded(),
    'SourceFilterRemoved': SourceFilterRemoved(),
    'SourceFilterVisibilityChanged': SourceFilterVisibilityChanged(),
    'SourceFiltersReordered': SourceFiltersReordered(),
    'MediaPlaying': MediaPlaying(),
    'MediaPaused': MediaPaused(),
    'MediaRestarted': MediaRestarted(),
    'MediaStopped': MediaStopped(),
    'MediaNext': MediaNext(),
    'MediaPrevious': MediaPrevious(),
    'MediaStarted': MediaStarted(),
    'MediaEnded': MediaEnded(),
    'SourceOrderChanged': SourceOrderChanged(),
    'SceneItemAdded': SceneItemAdded(),
    'SceneItemRemoved': SceneItemRemoved(),
    'SceneItemVisibilityChanged': SceneItemVisibilityChanged(),
    'SceneItemLockChanged': SceneItemLockChanged(),
    'SceneItemTransformChanged': SceneItemTransformChanged(),
    'SceneItemSelected': SceneItemSelected(),
    'SceneItemDeselected': SceneItemDeselected(),
    'PreviewSceneChanged': PreviewSceneChanged(),
    'StudioModeSwitched': StudioModeSwitched(),
}
