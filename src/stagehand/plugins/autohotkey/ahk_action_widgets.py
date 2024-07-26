from qtstrap import *
from qtstrap.extras.code_editor import CodeLine
import qtawesome as qta
from abc import abstractmethod
from stagehand.sandbox import Sandbox
from .ahk_script_editor import AHKScriptEditorDialog


class AHKActionWidget(QWidget):
    @abstractmethod
    def __init__(self, changed=None, owner=None):
        raise NotImplementedError

    @abstractmethod
    def refresh(self):
        raise NotImplementedError

    @abstractmethod
    def set_data(self, data):
        raise NotImplementedError

    @abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abstractmethod
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
        return {}

    def run(self):
        pass


class AHKScriptWidget(QWidget):
    # TODO: class doesn't init properly when there's no data
    def __init__(self, changed=None, owner=None):
        super().__init__()
        self.changed = changed
        self.owner = owner

        self.action = CodeLine(changed=changed)
        self.action.ctrl_enter_pressed.connect(self.run)
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
        return {'action': self.action.text()}

    def run(self):
        Sandbox().run(f'ahk.run_script("{self.action.text()}")')


widgets = {
    'script': AHKScriptWidget,
    # 'beep': Beep,
}
