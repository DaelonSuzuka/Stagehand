from qtstrap import *
import abc
import json


class TriggerItem:
    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}

    @classmethod
    def get_item(cls, name):
        return cls.get_subclasses()[name]

    @abc.abstractmethod
    def __init__(self, changed) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def from_dict(self, data: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    def reset(self):
        pass


class SandboxTrigger(QWidget, TriggerItem):
    name = 'sandbox'
    triggered = Signal()

    def __init__(self, changed, run, parent=None):
        super().__init__(parent=parent)

        self.trigger = QLineEdit()
        self.trigger.textChanged.connect(changed)
        
        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.trigger)

    def reset(self):
        self.trigger.clear()
        
    def from_dict(self, data: dict):
        if 'trigger' in data:
            self.trigger.setText(data['trigger'])

    def to_dict(self):
        return {
            'trigger': self.trigger.text()
        }


class ActionTrigger(QWidget):
    changed = Signal()

    def __init__(self, changed, run, trigger_type='sandbox', trigger='', parent=None):
        super().__init__(parent=parent)

        self.type = QComboBox()

        self.trigger = SandboxTrigger(changed, run)
        self._changed = changed
        self._run = run
        self.data = None

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_menu)
        self.type.setContextMenuPolicy(Qt.CustomContextMenu)
        self.type.customContextMenuRequested.connect(self.show_menu)

        self.enabled = QAction('Custom Trigger', self, triggered=changed, checkable=True)

        for trigger in TriggerItem.__subclasses__():
            self.type.addItem(trigger.name)

        # for name, trigger in self.triggers.items():
        #     self.type.addItem(name)

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.type_changed)

        self.trigger_box = CHBoxLayout(margins=(0,0,0,0))

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.trigger_box, 1)
            layout.add(VLine())

    def show_menu(self, pos) -> None:
        menu = QMenu()
        menu.addAction(QAction('Copy Trigger', self, triggered=self.copy))
        menu.addAction(QAction('Paste Trigger', self, triggered=self.paste))
        menu.addAction(QAction('Reset Trigger', self, triggered=self.reset))
        menu.exec_(self.mapToGlobal(pos))

    def type_changed(self):
        if self.trigger:
            self.trigger.deleteLater()
            self.trigger = None
        trigger = TriggerItem.get_item(self.type.currentText())
        self.trigger = trigger(self._changed, self._run)
        if self.data:
            self.trigger.from_dict(self.data['trigger'])
        self.trigger_box.add(self.trigger)

    def copy(self):
        data = json.dumps(self.to_dict())
        QClipboard().setText(data)

    def paste(self):
        data = json.loads(QClipboard().text())
        self.set_data(data)

    def reset(self):
        self.type.setCurrentText('sandbox')

    def set_data(self, data):
        if 'trigger' in data:
            self.data = data
            if 'trigger_type' not in data['trigger']:
                data['trigger']['trigger_type'] = 'sandbox'
            self.type.setCurrentText(data['trigger']['trigger_type'])
            
            self.type_changed()

            if 'enabled' in data['trigger']:
                self.enabled.setChecked(data['trigger']['enabled'])

    def to_dict(self):
        return {
            'trigger': {
                'enabled': self.enabled.isChecked(),
                'trigger_type': self.type.currentText(),
                **self.trigger.to_dict(),
            }
        }