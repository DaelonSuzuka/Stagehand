from qtstrap import *
from qtpy.shiboken import isValid
from stagehand.sandbox import Sandbox
from .requests import requests


class UnimplementedField(QLabel):
    def refresh(self):
        pass
    
    def set_data(self, data):
        pass

    def get_data(self):
        return ''


class SceneSelector(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.setPlaceholderText('<scenes>')
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)

        self.refresh()

    def refresh(self):
        def cb(msg):
            if not isValid(self):
                return
            scenes = [s['name'] for s in msg['scenes']]
            value = self.currentText()
            with SignalBlocker(self):
                self.clear()
                self.addItems(scenes)
            if value in scenes:
                self.setCurrentText(value)
            self.changed()

        Sandbox().obs.GetSceneList(cb)

    def set_data(self, data):
        if data not in [self.itemText(i) for i in range(self.count())]:
            self.addItem(data)
        self.setCurrentText(data)

    def get_data(self):
        return self.currentText()


class SourceSelector(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.setPlaceholderText('<sources>')
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)

        self.refresh()

    def refresh(self):
        def cb(msg):
            if not isValid(self):
                return
            sources = [s['name'] for s in msg['sources']]
            value = self.currentText()
            with SignalBlocker(self):
                self.clear()
                self.addItems(sources)
            if value in sources:
                self.setCurrentText(value)
            self.changed()

        Sandbox().obs.GetSourcesList(cb)
        
    def set_data(self, data):
        if data not in [self.itemText(i) for i in range(self.count())]:
            self.addItem(data)
        self.setCurrentText(data)

    def get_data(self):
        return self.currentText()
    

class FilterSelector(QComboBox):
    def __init__(self, changed=None, source=None, parent=None):
        super().__init__(parent=parent)
        self.setPlaceholderText('<filters>')
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)
        if source:
            source.currentTextChanged.connect(self.refresh)

        self.setPlaceholderText('FilterSelector')

    def refresh(self, source=None):
        if source:
            def cb(msg):
                if not isValid(self):
                    return
                filters = [s['name'] for s in msg['filters']]
                value = self.currentText()
                with SignalBlocker(self):
                    self.clear()
                    self.addItems(filters)
                if value in filters:
                    self.setCurrentText(value)
                self.changed()

            Sandbox().obs.GetSourceFilters(source, cb)

    def set_data(self, data):
        if data not in [self.itemText(i) for i in range(self.count())]:
            self.addItem(data)
        self.setCurrentText(data)

    def get_data(self):
        return self.currentText()


class BoolSelector(QComboBox):
    def __init__(self, changed=None, parent=None):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.currentIndexChanged.connect(changed)
        self.addItems(['True', 'False'])

    def refresh(self):
        pass

    def set_data(self, data):
        self.setCurrentText(str(data))

    def get_data(self):
        if self.currentText() == 'True':
            return True
        else:
            return False


class StringSelector(QLineEdit):
    def __init__(self, changed=None, parent=None, placeholder=''):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.textChanged.connect(changed)

        self.placeholder = placeholder
        self.setPlaceholderText(placeholder)

    def refresh(self):
        pass

    def set_data(self, data):
        self.setText(str(data))

    def get_data(self):
        return self.text()


class IntSelector(QLineEdit):
    def __init__(self, changed=None, parent=None, placeholder=''):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.textChanged.connect(changed)

        self.placeholder = placeholder
        self.setPlaceholderText(placeholder)
        self.setValidator(QIntValidator(self))

    def refresh(self):
        pass

    def set_data(self, data):
        self.setText(str(data))

    def get_data(self):
        return self.text()


class DoubleSelector(QLineEdit):
    def __init__(self, changed=None, parent=None, placeholder=''):
        super().__init__(parent=parent)
        self.changed = changed
        if changed:
            self.textChanged.connect(changed)

        self.placeholder = placeholder
        self.setPlaceholderText(placeholder)
        self.setValidator(QDoubleValidator(self))

    def refresh(self):
        pass

    def set_data(self, data):
        self.setText(str(data))

    def get_data(self):
        return self.text()