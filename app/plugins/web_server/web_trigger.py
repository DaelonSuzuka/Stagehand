from qtstrap import *
from stagehand.actions import TriggerItem
from .web_interface import SocketListener
import json


class WebTrigger(QWidget, TriggerItem):
    name = 'web'
    triggered = Signal()

    def __init__(self, changed, run):
        super().__init__()
        
        self.triggered.connect(run)

        self.socket = SocketListener()
        self.socket.message_recieved.connect(self.processTextMessage)

        self.action = QComboBox()
        items = [f'Action {i + 1}' for i in range(12)]
        self.action.addItems(items)
        self.action.currentIndexChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.action)

    def processTextMessage(self, text):
        try:
            msg = json.loads(text)
            if 'command' in msg and msg['command'] == 'click':
                if self.action.currentText() == f"Action {msg['button']}":
                    self.triggered.emit()
        except:
            pass

    def from_dict(self, data):
        try:
            self.action.setCurrentText(data['action'])
        except:
            pass

    def to_dict(self):
        return {
            'action': self.action.currentText(),
        }
