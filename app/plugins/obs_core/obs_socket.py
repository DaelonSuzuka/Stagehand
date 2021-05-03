from qtstrap import *
from qtpy.QtWebSockets import *
import json
import base64
import hashlib
import queue


class _ObsSocket(QObject):
    status_changed = Signal(str)
    message_received = Signal(dict)
    raw_message_received = Signal(str)
    socket_connected = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.id = 0
        self.active = False

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
            self.active = True
            self.socket_connected.emit()
            self.process_queue()

        elif status == 'inactive':
            self.active = False

        elif status == 'failed':
            self.active = False

    def connected(self):
        def auth_cb(msg):
            if msg['authRequired']:
                # apparently this is how you process the challege/response
                # this is shamelessly lifted from obs-websocket-py:
                # https://github.com/Elektordi/obs-websocket-py/blob/master/obswebsocket/core.py#L120
                secret = base64.b64encode(
                    hashlib.sha256(
                        (self.password + msg['salt']).encode('utf-8')
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

                self._send(auth_payload, auth_cb2)
            else:
                self.set_status('active')

        self._send({"request-type": "GetAuthRequired"}, auth_cb)

    def disconnected(self):
        self.set_status('inactive')

    def open(self, url, port, password):
        self.password = password
        self.socket.open(QUrl(f'ws://{url}:{port}'))

    def _send(self, payload, callback=None):
        payload['message-id'] = str(self.id)
        self.history[self.id] = payload

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

        # process callbacks
        if 'message-id' in msg:
            if msg['message-id'] in self.callbacks:
                self.callbacks[msg['message-id']](msg)


socket = None


def ObsSocket(parent=None):
    global socket
    if socket is None:
        socket = _ObsSocket(parent)
    return socket