from qt import *
import json


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

    def __init__(self, parent=None, url='localhost', port='4444'):
        super().__init__(parent=parent)
        self.url = url
        self.port = port
        self.id = 0

        self.socket = QWebSocket()
        self.socket.connected.connect(self.connected)
        self.socket.disconnected.connect(self.disconnected)
        self.socket.textMessageReceived.connect(self.recieve)

        self.history = {}

        self.status = QLabel('Not Connected')
        self.status_widget = ObsStatusWidget()

        self.url_box = QLineEdit(placeholderText='localhost')
        self.port_box = QLineEdit(placeholderText='4444')
        self.connect_btn = QPushButton('Connect')
        self.rx_history_box = QTextEdit(readOnly=True)
        self.tx_history_box = QTextEdit(readOnly=True)

        self.open()

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Status:'))
                layout.add(self.status)
            with layout.hbox(align='left'):
                layout.add(QLabel('Address:'))
                layout.add(self.url_box)
                layout.add(QLabel('Port:'))
                layout.add(self.port_box)
                layout.add(self.connect_btn)
                layout.add(QLabel(), 1)
            # with layout.hbox():
            #     with layout.vbox():
            #         layout.add(QLabel('TX History:'))
            #         layout.add(self.tx_history_box)
            #     with layout.vbox():
            #         layout.add(QLabel('RX History:'))
            #         layout.add(self.rx_history_box)
    
    def connected(self):
        self.status.setText('Connected')
        self.status_widget.setText('Connected')
        self.send({"request-type": "GetAuthRequired"})

    def disconnected(self):
        self.status.setText('Not Connected')
        self.status_widget.setText('Not Connected')

    def open(self, url=None, port=None):
        if url:
            self.url = url
        if port:
            self.port = port
        address = f'ws://{self.url}:{self.port}'
        # self.address.setText(address)
        self.socket.open(QUrl(address))

    def send(self, payload):
        payload['message-id'] = str(self.id)
        self.history[self.id] = payload

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
            # self.send({"request-type": 'GetVersion'})
            # self.send({"request-type": 'GetSceneList'})
            self.send({"request-type": 'GetSourcesList'})
            # self.send({"request-type": 'ListOutputs'})

    # def _GetVersion(self, msg):
    #     pass
        # self.available_requests = msg['available-requests'].split(',')
        # print(self.available_requests)

    # def _GetSceneList(self, msg):
    #     for scene in msg['scenes']:
    #         self.scenes[scene['name']] = scene
    
    # def _GetSourcesList(self, msg):
    #     for source in msg['sources']:
    #         self.sources[source['name']] = source

    
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
