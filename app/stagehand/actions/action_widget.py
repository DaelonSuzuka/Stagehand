from qtstrap import *
from stagehand.sandbox import Sandbox
import qtawesome as qta
from .action_editor import ActionEditorDialog
from .action_trigger import ActionTrigger
from .action_filter import FilterStack, ActionFilter
import abc
import json


class ActionItem:
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

    @abc.abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def reset(self):
        pass


class SandboxAction(QWidget, ActionItem):
    name = 'sandbox'

    def __init__(self, changed, parent=None):
        super().__init__(parent=parent)
        
        self.parent = parent
        self.action = QLineEdit()
        self.action.textChanged.connect(changed)
        self.changed = changed

        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=QIcon(qta.icon('fa5.edit')))

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.action)
            layout.add(self.edit_btn)
    
    def open_editor(self, *_):
        self.data['action'] = self.action.text()
        self.editor = ActionEditorDialog(self.data, self)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        text = self.editor.editor.toPlainText()
        self.action.setText(text)
        self.action.setDisabled('\n' in text)
        self.changed()

    def from_dict(self, data: dict):
        self.data = data
        try:
            self.action.setText(data['action'])
            self.action.setDisabled('\n' in text)
        except:
            pass

    def to_dict(self):
        return {
            'action': self.action.text()
        }

    def reset(self):
        self.action.clear()

    def run(self):
        Sandbox().run(self.action.text(), this=self.parent.this)


class Action(QWidget):
    changed = Signal()

    def __init__(self, changed, action_type='sandbox', action=''):
        super().__init__()

        self.type = QComboBox()
        self.action = SandboxAction(changed, self)
        self._changed = changed
        self.data = None
        self.this = None
        
        for action in ActionItem.__subclasses__():
            self.type.addItem(action.name)
        
        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.type_changed)

        self.action_box = CHBoxLayout(margins=(0,0,0,0))

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.action_box, 1)

    def type_changed(self):
        if self.action:
            self.action.deleteLater()
            self.action = None
        self.action = ActionItem.get_item(self.type.currentText())(self._changed)
        if self.data:
            self.action.from_dict(self.data)
        self.action_box.add(self.action)

    def set_data(self, data):
        self.data = data
        if 'action_type' not in data:
            data['action_type'] = 'sandbox'

        self.type.setCurrentText(data['action_type'])
        self.type_changed()

    def to_dict(self):
        return  {
            'action_type': self.type.currentText(),
            **self.action.to_dict(),
        }

    def run(self):
        self.action.run()

    def reset(self):
        self.type.setCurrentText('sandbox')
        self.action.reset()


class ActionWidget(QWidget):
    changed = Signal()

    @staticmethod
    def from_data(data):
        name = data['name']
        label = data['label']
        action = data['action']
        action_type = data['type']

        return ActionWidget()

    def __init__(self, name='', group=None, trigger=False, data=None, changed=None, parent=None):
        super().__init__(parent=parent)

        self.name = name
        label = name
        action_type = 'sandbox'
        action = ''

        if data:
            self.name = data['name']
            label = data['label']
            action = data['action']
            if 'type' in data:
                action_type = data['type']

        self.run_btn = QPushButton('', clicked=self.run, icon=QIcon(qta.icon('fa5.play-circle')))

        self.label = LabelEdit(label, changed=self.on_change)
        self.action = Action(self.on_change, action_type, action)
        self.trigger = ActionTrigger(self.on_change, run=self.run, parent=self)
        self.filter = ActionFilter(self.on_change, parent=self)

        if trigger:
            self.trigger.enabled.setChecked(True)
            self.filter.enabled.setChecked(True)

        if group:
            group.register(self)

        if changed:
            self.changed.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.label)
            layout.add(VLine())
            layout.add(self.trigger, 1)
            layout.add(self.filter)
            layout.add(self.action, 2)
            layout.add(self.run_btn)

    def to_dict(self):
        return {
            'name': self.name,
            'label': self.label.text(),
            **self.action.to_dict(),
            **self.trigger.to_dict(),
            **self.filter.to_dict(),
        }

    def set_data(self, data):
        self.label.setText(data['label'])
        self.action.set_data(data)
        self.trigger.set_data(data)
        self.filter.set_data(data)
        self.on_change()

    def on_change(self):
        self.filter.setVisible(self.filter.enabled.isChecked())
        self.trigger.setVisible(self.trigger.enabled.isChecked())
        self.changed.emit()

    def contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction(QAction('Run', self, triggered=self.run))
        menu.addAction(QAction('Rename', self, triggered=self.label.start_editing))
        menu.addAction(QAction('Copy', self, triggered=self.copy))
        menu.addAction(QAction('Paste', self, triggered=self.paste))
        menu.addAction(self.trigger.enabled)
        menu.addAction(self.filter.enabled)
        menu.addAction(QAction('Reset', self, triggered=self.reset))
        menu.exec_(event.globalPos())

    def copy(self):
        data = {
            **self.action.to_dict(),
            **self.trigger.to_dict(),
            **self.filter.to_dict(),
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

    def run(self):
        if self.filter.check_filters():
            self.action.run()