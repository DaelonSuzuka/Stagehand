from qtstrap import *
from stagehand.components import StagehandPage
from .godot_status_widget import GodotStatusWidget


class GodotSettingsPage(StagehandPage):
    page_type = 'Godot Settings'
    tags = ['singleton']

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name

        if data is not None:
            self.set_data(data)

        godot = GodotStatusWidget()

        self.status = QLabel(godot.status_label.text())
        self.url = QLineEdit(godot.url)
        self.port = QLineEdit(godot.port)
        # self.password = QLineEdit(godot.password)
        # self.password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.connect_at_start = QCheckBox()
        self.connect_at_start.setChecked(godot.connect_at_start.isChecked())

        # TODO: why doesn't this work?
        godot.status_changed.connect(self.status_changed)
        godot.connect_at_start.changed.connect(lambda: self.connect_at_start.setChecked(godot.connect_at_start.isChecked()))
        self.connect_at_start.stateChanged.connect(
            lambda x: godot.connect_at_start.setChecked(self.connect_at_start.isChecked())
        )

        self.url.textChanged.connect(godot.set_url)
        self.port.textChanged.connect(godot.set_port)
        # self.password.textChanged.connect(godot.set_password)

        with CVBoxLayout(self) as layout:
            with layout.form():
                layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
                layout.addRow('Status:', self.status)
                layout.addRow('Url:', self.url)
                layout.addRow('Port:', self.port)
                # layout.addRow('Password:', self.password)
                layout.addRow('Connect At Start:', self.connect_at_start)

    def tab_context_menu(self, pos: QPoint, tabs, tab_idx: int):
        menu = QMenu()
        menu.addAction('Close').triggered.connect(lambda: tabs.remove_page(tab_idx))
        menu.exec_(pos)

    def status_changed(self, status, message=''):
        if message:
            self.status.setText(message)

        # lock the UI if the connection is active
        if status == 'active':
            self.url.setEnabled(False)
            self.port.setEnabled(False)
            # self.password.setEnabled(False)
        elif status == 'inactive':
            self.url.setEnabled(True)
            self.port.setEnabled(True)
            # self.password.setEnabled(True)

    def get_name(self) -> str:
        return self.name
