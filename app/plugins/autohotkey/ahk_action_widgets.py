from qtstrap import *
from qtstrap.extras.code_editor import CodeLine, CodeEditor
import qtawesome as qta
import abc
from stagehand.sandbox import Sandbox


class AHKActionWidget(QWidget):
    @abc.abstractmethod
    def __init__(self, changed=None, owner=None):
        raise NotImplementedError

    @abc.abstractmethod
    def refresh(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_data(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError
    


class Beep(QWidget):
    def __init__(self, changed=None, owner=None):
        super().__init__()
        self.changed = changed
        self.owner = owner

    def refresh(self):
        return

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return {
        }

    def run(self):
        pass


class AHKScriptEditorDialog(QDialog):
    reload = Signal(str, Slot)

    def __init__(self, data, owner=None):
        super().__init__()

        self.owner = owner
        self.setWindowTitle('AutoHotKey Script Editor')

        self.name = owner.name
        self.label = QLineEdit(owner.label.text())
        self.editor = CodeEditor()
        self.editor.setText(data['action'])
        self.editor.textChanged.connect(lambda: self.reload.emit(self.editor.toPlainText(), self.set_error))
        # self.reload.connect(Sandbox().compile)
        self.error = QLabel('')

        self.reset = QPushButton('Reset', clicked=self.on_reset)
        self.cancel = QPushButton('Cancel', clicked=self.reject)
        self.ok = QPushButton('Ok', clicked=self.accept)
        self.run = QPushButton('', clicked=lambda: Sandbox().run(f'ahk.run_script("{self.editor.toPlainText()}")', error_cb=self.set_error))
        self.run.setIcon(qta.icon('mdi.play-circle-outline'))

        with CVBoxLayout(self) as layout:
            with layout.hbox() as layout:
                layout.add(QLabel('Name:'))
                layout.add(QLabel(owner.name))
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


class AHKScriptWidget(QWidget):
    def __init__(self, changed=None, owner=None):
        super().__init__()
        self.changed = changed
        self.owner = owner
        
        self.action = CodeLine(changed=changed)
        self.edit_btn = QPushButton('', clicked=self.open_editor, icon=qta.icon('fa5.edit'))
        self.edit_btn.setIconSize(QSize(22, 22))

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.action)
            layout.add(self.edit_btn)

    def open_editor(self, *_):
        self.data['action'] = self.action.text()
        self.data['name'] = self.owner.name
        self.editor = AHKScriptEditorDialog(self.data, self.owner)
        self.editor.accepted.connect(self.on_accept)
        self.editor.open()

    def on_accept(self):
        text = self.editor.editor.toPlainText()
        self.action.setText(text)
        self.action.setDisabled('\n' in text)
        self.owner.label.setText(self.editor.label.text())
        self.changed()

    def refresh(self):
        return

    def set_data(self, data):
        self.data = data
        if 'action' in data:
            self.action.setText(data['action'])
        self.action.setDisabled('\n' in self.action.text())

    def get_data(self):
        return {
            'action': self.action.text()
        }

    def run(self):
        Sandbox().run(f'ahk.run_script("{self.action.text()}")')


widgets = {
    'script': AHKScriptWidget,
    # 'beep': Beep,
}