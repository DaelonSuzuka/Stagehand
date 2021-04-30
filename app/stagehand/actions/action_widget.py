from qtstrap import *
from stagehand.sandbox import Sandbox
from stagehand.obs import requests
import qtawesome as qta
from .action_editor import ActionEditorDialog
import abc


class ActionStackItem:
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


class SandboxActionWidget(QWidget, ActionStackItem):
    def __init__(self, changed):
        super().__init__()
        
        self.action = QLineEdit()
        self.action.textChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.action)

    def from_dict(self, data: dict):
        try:
            self.action.setText(data['action'])
        except:
            pass

    def to_dict(self):
        return {
            'action': self.action.text()
        }

    def run(self):
        Sandbox().run(self.action.text())


class ActionStack(QWidget):
    changed = Signal()

    actions = {
        'sandbox': SandboxActionWidget,
    }

    def __init__(self, changed, action_type='sandbox', action=''):
        super().__init__()

        self.type = QComboBox()
        self.stack = QStackedWidget()
        
        for name, action in self.actions.items():
            self.type.addItem(name)
            self.stack.addWidget(action(changed))
        
        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.stack.setCurrentIndex)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.stack)

    def set_data(self, data):
        if 'action_type' not in data:
            data['action_type'] = 'sandbox'

        self.type.setCurrentText(data['action_type'])
        self.stack.currentWidget().from_dict(data)

    def to_dict(self):
        return {
            'action_type': self.type.currentText(),
            **self.stack.currentWidget().to_dict(),
        }

    def run(self):
        self.stack.currentWidget().run()



class ActionWidget(QWidget):
    changed = Signal()

    @staticmethod
    def from_data(data):
        name = data['name']
        label = data['label']
        action = data['action']
        action_type = data['type']

        return ActionWidget()

    def __init__(self, name='', group=None, data=None, changed=None, parent=None):
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

        self.label = LabelEdit(label, changed=self.on_change)
        self.action = ActionStack(self.on_change, action_type, action)

        if group:
            group.register(self)

        self.run_btn = QPushButton('', clicked=self.run, icon=QIcon(qta.icon('fa5.play-circle')))
        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=QIcon(qta.icon('fa5.edit')))

        self.on_change()

        if changed:
            self.changed.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.label)
            layout.add(self.action, 1)
            layout.add(self.edit_btn)
            layout.add(self.run_btn)

    def to_dict(self):
        return {
            'name': self.name,
            'label': self.label.text(),
            **self.action.to_dict()
        }

    def set_data(self, data):
        self.label.setText(data['label'])
        self.action.set_data(data)

    def on_change(self):
        # self.action.setEnabled('\n' not in self.action.text())
        self.changed.emit()

    def open_editor(self, _=None):
        self.editor = ActionEditorDialog(self.to_dict(), self)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        self.label.setText(self.editor.label.text())

        text = self.editor.editor.toPlainText()
        # self.action.setText(text)

        self.on_change()

    def contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction(QAction('Run', self, triggered=self.run))
        menu.addAction(QAction('Rename', self, triggered=self.label.start_editing))
        menu.addAction(QAction('Edit', self, triggered=self.open_editor))
        menu.addAction(QAction('Reset', self, triggered=self.reset))
        menu.exec_(event.globalPos())

    def reset(self):
        self.label.setText(self.name)
        self.action.clear()
        QSettings().setValue(f'{self.name}_label', self.name)
        self.on_change()

    def run(self):
        self.action.run()
        # Sandbox().run(self.action.text())