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

    name = 'SwitchScenes'
    category = 'scenes'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['sources'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SwitchScenes'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SwitchScenes'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scenes'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ScenesChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'ScenesChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SceneCollectionChanged(BaseEvent):
    """Triggered when switching to another scene collection or when renaming the current scene collection.

    :Returns:
        *sceneCollection*
            type: String
            Name of the new current scene collection.
    """

    name = 'SceneCollectionChanged'
    category = 'scenes'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sceneCollection'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneCollectionChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneCollectionChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SceneCollectionListChanged(BaseEvent):
    """Triggered when a scene collection is created, added, renamed, or removed.

    :Returns:
        *sceneCollections*
            type: Array<Object>
            Scene collections list.
    """

    name = 'SceneCollectionListChanged'
    category = 'scenes'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sceneCollections'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneCollectionListChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneCollectionListChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SwitchTransition(BaseEvent):
    """The active transition has been changed.

    :Returns:
        *transition_name*
            type: String
            The name of the new active transition.
    """

    name = 'SwitchTransition'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['transition-name'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SwitchTransition'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SwitchTransition'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['transitions'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionListChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'TransitionListChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class TransitionDurationChanged(BaseEvent):
    """The active transition duration has been changed.

    :Returns:
        *new_duration*
            type: int
            New transition duration.
    """

    name = 'TransitionDurationChanged'
    category = 'transitions'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['new-duration'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionDurationChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'TransitionDurationChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['type'] = None
        self.datain['duration'] = None
        self.datain['from-scene'] = None
        self.datain['to-scene'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionBegin'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'TransitionBegin'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['type'] = None
        self.datain['duration'] = None
        self.datain['to-scene'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionEnd'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'TransitionEnd'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['name'] = None
        self.datain['type'] = None
        self.datain['duration'] = None
        self.datain['from-scene'] = None
        self.datain['to-scene'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'TransitionVideoEnd'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'TransitionVideoEnd'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ProfileChanged(BaseEvent):
    """Triggered when switching to another profile or when renaming the current profile.

    :Returns:
        *profile*
            type: String
            Name of the new current profile.
    """

    name = 'ProfileChanged'
    category = 'profiles'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['profile'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ProfileChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'ProfileChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ProfileListChanged(BaseEvent):
    """Triggered when a profile is created, added, renamed, or removed.

    :Returns:
        *profiles*
            type: Array<Object>
            Profiles list.
    """

    name = 'ProfileListChanged'
    category = 'profiles'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['profiles'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ProfileListChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'ProfileListChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StreamStarting(BaseEvent):
    """A request to start streaming has been issued.

    :Returns:
        *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    name = 'StreamStarting'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['preview-only'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStarting'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'StreamStarting'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StreamStarted(BaseEvent):
    """Streaming started successfully.

    """

    name = 'StreamStarted'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStarted'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'StreamStarted'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StreamStopping(BaseEvent):
    """A request to stop streaming has been issued.

    :Returns:
        *preview_only*
            type: boolean
            Always false (retrocompatibility).
    """

    name = 'StreamStopping'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['preview-only'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStopping'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'StreamStopping'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StreamStopped(BaseEvent):
    """Streaming stopped successfully.

    """

    name = 'StreamStopped'
    category = 'streaming'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStopped'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'StreamStopped'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['streaming'] = None
        self.datain['recording'] = None
        self.datain['replay-buffer-active'] = None
        self.datain['bytes-per-sec'] = None
        self.datain['kbits-per-sec'] = None
        self.datain['strain'] = None
        self.datain['total-stream-time'] = None
        self.datain['num-total-frames'] = None
        self.datain['num-dropped-frames'] = None
        self.datain['fps'] = None
        self.datain['render-total-frames'] = None
        self.datain['render-missed-frames'] = None
        self.datain['output-total-frames'] = None
        self.datain['output-skipped-frames'] = None
        self.datain['average-frame-time'] = None
        self.datain['cpu-usage'] = None
        self.datain['memory-usage'] = None
        self.datain['free-disk-space'] = None
        self.datain['preview-only'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StreamStatus'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'StreamStatus'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class RecordingStarting(BaseEvent):
    """

Note: `recordingFilename` is not provided in this event because this information
is not available at the time this event is emitted.

    """

    name = 'RecordingStarting'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStarting'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'RecordingStarting'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class RecordingStarted(BaseEvent):
    """Recording started successfully.

    :Returns:
        *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    name = 'RecordingStarted'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['recordingFilename'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStarted'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'RecordingStarted'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class RecordingStopping(BaseEvent):
    """A request to stop recording has been issued.

    :Returns:
        *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    name = 'RecordingStopping'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['recordingFilename'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStopping'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'RecordingStopping'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class RecordingStopped(BaseEvent):
    """Recording stopped successfully.

    :Returns:
        *recordingFilename*
            type: String
            Absolute path to the file of the current recording.
    """

    name = 'RecordingStopped'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['recordingFilename'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingStopped'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'RecordingStopped'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class RecordingPaused(BaseEvent):
    """Current recording paused

    """

    name = 'RecordingPaused'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingPaused'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'RecordingPaused'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class RecordingResumed(BaseEvent):
    """Current recording resumed

    """

    name = 'RecordingResumed'
    category = 'recording'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'RecordingResumed'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'RecordingResumed'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ReplayStarting(BaseEvent):
    """A request to start the replay buffer has been issued.

    """

    name = 'ReplayStarting'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStarting'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'ReplayStarting'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ReplayStarted(BaseEvent):
    """Replay Buffer started successfully

    """

    name = 'ReplayStarted'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStarted'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'ReplayStarted'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ReplayStopping(BaseEvent):
    """A request to stop the replay buffer has been issued.

    """

    name = 'ReplayStopping'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStopping'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'ReplayStopping'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class ReplayStopped(BaseEvent):
    """Replay Buffer stopped successfully

    """

    name = 'ReplayStopped'
    category = 'replay buffer'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'ReplayStopped'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'ReplayStopped'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class Exiting(BaseEvent):
    """OBS is exiting.

    """

    name = 'Exiting'
    category = 'other'
    fields = []

    def __init__(self):
        super().__init__()

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'Exiting'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'Exiting'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['pulse'] = None
        self.datain['current-profile'] = None
        self.datain['current-scene'] = None
        self.datain['streaming'] = None
        self.datain['total-stream-time'] = None
        self.datain['total-stream-bytes'] = None
        self.datain['total-stream-frames'] = None
        self.datain['recording'] = None
        self.datain['total-record-time'] = None
        self.datain['total-record-bytes'] = None
        self.datain['total-record-frames'] = None
        self.datain['stats'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'Heartbeat'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'Heartbeat'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['realm'] = None
        self.datain['data'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'BroadcastCustomMessage'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'BroadcastCustomMessage'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None
        self.datain['sourceKind'] = None
        self.datain['sourceSettings'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceCreated'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceCreated'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceType'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceDestroyed'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceDestroyed'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['volume'] = None
        self.datain['volumeDb'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceVolumeChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceVolumeChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['muted'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceMuteStateChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceMuteStateChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SourceAudioDeactivated(BaseEvent):
    """A source has removed audio.

    :Returns:
        *sourceName*
            type: String
            Source name
    """

    name = 'SourceAudioDeactivated'
    category = 'sources'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioDeactivated'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceAudioDeactivated'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class SourceAudioActivated(BaseEvent):
    """A source has added audio.

    :Returns:
        *sourceName*
            type: String
            Source name
    """

    name = 'SourceAudioActivated'
    category = 'sources'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioActivated'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceAudioActivated'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['syncOffset'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioSyncOffsetChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceAudioSyncOffsetChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['mixers'] = None
        self.datain['hexMixersValue'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceAudioMixersChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceAudioMixersChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['previousName'] = None
        self.datain['newName'] = None
        self.datain['sourceType'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceRenamed'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceRenamed'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['filterName'] = None
        self.datain['filterType'] = None
        self.datain['filterSettings'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFilterAdded'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceFilterAdded'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['filterName'] = None
        self.datain['filterType'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFilterRemoved'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceFilterRemoved'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['filterName'] = None
        self.datain['filterEnabled'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFilterVisibilityChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceFilterVisibilityChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['filters'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceFiltersReordered'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceFiltersReordered'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaPlaying'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaPlaying'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaPaused'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaPaused'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaRestarted'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaRestarted'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaStopped'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaStopped'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaNext'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaNext'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaPrevious'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaPrevious'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaStarted'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaStarted'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['sourceName'] = None
        self.datain['sourceKind'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'MediaEnded'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'MediaEnded'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['scene-items'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SourceOrderChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SourceOrderChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['item-name'] = None
        self.datain['item-id'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemAdded'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneItemAdded'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['item-name'] = None
        self.datain['item-id'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemRemoved'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneItemRemoved'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['item-name'] = None
        self.datain['item-id'] = None
        self.datain['item-visible'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemVisibilityChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneItemVisibilityChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['item-name'] = None
        self.datain['item-id'] = None
        self.datain['item-locked'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemLockChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneItemLockChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['item-name'] = None
        self.datain['item-id'] = None
        self.datain['transform'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemTransformChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneItemTransformChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['item-name'] = None
        self.datain['item-id'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemSelected'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneItemSelected'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['item-name'] = None
        self.datain['item-id'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'SceneItemDeselected'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'SceneItemDeselected'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


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
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['scene-name'] = None
        self.datain['sources'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'PreviewSceneChanged'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'PreviewSceneChanged'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
            }


class StudioModeSwitched(BaseEvent):
    """Studio Mode has been enabled or disabled.

    :Returns:
        *new_state*
            type: boolean
            The new enabled state of Studio Mode.
    """

    name = 'StudioModeSwitched'
    category = 'studio mode'
    fields = []

    def __init__(self):
        super().__init__()
        self.datain = {}
        self.datain['new-state'] = None

    @staticmethod
    def payload():
        payload = {}
        payload['request-type'] = 'StudioModeSwitched'
        return payload

    class Widget(QWidget):
        def __init__(self, changed=None, parent=None):
            super().__init__(parent=parent)
            self.changed = changed

            with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
                layout.add(QLabel('[ request has no fields ]'))

        def payload(self):
            payload = {}
            payload['request-type'] = 'StudioModeSwitched'
            return payload

        def refresh(self):
            return

        def from_dict(self, data):
            self._data = data

        def to_dict(self):
            return {
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