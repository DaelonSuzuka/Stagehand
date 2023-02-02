from qtstrap import *
from qtstrap.extras.command_palette import Command
from .teamspeak_socket import TeamSpeakSocket
from stagehand.components import StagehandStatusBarItem


class TeamSpeakStatusWidget(StagehandStatusBarItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.socket = TeamSpeakSocket()
        self.socket.status_changed.connect(self.set_status)

        self.url = 'localhost'
        self.port = '5898'
        self.api_key = QSettings().value('teamspeak/api_key', '')
        self.status = ''
        self.status_label = QLabel('Not Connected')
        self.connect_at_start = PersistentCheckableAction('teamspeak/connect_at_start', 'Connect on Startup')

        if self.connect_at_start.isChecked():
            self.open()

        self.commands = [
            Command("TeamSpeak: Connect websocket", triggered=self.open),
            Command("TeamSpeak: Disconnect websocket", triggered=self.close),
        ]

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(QLabel('TeamSpeak:'))
            layout.add(self.status_label)
            layout.add(QLabel())

    def set_status(self, status):
        self.status = status
        status_messages = {
            'active': 'Connected',
            'pending': 'Connecting',
            'reconnecting': f'Reconnecting {self.socket.reconnect_attempts}',
            'inactive': 'Not Connected',
            'failed': 'Authentication Failed',
        }
        self.status_label.setText(status_messages[status])

    def contextMenuEvent(self, event):
        menu = QMenu()
        if self.status != 'active':
            menu.addAction('Connect').triggered.connect(self.open)
        else:
            menu.addAction('Disconnect').triggered.connect(self.close)
        menu.addAction(self.connect_at_start)
        menu.exec_(event.globalPos())
        
    def open(self):
        self.set_status('pending')
        self.socket.open(self.url, self.port, self.api_key)

    def close(self):
        self.socket.we_closed = True
        self.socket.close()

    def send(self, payload, callback=None):
        self.socket.send(payload, callback)

    def on_app_close(self):
        self.close()