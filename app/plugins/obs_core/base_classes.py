from qtstrap import *
from .obs_extension import ObsExtension


obs = ObsExtension()

class BaseRequest:
    def __init__(self):
        pass


class SourceSelector(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)

        self.setPlaceholderText('SourceSelector')

        self.refresh()

    def refresh(self):
        def cb(msg):
            sources = [s['name'] for s in msg['sources']]
            value = self.currentText()
            self.clear()
            self.addItems(sources)
            if value in sources:
                self.setCurrentText(value)
            self.changed()

        obs.get_source_list(cb)

class SceneSelector(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)
        self.refresh()

    def refresh(self):
        def cb(msg):
            scenes = [s['name'] for s in msg['scenes']]
            value = self.currentText()
            self.clear()
            self.addItems(scenes)
            if value in scenes:
                self.setCurrentText(value)
            self.changed()

        obs.get_scene_list(cb)



class FilterSelector(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)

        self.setPlaceholderText('FilterSelector')


class BoolSelector(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)
        self.addItems(['True', 'False'])