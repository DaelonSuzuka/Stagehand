from qtstrap import *
from .base_classes import *


class SwitchScenesWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SwitchScenes':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ScenesChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'ScenesChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneCollectionChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneCollectionChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneCollectionListChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneCollectionListChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SwitchTransitionWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SwitchTransition':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class TransitionListChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'TransitionListChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class TransitionDurationChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'TransitionDurationChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class TransitionBeginWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'TransitionBegin':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class TransitionEndWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'TransitionEnd':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class TransitionVideoEndWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'TransitionVideoEnd':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ProfileChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'ProfileChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ProfileListChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'ProfileListChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StreamStartingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'StreamStarting':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StreamStartedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'StreamStarted':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StreamStoppingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'StreamStopping':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StreamStoppedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'StreamStopped':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StreamStatusWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'StreamStatus':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class RecordingStartingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'RecordingStarting':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class RecordingStartedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'RecordingStarted':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class RecordingStoppingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'RecordingStopping':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class RecordingStoppedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'RecordingStopped':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class RecordingPausedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'RecordingPaused':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class RecordingResumedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'RecordingResumed':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class VirtualCamStartedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'VirtualCamStarted':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class VirtualCamStoppedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'VirtualCamStopped':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ReplayStartingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'ReplayStarting':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ReplayStartedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'ReplayStarted':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ReplayStoppingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'ReplayStopping':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ReplayStoppedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'ReplayStopped':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class ExitingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'Exiting':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class HeartbeatWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'Heartbeat':
            return False
        return True

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

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'BroadcastCustomMessage':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceCreatedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceCreated':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceDestroyedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceDestroyed':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceVolumeChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceVolumeChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceMuteStateChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceMuteStateChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceAudioDeactivatedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceAudioDeactivated':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceAudioActivatedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceAudioActivated':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceAudioSyncOffsetChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceAudioSyncOffsetChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceAudioMixersChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceAudioMixersChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceRenamedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceRenamed':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceFilterAddedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceFilterAdded':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceFilterRemovedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceFilterRemoved':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceFilterVisibilityChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceFilterVisibilityChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceFiltersReorderedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceFiltersReordered':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaPlayingWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaPlaying':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaPausedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaPaused':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaRestartedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaRestarted':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaStoppedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaStopped':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaNextWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaNext':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaPreviousWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaPrevious':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaStartedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaStarted':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class MediaEndedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'MediaEnded':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SourceOrderChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SourceOrderChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneItemAddedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneItemAdded':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneItemRemovedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneItemRemoved':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneItemVisibilityChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneItemVisibilityChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneItemLockChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneItemLockChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneItemTransformChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneItemTransformChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneItemSelectedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneItemSelected':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class SceneItemDeselectedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'SceneItemDeselected':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class PreviewSceneChangedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'PreviewSceneChanged':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }


class StudioModeSwitchedWidget(QWidget):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed

        with CHBoxLayout(self, margins=0) as layout:
            pass

    def validate_event(self, event):
        if event['update-type'] != 'StudioModeSwitched':
            return False
        return True

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }



event_widgets = {
    'SwitchScenes': SwitchScenesWidget,
    'ScenesChanged': ScenesChangedWidget,
    'SceneCollectionChanged': SceneCollectionChangedWidget,
    'SceneCollectionListChanged': SceneCollectionListChangedWidget,
    'SwitchTransition': SwitchTransitionWidget,
    'TransitionListChanged': TransitionListChangedWidget,
    'TransitionDurationChanged': TransitionDurationChangedWidget,
    'TransitionBegin': TransitionBeginWidget,
    'TransitionEnd': TransitionEndWidget,
    'TransitionVideoEnd': TransitionVideoEndWidget,
    'ProfileChanged': ProfileChangedWidget,
    'ProfileListChanged': ProfileListChangedWidget,
    'StreamStarting': StreamStartingWidget,
    'StreamStarted': StreamStartedWidget,
    'StreamStopping': StreamStoppingWidget,
    'StreamStopped': StreamStoppedWidget,
    'StreamStatus': StreamStatusWidget,
    'RecordingStarting': RecordingStartingWidget,
    'RecordingStarted': RecordingStartedWidget,
    'RecordingStopping': RecordingStoppingWidget,
    'RecordingStopped': RecordingStoppedWidget,
    'RecordingPaused': RecordingPausedWidget,
    'RecordingResumed': RecordingResumedWidget,
    'VirtualCamStarted': VirtualCamStartedWidget,
    'VirtualCamStopped': VirtualCamStoppedWidget,
    'ReplayStarting': ReplayStartingWidget,
    'ReplayStarted': ReplayStartedWidget,
    'ReplayStopping': ReplayStoppingWidget,
    'ReplayStopped': ReplayStoppedWidget,
    'Exiting': ExitingWidget,
    'Heartbeat': HeartbeatWidget,
    'BroadcastCustomMessage': BroadcastCustomMessageWidget,
    'SourceCreated': SourceCreatedWidget,
    'SourceDestroyed': SourceDestroyedWidget,
    'SourceVolumeChanged': SourceVolumeChangedWidget,
    'SourceMuteStateChanged': SourceMuteStateChangedWidget,
    'SourceAudioDeactivated': SourceAudioDeactivatedWidget,
    'SourceAudioActivated': SourceAudioActivatedWidget,
    'SourceAudioSyncOffsetChanged': SourceAudioSyncOffsetChangedWidget,
    'SourceAudioMixersChanged': SourceAudioMixersChangedWidget,
    'SourceRenamed': SourceRenamedWidget,
    'SourceFilterAdded': SourceFilterAddedWidget,
    'SourceFilterRemoved': SourceFilterRemovedWidget,
    'SourceFilterVisibilityChanged': SourceFilterVisibilityChangedWidget,
    'SourceFiltersReordered': SourceFiltersReorderedWidget,
    'MediaPlaying': MediaPlayingWidget,
    'MediaPaused': MediaPausedWidget,
    'MediaRestarted': MediaRestartedWidget,
    'MediaStopped': MediaStoppedWidget,
    'MediaNext': MediaNextWidget,
    'MediaPrevious': MediaPreviousWidget,
    'MediaStarted': MediaStartedWidget,
    'MediaEnded': MediaEndedWidget,
    'SourceOrderChanged': SourceOrderChangedWidget,
    'SceneItemAdded': SceneItemAddedWidget,
    'SceneItemRemoved': SceneItemRemovedWidget,
    'SceneItemVisibilityChanged': SceneItemVisibilityChangedWidget,
    'SceneItemLockChanged': SceneItemLockChangedWidget,
    'SceneItemTransformChanged': SceneItemTransformChangedWidget,
    'SceneItemSelected': SceneItemSelectedWidget,
    'SceneItemDeselected': SceneItemDeselectedWidget,
    'PreviewSceneChanged': PreviewSceneChangedWidget,
    'StudioModeSwitched': StudioModeSwitchedWidget,
}
