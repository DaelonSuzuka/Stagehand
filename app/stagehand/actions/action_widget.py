from qtstrap import *
from stagehand.sandbox import Sandbox
import qtawesome as qta
from .action_editor import ActionEditorDialog


class ActionStack(QWidget):
    changed = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.type = QComboBox()
        self.type.addItems([
            'sandbox',
            'obs',
            'key',
        ])

        self.sandbox_action = QLineEdit()
        
        self.obs_action = QWidget()
        self.obs_action_type = QComboBox()
        self.obs_action_type.addItems(['set scene', 'set mute'])
        self.obs_action_value = QComboBox()
        with CHBoxLayout(self.obs_action, margins=(0,0,0,0)) as layout:
            layout.add(self.obs_action_type)
            layout.add(self.obs_action_value)

        self.key_action = QWidget()
        self.key_action_type = QComboBox()
        self.key_action_type.addItems(['press', 'release', 'both'])
        self.key_action_value = QLineEdit()
        with CHBoxLayout(self.key_action, margins=(0,0,0,0)) as layout:
            layout.add(self.key_action_type)
            layout.add(self.key_action_value)
        
        self.stack = QStackedWidget()
        self.stack.addWidget(self.sandbox_action)
        self.stack.addWidget(self.obs_action)
        self.stack.addWidget(self.key_action)

        self.type.currentIndexChanged.connect(self.stack.setCurrentIndex)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.stack)


class ActionWidget(QWidget):
    changed = Signal(str)

    @staticmethod
    def from_data(data):
        name = data['name']
        label = data['label']
        action = data['action']
        action_type = data['type']

        action = ActionWidget()


    def __init__(self, name='', group=None, data=None, changed=None, parent=None):
        super().__init__(parent=parent)

        self.name = name
        label = name
        action = ''

        if data:
            self.name = data['name']
            label = data['label']
            action = data['action']
            # action_type = data['type']

        self.label = LabelEdit(label, changed=self.on_change)

        self.action = QLineEdit(text=action)
        self.action.textChanged.connect(self.on_change)
        
        self.stack = ActionStack()

        if group:
            group.register(self)

        self.run_btn = QPushButton('', clicked=self.run, icon=QIcon(qta.icon('fa5.play-circle')))
        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=QIcon(qta.icon('fa5.edit')))

        self.on_change()

        if changed:
            self.changed.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.label)
            layout.add(self.stack, 1)
            layout.add(self.edit_btn)
            layout.add(self.run_btn)
    
    @staticmethod
    def default_data(name):
        return {
            'name': name,
            'label': name,
            'action': '',
        }

    def to_dict(self):
        return {
            'name': self.name,
            'label': self.label.text(),
            'action': self.action.text(),
        }

    def set_data(self, data):
        self.label.setText(data['label'])
        self.action.setText(data['action'])

    def on_change(self):
        self.action.setEnabled('\n' not in self.action.text())

        msg = f'{self.name}: {self.label.text()}, <{self.action.text()}>'
        self.changed.emit(msg)

    def open_editor(self, _=None):
        self.editor = ActionEditorDialog(self.to_dict(), self)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        self.label.setText(self.editor.label.text())

        text = self.editor.editor.toPlainText()
        self.action.setText(text)

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
        Sandbox().run(self.action.text())