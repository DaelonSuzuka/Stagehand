from qtstrap import *
import json
from .items import TriggerItem
from .sandbox_trigger import SandboxTrigger


class ActionTrigger(QWidget):
    changed = Signal()

    def __init__(self, changed, run, trigger_type='sandbox', trigger='', owner=None):
        super().__init__()

        self.owner = owner
        self.type = QComboBox()

        self.trigger = SandboxTrigger(changed, run)
        self._changed = changed
        self._run = run
        self.data = None

        self.enabled = QAction('Custom Trigger', self, triggered=changed, checkable=True)

        for trigger in TriggerItem.__subclasses__():
            self.type.addItem(trigger.name)

        # for name, trigger in self.triggers.items():
        #     self.type.addItem(name)

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.type_changed)

        self.trigger_box = CHBoxLayout(margins=0)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(QLabel("Trigger:", minimumWidth=60))
            layout.add(self.type)
            layout.add(self.trigger_box, 1)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction(QAction('Copy Trigger', self, triggered=self.copy))
        menu.addAction(QAction('Paste Trigger', self, triggered=self.paste))
        menu.addAction(QAction('Reset Trigger', self, triggered=self.reset))
        menu.exec_(event.globalPos())

    def type_changed(self):
        if self.trigger:
            self.trigger.deleteLater()
            self.trigger = None
        trigger_class = TriggerItem.get_item(self.type.currentText())
        self.trigger = trigger_class(self._changed, self._run, self.owner)
        if self.data:
            self.trigger.set_data(self.data['trigger'])
        self.trigger_box.add(self.trigger)

    def copy(self):
        data = json.dumps(self.get_data())
        QClipboard().setText(data)

    def paste(self):
        data = json.loads(QClipboard().text())
        self.set_data(data)

    def reset(self):
        self.type.setCurrentText('keyboard')

    def set_data(self, data):
        if 'trigger' in data:
            self.data = data
            if 'trigger_type' not in data['trigger']:
                data['trigger']['trigger_type'] = 'keyboard'
            self.type.setCurrentText(data['trigger']['trigger_type'])
            
            self.type_changed()

            if 'enabled' in data['trigger']:
                self.enabled.setChecked(data['trigger']['enabled'])

    def get_data(self):
        return {
            'trigger': {
                'enabled': self.enabled.isChecked(),
                'trigger_type': self.type.currentText(),
                **self.trigger.get_data(),
            }
        }