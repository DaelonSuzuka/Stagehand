from qtstrap import *
from qtstrap.extras.command_palette import Command
from qtstrap.extras.settings_model import SettingsModel
from stagehand.components import StagehandStatusBarItem
from stagehand.main_window import MainWindow
from .obs_socket import ObsSocket


class ObsSettings(SettingsModel):
    url: str = 'localhost'
    port: str = '4444'
    password: str = 'websocketpassword'
    connect_at_start: bool = False

    class Config:
        prefix = 'plugins/obs'


@singleton
class ObsStatusWidget(StagehandStatusBarItem):
    status_changed = Signal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.socket = ObsSocket()
        self.socket.status_changed.connect(self.set_status)

        self.status = ''
        self.status_label = QLabel('Not Connected')

        self.settings = ObsSettings()

        self.connect_at_start = PersistentCheckableAction('obs/connect_at_start', 'Connect on Startup')
        if self.connect_at_start.isChecked():
            self.open()

        self.commands = [
            Command('OBS: Connect websocket', triggered=self.open),
            Command('OBS: Disconnect websocket', triggered=self.close),
            Command('OBS: Open Settings', triggered=self.open_settings),
        ]

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(QLabel('OBS:'))
            layout.add(self.status_label)
            layout.add(QLabel())

    def setText(self, text):
        self.status_label.setText(text)

    def set_url(self, url):
        self.settings.url = url

    def set_port(self, port):
        self.settings.port = port

    def set_password(self, password):
        self.settings.password = password

    def set_status(self, status):
        self.status = status
        status_messages = {
            'active': 'Connected',
            'pending': 'Connecting',
            'reconnecting': f'Reconnecting {self.socket.reconnect_attempts}',
            'inactive': 'Not Connected',
            'failed': 'Authentication Failed',
        }
        message = status_messages[status]

        self.status_label.setText(message)
        self.status_changed.emit(self.status, message)

    def contextMenuEvent(self, event):
        menu = QMenu()
        if self.status != 'active':
            menu.addAction('Connect').triggered.connect(self.open)
        else:
            menu.addAction('Disconnect').triggered.connect(self.close)
        menu.addAction(self.connect_at_start)
        menu.addAction('Open Settings').triggered.connect(self.open_settings)
        menu.exec_(event.globalPos())

    def open_settings(self):
        MainWindow().tabs.create_page('OBS Settings')

    def open(self):
        self.set_status('pending')
        self.socket.open(self.settings.url, self.settings.port, self.settings.password)

    def close(self):
        self.socket.we_closed = True
        self.socket.close()

    def send(self, payload, callback=None):
        self.socket.send(payload, callback)

    def on_app_close(self):
        self.close()
