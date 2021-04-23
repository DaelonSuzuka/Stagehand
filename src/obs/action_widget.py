from qtstrap import *
from obs import Sandbox
from editor import CodeEditor
import qtawesome as qta


class ActionEditorDialog(QDialog):
    reload = Signal(str, Slot)

    def __init__(self, data, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle('Action Editor')

        self.name = data['name']
        self.label = QLineEdit(data['label'])
        self.editor = CodeEditor()
        self.editor.setText(data['action'])
        self.editor.textChanged.connect(lambda: self.reload.emit(self.editor.toPlainText(), self.set_error))
        self.reload.connect(Sandbox().compile)
        self.error = QLabel('')

        self.reset = QPushButton('Reset', clicked=self.on_reset)
        self.cancel = QPushButton('Cancel', clicked=self.reject)
        self.ok = QPushButton('Ok', clicked=self.accept)
        self.run = QPushButton('', clicked=lambda: Sandbox().run(self.editor.toPlainText(), self.set_error))
        self.run.setIcon(QIcon(qta.icon('mdi.play-circle-outline')))

        with CVBoxLayout(self) as layout:
            with layout.hbox() as layout:
                layout.add(QLabel('Name:'))
                layout.add(QLabel(data['name']))
                layout.add(QLabel(), 1)
                layout.add(self.reset)
            with layout.hbox(align='left') as layout:
                layout.add(QLabel('Label:'))
                layout.add(self.label)
                layout.add(QLabel(), 1)
                layout.add(self.run)
            layout.add(self.editor)
            layout.add(self.error)
            with layout.hbox(align='right') as layout:
                layout.add(self.cancel)
                layout.add(self.ok)

        self.editor.setFocus()

    @Slot()
    def set_error(self, error):
        self.error.setText(error)

    def on_reset(self):
        self.editor.setText('')
        self.label.setText(self.name)


class ActionWidgetGroup(QObject):
    action_changed = Signal()

    def __init__(self, name, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.actions = []
        self.load()

    def register(self, action):
        self.actions.append(action)
        if action.name in self.prev_data:
            action.set_data(self.prev_data[action.name])
        action.changed.connect(self.on_action_change)

    def on_action_change(self):
        self.save()
        self.action_changed.emit()

    def load(self):
        self.prev_data = QSettings().value(self.name, {})

    def save(self):
        QSettings().setValue(self.name, self.get_data())

    def get_data(self):
        data = {}
        for action in self.actions:
            data[action.name] = action.to_dict()
        return data


class ActionWidget(QWidget):
    changed = Signal(str)

    def __init__(self, name='', group=None, data=None, changed=None, parent=None):
        super().__init__(parent=parent)

        self.name = name
        label = name
        action = ''

        if data:
            self.name = data['name']
            label = data['label']
            action = data['action']

        self.label = LabelEdit(label, changed=self.on_change)
        
        self.action = QLineEdit(text=action)
        self.action.textChanged.connect(self.on_change)

        if group:
            group.register(self)

        self.run_btn = QPushButton('', clicked=self.run)
        self.run_btn.setIcon(QIcon(qta.icon('fa5.play-circle')))
        
        self.edit_btn = QPushButton('', clicked=self.open_editor)
        self.edit_btn.setIcon(QIcon(qta.icon('fa5.edit')))

        self.on_change()

        if changed:
            self.changed.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.label)
            layout.add(self.action, 1)
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