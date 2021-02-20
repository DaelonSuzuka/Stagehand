from qt import *
from devices import DeviceControlsDockWidget
from judipedal_controls import JudiPedalsControls
import json
import struct
import sounddevice as sd
import numpy as np


class ObsManager(QObject):
    message_recieved = Signal(str)

    def __init__(self, parent=None, url='localhost', port='4444'):
        super().__init__(parent=parent)
        self.url = url
        self.port = port
        self.id = 0

        self.socket = QWebSocket()
        self.socket.connected.connect(self.connected)
        self.socket.textMessageReceived.connect(self.recieve)

        self.history = {}

        self.scenes = {}
        self.sources = {}

        self.open()
    
    def connected(self):
        self.send({"request-type": "GetAuthRequired"})

    def open(self, url=None, port=None):
        if url:
            self.url = url
        if port:
            self.port = port
        self.socket.open(QUrl(f'ws://{self.url}:{self.port}'))

    def send(self, payload):
        payload['message-id'] = str(self.id)
        self.history[self.id] = payload
        self.socket.sendTextMessage(json.dumps(payload))
        self.id += 1

    def get_previous_request_type(self, msg):
        return self.history[int(msg['message-id'])]['request-type']

    def recieve(self, message):
        self.message_recieved.emit(message)
        msg = json.loads(message)

        if 'error' in msg:
            print('error:', self.get_previous_request_type(msg))

        # process responses
        if 'message-id' in msg:
            prev = self.get_previous_request_type(msg)
            if f'_{prev}' in dir(self):
                getattr(self, f'_{prev}')(msg)

    def _GetAuthRequired(self, msg):
        if msg['authRequired'] == False:
            self.active = True
            self.send({"request-type": 'GetVersion'})
            self.send({"request-type": 'GetSceneList'})
            self.send({"request-type": 'GetSourcesList'})
            self.send({"request-type": 'ListOutputs'})

    def _GetVersion(self, msg):
        pass
        # self.available_requests = msg['available-requests'].split(',')
        # print(self.available_requests)

    def _GetSceneList(self, msg):
        for scene in msg['scenes']:
            self.scenes[scene['name']] = scene
    
    def _GetSourcesList(self, msg):
        for source in msg['sources']:
            self.sources[source['name']] = source

    
        # if 'update-type' in msg:
        #     if msg['update-type'] == 'SwitchScenes':
        #         self.current_scene.setText(msg['scene-name'])
        #         self.sources.clear()
        #         for source in msg['sources']:
        #             self.sources.addItem(source['name'])
        # else:
        #     if 'current-scene' in msg:
        #         self.current_scene.setText(msg['current-scene'])
                
        #     if 'sources' in msg:
        #         for source in msg['sources']:
        #             self.sources.addItem(source['name'])

        #     if 'scenes' in msg:
        #         for scene in msg['scenes']:
        #             self.scenes.addItem(scene['name'])


class ObsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._id = 0
        self.active = False

        self.obs = ObsManager()

        self.payload = QLineEdit()
        self.payload.returnPressed.connect(self.enter)
        self.history = QTextEdit()

        self.obs.message_recieved.connect(lambda s: self.history.append(s))

        self.scenes = QListWidget()
        self.current_scene = QLabel('Unknown')
        self.sources = QListWidget()

        self.stream = sd.InputStream(48000)
        self.stream.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.process_audio)
        self.timer.start(50)

        self.meter = QLabel()
        self.prev_amplitude = 0
        self.amplitude = 0

        with CVBoxLayout(self) as layout:
            layout.add(self.meter)
            with layout.hbox() as layout:
                with layout.vbox() as layout:
                    layout.add(QLabel('Scenes:'))
                    layout.add(self.scenes)
                    layout.add(QLabel('Sources:'))
                    layout.add(self.current_scene)
                    layout.add(self.sources)
                with layout.vbox() as layout:    
                    layout.add(self.payload)
                    layout.add(self.history)

    def process_audio(self):
        buffer, _ = self.stream.read(self.stream.read_available)
        floats = [f[0] for f in struct.iter_unpack("<f", buffer)]
        raw = sum(f**2 for f in floats)

        self.amplitude = self.amplitude - (0.2 * self.amplitude - raw)
        gain = int(self.amplitude * 10)
        if gain > 50:
            gain = 50
        self.meter.setText('|' * gain)

    def pedal(self, number):
        if not self.active:
            return

        actions = {
            1: lambda: self.send({"request-type": "GetSceneList"}),
            2: lambda: self.send({"request-type": "GetSourcesList"}),
            3: lambda: self.send({"request-type": "GetAuthRequired"}),
            4: lambda: self.send({"request-type": "GetAuthRequired"}),
        }

        actions[number]()

    def enter(self):
        self.obs.send({"request-type": self.payload.text()})


class MainWindow(BaseMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("MainWindow")

        self.device_controls = DeviceControlsDockWidget(self)
        self.socket = ObsWidget()
        self.pedals = JudiPedalsControls()
        self.pedals.pedal_pressed.connect(self.socket.pedal)

        widget = QWidget()
        self.setCentralWidget(widget)
        with CVBoxLayout(widget) as layout:
            layout.add(self.socket)
            layout.add(self.pedals)