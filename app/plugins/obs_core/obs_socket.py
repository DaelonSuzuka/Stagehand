from qtstrap import *
from qtpy.QtWebSockets import *
from qtpy.shiboken import isValid
import json
import base64
import hashlib
import queue
import logging


@singleton
class ObsSocket(QObject):
    status_changed = Signal(str)
    message_received = Signal(dict)
    raw_message_received = Signal(str)
    socket_connected = Signal()
    event_received = Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.log = logging.getLogger(__name__)

        self.id = 0
        self.active = False
        self.we_closed = False
        self.reconnect_attempts = 0
        self.max_attempts = 5

        self.url = ''

        self.socket = QWebSocket()
        self.socket.connected.connect(self.connected)
        self.socket.disconnected.connect(self.disconnected)
        self.socket.textMessageReceived.connect(self.recieve)

        self.queue = queue.Queue()
        self.history = {}
        self.callbacks = {}

    def set_status(self, status):
        self.status_changed.emit(status)
        if status == 'active':
            self.reconnect_attempts = 0
            self.active = True
            self.socket_connected.emit()
            self.process_queue()

        elif status == 'inactive':
            self.reconnect_attempts = 0
            self.active = False

        elif status == 'failed':
            self.active = False

        elif status == 'reconnecting':
            self.active = False

    def connected(self):
        def auth_cb(msg):
            if msg['authRequired']:
                # apparently this is how you process the challege/response
                # this is shamelessly lifted from obs-websocket-py:
                # https://github.com/Elektordi/obs-websocket-py/blob/master/obswebsocket/core.py#L120
                secret = base64.b64encode(hashlib.sha256((self.password + msg['salt']).encode('utf-8')).digest())
                auth = base64.b64encode(hashlib.sha256(secret + msg['challenge'].encode('utf-8')).digest()).decode(
                    'utf-8'
                )

                auth_payload = {
                    'request-type': 'Authenticate',
                    'auth': auth,
                }

                def auth_cb2(msg):
                    if msg['status'] == 'error':
                        if msg['error'] == 'Authentication Failed.':
                            self.set_status('failed')

                    elif msg['status'] == 'ok':
                        self.set_status('active')

                self._send(auth_payload, auth_cb2)
            else:
                self.set_status('active')

        self._send({'request-type': 'GetAuthRequired'}, auth_cb)

    def disconnected(self):
        if self.we_closed:
            self.we_closed = False
            self.set_status('inactive')
            return
        self.set_status('reconnecting')
        self.retry()

    def retry(self):
        self.reconnect_attempts += 1
        if self.reconnect_attempts >= self.max_attempts:
            self.log.info('Max retry attempts reached, aborting')
            self.set_status('inactive')
            return

        self.set_status('reconnecting')
        if isValid(self.socket):
            self.socket.close()
            self.log.info('Attempting to reconnect')
            self.socket.open(self.url)

    def open(self, url, port, password=''):
        self.url = QUrl(f'ws://{url}:{port}')
        self.log.info(f'Attempting to connect to OBS at: {self.url}')
        self.password = password
        self.socket.open(self.url)

    def close(self):
        self.log.info(f'Closing socket')
        self.socket.close()

    def _send(self, payload, callback=None):
        payload['message-id'] = str(self.id)
        self.history[self.id] = payload

        self.log.info(f'TX: {payload}')

        if callback:
            self.callbacks[str(self.id)] = callback

        message = json.dumps(payload)
        self.socket.sendTextMessage(message)
        self.id += 1

    def send(self, payload, callback=None):
        if self.active:
            self._send(payload, callback)
        else:
            self.queue.put((payload, callback))

    def process_queue(self):
        while not self.queue.empty():
            payload, callback = self.queue.get()
            self._send(payload, callback)

    def recieve(self, message):
        self.raw_message_received.emit(message)
        msg = json.loads(message)
        self.message_received.emit(msg)

        self.log.info(f'RX: {message}')

        # process callbacks
        if 'message-id' in msg:
            if msg['message-id'] in self.callbacks:
                self.callbacks[msg['message-id']](msg)
        if 'update-type' in msg:
            self.event_received.emit(msg)
