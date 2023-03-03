from qtstrap import *
from qtstrap.extras.command_palette import Command
from .obs_socket import ObsSocket
from stagehand.components import StagehandStatusBarItem
from stagehand.main_window import MainWindow


@singleton
class ObsStatusWidget(StagehandStatusBarItem):
    status_changed = Signal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.socket = ObsSocket()
        self.socket.status_changed.connect(self.set_status)

        self.status = ''
        self.status_label = QLabel('Not Connected')

        self.url = QSettings().value('obs/url', 'localhost')
        self.port = QSettings().value('obs/port', '4444')
        self.password = QSettings().value('obs/password', 'websocketpassword')

        self.connect_at_start = PersistentCheckableAction('obs/connect_at_start', 'Connect on Startup')

        if self.connect_at_start.isChecked():
            self.open()

        self.commands = [
            Command("OBS: Connect websocket", triggered=self.open),
            Command("OBS: Disconnect websocket", triggered=self.close),
            Command("OBS: Open Settings", triggered=self.open_settings),
        ]

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(QLabel('OBS:'))
            layout.add(self.status_label)
            layout.add(QLabel())

    def setText(self, text):
        self.status_label.setText(text)

    def set_url(self, url):
        QSettings().setValue('obs/url', url)
        self.url = url

    def set_port(self, port):
        QSettings().setValue('obs/port', port)
        self.port = port

    def set_password(self, password):
        QSettings().setValue('obs/password', password)
        self.password = password

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
        self.socket.open(self.url, self.port, self.password)

    def close(self):
        self.socket.we_closed = True
        self.socket.close()

    def send(self, payload, callback=None):
        self.socket.send(payload, callback)

    def on_app_close(self):
        self.close()