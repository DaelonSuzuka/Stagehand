from qtstrap import *
from .obs_socket import ObsSocket
from pathlib import Path


class ObsStatusWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.status = QLabel('Not Connected')

        with CHBoxLayout(self) as layout:
            layout.add(QLabel('OBS Status:'))
            layout.add(self.status)

    def setText(self, text):
        self.status.setText(text)


class ObsManager(QWidget):
    message_received = Signal(dict)
    raw_message_received = Signal(str)
    socket_connected = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.socket = ObsSocket()
        self.socket.status_changed.connect(self.set_status)

        self.status = QLabel('Not Connected')
        self.status_widget = ObsStatusWidget()
        self.sidebar_widget = QPushButton(iconSize=QSize(40, 40), icon=QIcon(str(Path(__file__).parent / 'obs.png')), flat=True)

        self.url = PersistentLineEdit('obs_url', default='localhost', fixedWidth=75)
        self.port = PersistentLineEdit('obs_port', default='4444', fixedWidth=50)
        self.connect_btn = QPushButton('Connect', clicked=self.on_connect_btn)
        self.connect_at_start = PersistentCheckBox('connect_at_start')

        self.password = PersistentLineEdit('obs_password')
        def set_show_password(state):
            if state == Qt.Checked:
                self.password.setEchoMode(QLineEdit.Normal)
            else:
                self.password.setEchoMode(QLineEdit.Password)
        self.show_password = PersistentCheckBox('show_password', changed=set_show_password)
        set_show_password(self.show_password.checkState())

        if self.connect_at_start.checkState() == Qt.Checked:
            self.open()

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Connect on Startup:'))
                layout.add(self.connect_at_start)
            layout.add(HLine())
            with layout.hbox(align='left'):
                layout.add(QLabel('Status:'))
                layout.add(self.status)
            with layout.hbox(align='left'):
                layout.add(QLabel('Address:'))
                layout.add(self.url)
                layout.add(QLabel('Port:'))
                layout.add(self.port)
                layout.add(self.connect_btn)
                layout.add(QLabel(), 1)
            with layout.hbox(align='left'):
                layout.add(QLabel('Password:'))
                layout.add(self.password)
                layout.add(QLabel('Show:'))
                layout.add(self.show_password)
                layout.add(QLabel(), 1)

    def on_connect_btn(self):
        if self.connect_btn.text() == 'Connect':
            self.open()
        else:
            self.socket.close()

    def lock(self):
        self.url.setEnabled(False)
        self.port.setEnabled(False)
        self.password.setEnabled(False)
        self.show_password.setEnabled(False)
        self.show_password.setChecked(False)
        self.password.setEchoMode(QLineEdit.Password)

    def unlock(self):
        self.url.setEnabled(True)
        self.port.setEnabled(True)
        self.password.setEnabled(True)
        self.show_password.setEnabled(True)

    def set_status(self, status):
        if status == 'active':
            self.status.setText('Connected')
            self.status_widget.setText('Connected')
            self.connect_btn.setText('Disconnect')

        elif status == 'inactive':
            self.status.setText('Not Connected')
            self.status_widget.setText('Not Connected')
            self.connect_btn.setText('Connect')

        elif status == 'failed':
            self.status.setText('Authentication Failed')
            self.status_widget.setText('Not Connected')
            self.connect_btn.setText('Connect')

    def open(self):
        self.socket.open(self.url.text(), self.port.text(), self.password.text())

    def send(self, payload, callback=None):
        self.socket.send(payload, callback)