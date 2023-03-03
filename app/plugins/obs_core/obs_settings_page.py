from qtstrap import *
from stagehand.components import StagehandPage
from .obs_status_widget import ObsStatusWidget


class ObsSettingsPage(StagehandPage):
    page_type = 'OBS Settings'
    tags = ['singleton']

    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name

        if data is not None:
            self.set_data(data)

        obs = ObsStatusWidget()

        self.status = QLabel(obs.status_label.text())
        self.url = QLineEdit(obs.url)
        self.port = QLineEdit(obs.port)
        self.password = QLineEdit(obs.password)
        self.password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.connect_at_start = QCheckBox()
        self.connect_at_start.setChecked(obs.connect_at_start.isChecked())

        # TODO: why doesn't this work?
        obs.status_changed.connect(self.status_changed)
        obs.connect_at_start.changed.connect(lambda: self.connect_at_start.setChecked(obs.connect_at_start.isChecked()))
        self.connect_at_start.stateChanged.connect(
            lambda x: obs.connect_at_start.setChecked(self.connect_at_start.isChecked())
        )

        self.url.textChanged.connect(obs.set_url)
        self.port.textChanged.connect(obs.set_port)
        self.password.textChanged.connect(obs.set_password)

        with CVBoxLayout(self) as layout:
            with layout.form():
                layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
                layout.addRow('Status:', self.status)
                layout.addRow('Url:', self.url)
                layout.addRow('Port:', self.port)
                layout.addRow('Password:', self.password)
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
            self.password.setEnabled(False)
        elif status == 'inactive':
            self.url.setEnabled(True)
            self.port.setEnabled(True)
            self.password.setEnabled(True)

    def get_name(self) -> str:
        return self.name

    def set_data(self, data: dict) -> None:
        self.name = data.get('name', self.name)

    def get_data(self) -> dict:
        data = {
            'page_type': self.page_type,
            'name': self.name,
        }
        return data
