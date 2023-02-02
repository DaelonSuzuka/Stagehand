from qtstrap import *
from qtpy.QtWebSockets import *
from qtpy.shiboken import isValid
import json
import queue
import logging


class _TeamSpeakSocket(QObject):
    status_changed = Signal(str)
    message_received = Signal(dict)
    raw_message_received = Signal(str)
    socket_connected = Signal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.log = logging.getLogger(__name__)

        self.id = 0
        self.active = False
        self.we_closed = False
        self.reconnect_attempts = 0
        self.max_attempts = 5

        self.url = ''
        self.api_key = ''

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
        auth = {
            "type": "auth",
            "payload": {
                "identifier": "net.stagehand",
                "version": "1.0.0",
                "name": "Stagehand",
                "description": "An example application that does things",
                "content": {
                    "apiKey": self.api_key
                }
            }
        }
        self._send(auth)

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
            self.set_status('inactive')
            return

        self.set_status('reconnecting')
        if isValid(self.socket):
            self.socket.close()
            self.socket.open(self.url)
        self.socket.close()
        self.socket.open(self.url)

    def open(self, url, port, api_key=''):
        self.url = QUrl(f'ws://{url}:{port}')
        self.log.info(f"Attempting to connect to TeamSpeak at: {self.url}")
        self.api_key = api_key
        self.socket.open(self.url)

    def close(self):
        self.log.info(f"Closing socket")
        self.socket.close()

    @trace
    def _send(self, payload):
        self.history[self.id] = payload

        self.log.info(f"TX: {payload}")

        message = json.dumps(payload)
        self.socket.sendTextMessage(message)
        self.id += 1

    @trace
    def send(self, payload):
        if self.active:
            self._send(payload)
        else:
            self.queue.put((payload))

    def process_queue(self):
        while not self.queue.empty():
            payload = self.queue.get()
            self._send(payload)

    def recieve(self, message):
        self.raw_message_received.emit(message)
        msg = json.loads(message)
        self.message_received.emit(msg)

        self.log.info(f"RX: {message}")

        if msg['type'] == 'auth':
            if msg['status']['code'] == 0:
                api_key = msg['payload']['apiKey']
                QSettings().setValue('teamspeak/api_key', api_key)
                self.api_key = api_key
                self.set_status('active')



socket = None


def TeamSpeakSocket(parent=None):
    global socket
    if socket is None:
        socket = _TeamSpeakSocket(parent)
    return socket