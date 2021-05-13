from qtstrap import *
from stagehand.actions import TriggerStackItem


class Stomp5Trigger(QWidget, TriggerStackItem):
    triggered = Signal()

    def __init__(self, changed, run):
        super().__init__()
        
        self.triggered.connect(run)

        self.number = QComboBox()
        self.number.addItems(['1', '2', '3', '4', '5'])
        self.number.currentIndexChanged.connect(changed)

        self.direction = QComboBox()
        self.direction.addItems(['press', 'release'])
        self.direction.currentIndexChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.number)
            layout.add(self.direction)

    def from_dict(self, data):
        try:
            self.direction.setCurrentText(data['direction'])
            self.number.setCurrentText(data['number'])
        except:
            pass

    def to_dict(self):
        return {
            'direction': self.direction.currentText(),
            'number': self.number.currentText(),
        }
