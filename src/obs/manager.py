from qtstrap import *
from qtpy.QtWebSockets import *
import json
from obs import requests
import base64
import hashlib


class ObsStatusWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.status = QLabel('Not Connected')

        with CHBoxLayout(self) as layout:
            layout.add(QLabel('Socket:'))
            layout.add(self.status)

    def setText(self, text):
        self.status.setText(text)


class ObsManager(QWidget):
    message_received = Signal(dict)
    raw_message_received = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.id = 0
        self.active = False

        self.socket = QWebSocket()
        self.socket.connected.connect(self.connected)
        self.socket.disconnected.connect(self.disconnected)
        self.socket.textMessageReceived.connect(self.recieve)

        self.history = {}
        self.callbacks = {}

        self.status = QLabel('Not Connected')
        self.status_widget = ObsStatusWidget()

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

    def unlock(self):
        self.url.setEnabled(True)
        self.port.setEnabled(True)
        self.password.setEnabled(True)

    def set_status(self, status):
        if status == 'active':
            self.active = True
            self.status.setText('Connected')
            self.status_widget.setText('Connected')
            self.connect_btn.setText('Disconnect')

        elif status == 'inactive':
            self.active = False
            self.status.setText('Not Connected')
            self.status_widget.setText('Not Connected')
            self.connect_btn.setText('Connect')

        elif status == 'failed':
            self.active = False
            self.status.setText('Authentication Failed')
            self.status_widget.setText('Not Connected')
            self.connect_btn.setText('Connect')

    def connected(self):
        self.lock()

        def auth_cb(msg):
            if msg['authRequired']:
                # apparently this is how you process the challege/response
                # this is shamelessly lifted from obs-websocket-py:
                # https://github.com/Elektordi/obs-websocket-py/blob/master/obswebsocket/core.py#L120
                secret = base64.b64encode(
                    hashlib.sha256(
                        (self.password.text() + msg['salt']).encode('utf-8')
                    ).digest()
                )
                auth = base64.b64encode(
                    hashlib.sha256(
                        secret + msg['challenge'].encode('utf-8')
                    ).digest()
                ).decode('utf-8')

                auth_payload = {
                    "request-type": "Authenticate",
                    "auth": auth,
                }

                def auth_cb2(msg):
                    if msg['status'] == 'error':
                        if msg['error'] == 'Authentication Failed.':
                            self.unlock()
                            self.set_status('failed')

                    elif msg['status'] == 'ok':
                        self.set_status('active')

                self.send(auth_payload, auth_cb2)
            else:
                self.set_status('active')

        self.send(requests.GetAuthRequired(), auth_cb)

    def disconnected(self):
        self.unlock()
        self.set_status('inactive')

    def open(self):
        address = f'ws://{self.url.text()}:{self.port.text()}'
        self.socket.open(QUrl(address))

    def send(self, payload, callback=None):
        payload['message-id'] = str(self.id)
        self.history[self.id] = payload

        if callback:
            self.callbacks[str(self.id)] = callback

        message = json.dumps(payload)
        self.socket.sendTextMessage(message)
        self.id += 1

    def recieve(self, message):
        self.raw_message_received.emit(message)
        msg = json.loads(message)
        self.message_received.emit(msg)

        # process callbacks
        if 'message-id' in msg:
            if msg['message-id'] in self.callbacks:
                self.callbacks[msg['message-id']](msg)