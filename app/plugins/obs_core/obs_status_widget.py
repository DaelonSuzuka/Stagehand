from qtstrap import *
from .obs_socket import ObsSocket
from stagehand.components import StagehandStatusBarItem, SidebarButton
from pathlib import Path


class ObsStatusWidget(StagehandStatusBarItem):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.socket = ObsSocket()
        self.socket.status_changed.connect(self.set_status)

        self.status = ''
        self.status_label = QLabel('Not Connected')

        self.url = 'localhost'
        self.port = '4444'
        self.password = 'websocketpassword'

        self.connect_at_start = PersistentCheckableAction('obs/connect_at_start', 'Connect on Startup')

        if self.connect_at_start.isChecked():
            self.open()

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(QLabel('OBS:'))
            layout.add(self.status_label)
            layout.add(QLabel())

    def setText(self, text):
        self.status_label.setText(text)
    
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
        self.socket.open(self.url, self.port, self.password)

    def close(self):
        self.socket.we_closed = True
        self.socket.close()

    def send(self, payload, callback=None):
        self.socket.send(payload, callback)