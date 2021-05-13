from qtstrap import *
from stagehand.actions import TriggerStackItem
from codex import SubscriptionManager


@SubscriptionManager.subscribe
class Stomp5Trigger(QWidget, TriggerStackItem):
    triggered = Signal()

    def __init__(self, changed, run):
        super().__init__()
        
        self.triggered.connect(run)
        self.devices = {}

        self.device = QComboBox()
        self.device.currentIndexChanged.connect(changed)
        self.device.currentTextChanged.connect(self.device_changed)

        self.signal = QComboBox()
        self.signal.addItems([
            '1 Pressed',
            '1 Released',
            '2 Pressed',
            '2 Released',
            '3 Pressed',
            '3 Released',
            '4 Pressed',
            '4 Released',
            '5 Pressed',
            '5 Released',
        ])

        self.pedal = QComboBox()
        self.pedal.addItems(['1', '2', '3', '4', '5'])
        self.pedal.currentIndexChanged.connect(changed)

        self.direction = QComboBox()
        self.direction.addItems(['press', 'release'])
        self.direction.currentIndexChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.device)
            layout.add(self.signal)
    
    def device_changed(self, guid):
        if guid in self.devices:
            adapter = self.devices[guid].get_adapter()

    def device_added(self, device):
        if device.profile_name == 'Stomp 5':
            self.devices[device.guid] = device
            with SignalBlocker(self.device):
                selected = self.device.currentText()
                self.device.clear()
                items = sorted(self.devices.keys())
                if selected not in items:
                    items.insert(0, selected)
                self.device.addItems(items)
                self.device.setCurrentText(selected)

    def from_dict(self, data):
        try:
            self.direction.setCurrentText(data['direction'])
            self.pedal.setCurrentText(data['pedal'])
            if data['device'] not in self.devices:
                self.device.addItem(data['device'])
            self.device.setCurrentText(data['device'])
        except:
            pass

    def to_dict(self):
        return {
            'direction': self.direction.currentText(),
            'pedal': self.pedal.currentText(),
            'device': self.device.currentText(),
        }
