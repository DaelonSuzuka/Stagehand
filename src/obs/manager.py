from qt import *
import json
from obs import requests


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

        self.socket = QWebSocket()
        self.socket.connected.connect(self.connected)
        self.socket.disconnected.connect(self.disconnected)
        self.socket.textMessageReceived.connect(self.recieve)

        self.history = {}
        self.callbacks = {}

        self.status = QLabel('Not Connected')
        self.status_widget = ObsStatusWidget()

        self.url = PersistentLineEdit('obs_url', default='localhost')
        self.port = PersistentLineEdit('obs_port', default='4444')
        self.connect_btn = QPushButton('Connect', clicked=self.on_connect_btn)
        self.connect_at_start = PersistentCheckBox('connect_at_start')
        self.password = PersistentLineEdit('obs_password')

        if self.connect_at_start.checkState() == Qt.Checked:
            self.open()

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Status:'))
                layout.add(self.status)
            with layout.hbox(align='left'):
                layout.add(QLabel('Connect on Startup:'))
                layout.add(self.connect_at_start)
            with layout.hbox(align='left'):
                layout.add(QLabel('Password:'))
                layout.add(self.password)
                layout.add(QLabel(), 1)
            with layout.hbox(align='left'):
                layout.add(QLabel('Address:'))
                layout.add(self.url)
                layout.add(QLabel('Port:'))
                layout.add(self.port)
                layout.add(self.connect_btn)
                layout.add(QLabel(), 1)

    def on_connect_btn(self):
        if self.connect_btn.text() == 'Connect':
            self.open()
        else:
            self.socket.close()

    def connected(self):
        self.status.setText('Connected')
        self.status_widget.setText('Connected')
        self.connect_btn.setText('Disconnect')
        self.url.setEnabled(False)
        self.port.setEnabled(False)

        def auth_cb(msg):
            if msg['authRequired']:
                # do auth stuff
                pass
            else:
                self.active = True

        self.send(requests.GetAuthRequired(), auth_cb)

    def disconnected(self):
        self.status.setText('Not Connected')
        self.status_widget.setText('Not Connected')
        self.connect_btn.setText('Connect')
        self.url.setEnabled(True)
        self.port.setEnabled(True)

    def open(self):
        address = f'ws://{self.url.text()}:{self.port.text()}'
        # self.address.setText(address)
        self.socket.open(QUrl(address))

    def send(self, payload, callback=None):
        payload['message-id'] = str(self.id)
        self.history[self.id] = payload

        if callback:
            self.callbacks[str(self.id)] = callback

        message = json.dumps(payload)
        # self.tx_history_box.append(message)
        self.socket.sendTextMessage(message)
        self.id += 1

    def get_previous_request_type(self, msg):
        return self.history[int(msg['message-id'])]['request-type']

    def recieve(self, message):
        self.raw_message_received.emit(message)
        # self.rx_history_box.append(message)
        msg = json.loads(message)
        self.message_received.emit(msg)
        # if 'error' in msg:
        #     print('error:', self.get_previous_request_type(msg))

        # process responses
        if 'message-id' in msg:
            if msg['message-id'] in self.callbacks:
                self.callbacks[msg['message-id']](msg)