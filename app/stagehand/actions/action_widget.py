from qtstrap import *
import qtawesome as qta
import json
from .action_trigger import ActionTrigger
from .action_filter import ActionFilter
from .items import ActionItem


class Action(QWidget):
    changed = Signal()

    def __init__(self, changed, action_type='sandbox', action='', owner=None):
        super().__init__()

        self.owner = owner
        self.type = QComboBox()
        self.action = None
        self._changed = changed
        self.data = None
        self.this = None
        
        for action in ActionItem.__subclasses__():
            self.type.addItem(action.name)
        
        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.type_changed)

        self.action_box = CHBoxLayout(margins=0)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(QLabel("Action:", minimumWidth=60))
            layout.add(self.type)
            layout.add(self.action_box, 1)

    def type_changed(self):
        if self.action:
            self.action.deleteLater()
            self.action = None
        self.action = ActionItem.get_item(self.type.currentText())(self._changed, self.owner)
        if self.data:
            self.action.set_data(self.data['action'])
        self.action_box.add(self.action)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction(QAction('Copy Action', self, triggered=self.copy))
        menu.addAction(QAction('Paste Action', self, triggered=self.paste))
        menu.addAction(QAction('Reset Action', self, triggered=self.reset))
        menu.exec_(event.globalPos())

    def copy(self):
        data = json.dumps(self.get_data())
        QClipboard().setText(data)

    def paste(self):
        data = json.loads(QClipboard().text())
        self.set_data(data)

    def set_data(self, data):
        if 'action' in data:
            self.data = data
            if 'type' not in data['action']:
                data['action']['type'] = 'sandbox'

            self.type.setCurrentText(data['action']['type'])
            self.type_changed()

    def get_data(self):
        return {
            'action': {
                'type': self.type.currentText(),
                **self.action.get_data(),
            }
        }

    def run(self):
        self.action.run()

    def reset(self):
        self.type.setCurrentText('sandbox')
        self.action.reset()


@draggable
class ActionWidget(QWidget):
    changed = Signal()

    @classmethod
    @property
    def default_data(cls):
        return {
            'name': 'Action',
            'enabled': True,
            'action': {
                'type': 'sandbox',
                'action': ''
            },
            'trigger': {
                'enabled': True,
                'trigger_type': 'keyboard',
                'trigger': ''
            },
            'filter': {
                'enabled': True,
                'filters': []
            }
        }

    def __init__(self, name='', group=None, trigger=False, data=None, changed=None, parent=None):
        super().__init__(parent=parent)

        self.name = name
        action_type = 'sandbox'
        action = ''

        if data:
            self.name = data['name']
            action = data['action']
            if 'type' in data:
                action_type = data['type']

        self.run_btn = QPushButton('', clicked=self.run, icon=qta.icon('fa5.play-circle'))
        self.run_btn.setIconSize(QSize(22, 22))

        self.enabled = AnimatedToggle()
        self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        self.label = LabelEdit(self.name, changed=self.on_change)
        self.action = Action(self.on_change, action_type, action, owner=self)
        self.trigger = ActionTrigger(self.on_change, run=self.run, owner=self)
        self.filter = ActionFilter(self.on_change, owner=self)

        if trigger:
            self.trigger.enabled.setChecked(True)
            self.filter.enabled.setChecked(True)

        self.group = group
        if group:
            group.register(self)

        if changed:
            self.changed.connect(changed)

        self.do_layout()

    def do_layout(self):
        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                layout.add(self.label)
                layout.add(QWidget(), 1)
                layout.add(self.enabled)
                layout.add(self.filter)
            with layout.hbox(margins=0):
                layout.add(self.trigger)
                layout.add(QWidget(), 1)
            with layout.hbox(margins=0):
                layout.add(self.action, 2)
                layout.add(self.run_btn)
            layout.add(HLine())

    def get_data(self):
        return {
            'name': self.label.text(),
            'enabled': self.enabled.isChecked(),
            **self.action.get_data(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
        }

    def set_data(self, data):
        if not data:
            data = self.default_data

        self.enabled.setChecked(data.get('enabled', True))
        self.label.setText(data['name'])
        self.action.set_data(data)
        self.trigger.set_data(data)
        self.filter.set_data(data)
        call_later(self.on_change, 50) #TODO: this is a hack, find a real solution

    def on_change(self):
        self.filter.setVisible(self.filter.enabled.isChecked())
        self.trigger.setVisible(self.trigger.enabled.isChecked())
        self.changed.emit()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction('Run').triggered.connect(self.run)
        menu.addAction('Rename').triggered.connect(self.label.start_editing)
        menu.addAction('Copy').triggered.connect(self.copy)
        menu.addAction('Paste').triggered.connect(self.paste)
        menu.addAction(self.trigger.enabled)
        menu.addAction(self.filter.enabled)
        menu.addAction('Reset').triggered.connect(self.reset)
        menu.addAction('Remove').triggered.connect(self.remove)
        menu.exec_(event.globalPos())

    def get_drag_data(self) -> QMimeData:
        mime = QMimeData()
        data = json.dumps(self.get_data()).encode()
        mime.setData('action_drop', data)
        return mime

    def handle_drop(self, drop):
        if drop == Qt.MoveAction:
            self.remove()

    def copy(self):
        data = {
            **self.action.get_data(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
        }
        QClipboard().setText(json.dumps(data))

    def paste(self):
        data = json.loads(QClipboard().text())
        self.action.set_data(data)
        self.trigger.set_data(data)
        self.filter.set_data(data)

    def reset(self):
        self.label.setText(self.name)
        self.action.reset()
        self.trigger.reset()
        self.filter.reset()
        self.on_change()

    def remove(self):
        if self.group:
            self.group.actions.remove(self)
            self.group.parent().actions.remove(self)
            self.group.action_changed.emit()
        self.deleteLater()

    def run(self):
        if self.group:
            if not self.group.can_run():
                return

        if not self.enabled:
            return

        if not self.filter.check_filters():
            return

        Sandbox().this = self
        Sandbox().source = self.sender()
        self.action.run()
        Sandbox().this = None
        Sandbox().source = None


class CompactActionWidget(ActionWidget):
    @classmethod
    @property
    def default_data(cls):
        return {
            'name': 'Action',
            'enabled': True,
            'action': {
                'type': 'sandbox',
                'action': ''
            },
            'trigger': {
                'enabled': False,
                'trigger_type': 'sandbox',
                'trigger': ''
            },
            'filter': {
                'enabled': False,
                'filters': []
            }
        }

    def do_layout(self):
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.label)
            layout.add(VLine())
            # layout.add(self.trigger, 1)
            # layout.add(self.filter)
            layout.add(self.action, 2)
            layout.add(self.run_btn)
        
    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction('Run').triggered.connect(self.run)
        menu.addAction('Rename').triggered.connect(self.label.start_editing)
        menu.addAction('Copy').triggered.connect(self.copy)
        menu.addAction('Paste').triggered.connect(self.paste)
        menu.addAction('Reset').triggered.connect(self.reset)
        menu.exec_(event.globalPos())