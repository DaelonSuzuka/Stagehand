from qt import *
from devices import DeviceControlsDockWidget
from judipedal_controls import JudiPedalsControls
import json


class ObsSocket(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._id = 0
        self.active = False

        self.socket = QWebSocket()
        self.socket.connected.connect(self.on_connected)
        self.socket.textMessageReceived.connect(self.recieve)
        self.socket.open(QUrl('ws://127.0.0.1:4444'))

        self.payload = QLineEdit()
        self.payload.returnPressed.connect(self.enter)
        self.text = QTextEdit()

        self.scenes = QListWidget()
        self.current_scene = QLabel('Unknown')
        self.sources = QListWidget()

        with CHBoxLayout(self) as layout:
            with layout.vbox() as layout:    
                layout.add(self.scenes)
                layout.add(self.current_scene)
                layout.add(self.sources)
            with layout.vbox() as layout:    
                layout.add(self.payload)
                layout.add(self.text)

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
        self.send({"request-type": self.payload.text()})

    def on_connected(self):
        self.send({"request-type": "GetAuthRequired"})

    def send(self, payload):
        payload['message-id'] = str(self.id)
        self.socket.sendTextMessage(json.dumps(payload))

    def recieve(self, message):
        self.text.setText(message)
        msg = json.loads(message)

        if 'authRequired' in msg:
            if msg['authRequired'] == False and msg['status'] == 'ok':
                self.active = True
                self.send({"request-type": 'GetSceneList'})
                self.send({"request-type": 'GetSourcesList'})
                self.send({"request-type": 'GetCurrentScene'})

        if 'scene-name' in msg:
            self.current_scene.setText(msg['scene-name'])
            
        if 'sources' in msg:
            for source in msg['sources']:
                self.sources.addItem(source['name'])

        if 'scenes' in msg:
            for scene in msg['scenes']:
                self.scenes.addItem(scene['name'])

    @property
    def id(self):
        self._id += 1
        return self._id


class MainWindow(BaseMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("MainWindow")

        self.device_controls = DeviceControlsDockWidget(self)
        self.socket = ObsSocket()
        self.pedals = JudiPedalsControls()
        self.pedals.pedal_pressed.connect(self.socket.pedal)

        widget = QWidget()
        self.setCentralWidget(widget)
        with CVBoxLayout(widget) as layout:
            layout.add(self.socket)
            layout.add(self.pedals)