from qtstrap import *
from qtstrap.extras.code_editor import CodeLine, PythonHighlighter
from stagehand.sandbox import Sandbox, SandboxCompletionModel
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
    def set_data(self, data: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    def reset(self):
        pass


class SandboxAction(QWidget, ActionItem):
    name = 'sandbox'

    def __init__(self, changed, owner=None):
        super().__init__()
        
        self.owner = owner
        self.action = CodeLine(changed=changed, highlighter=PythonHighlighter, model=SandboxCompletionModel())
        self.changed = changed

        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=qta.icon('fa5.edit'))

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.action)
            layout.add(self.edit_btn)
    
    def open_editor(self, *_):
        self.data['action'] = self.action.text()
        self.data['name'] = self.owner.name
        self.editor = ActionEditorDialog(self.data, self.owner)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        text = self.editor.editor.toPlainText()
        self.action.setText(text)
        self.action.setDisabled('\n' in text)
        self.owner.label.setText(self.editor.label.text())
        self.changed()

    def set_data(self, data: dict):
        self.data = data
        if 'action' in data:
            self.action.setText(data['action'])
        self.action.setDisabled('\n' in self.action.text())

    def get_data(self):
        return {
            'action': self.action.text()
        }

    def reset(self):
        self.action.clear()
        self.action.setDisabled(False)

    def run(self):
        # Sandbox().run(self.action.text(), this=self.parent.this)
        Sandbox().run(self.action.text())


class Action(QWidget):
    changed = Signal()

    def __init__(self, changed, action_type='sandbox', action='', owner=None):
        super().__init__()

        self.owner = owner
        self.type = QComboBox()
        self.action = SandboxAction(changed, owner)
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
            self.action.set_data(self.data)
        self.action_box.add(self.action)

    def set_data(self, data):
        self.data = data
        if 'action_type' not in data:
            data['action_type'] = 'sandbox'

        self.type.setCurrentText(data['action_type'])
        self.type_changed()

    def get_data(self):
        return  {
            'action_type': self.type.currentText(),
            **self.action.get_data(),
        }

    def run(self):
        self.action.run()

    def reset(self):
        self.type.setCurrentText('sandbox')
        self.action.reset()


class ActionWidget(QWidget):
    changed = Signal()

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

        self.run_btn = QPushButton('', clicked=self.run, icon=qta.icon('fa5.play-circle'))

        self.label = LabelEdit(label, changed=self.on_change)
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
            'name': self.name,
            'label': self.label.text(),
            **self.action.get_data(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
        }

    def set_data(self, data):
        self.label.setText(data['label'])
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
        menu.exec_(event.globalPos())

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

    def run(self):
        if self.group:
            if not self.group.filter.check_filters():
                return

        if not self.filter.check_filters():
            return

        self.action.run()


class CompactActionWidget(ActionWidget):
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