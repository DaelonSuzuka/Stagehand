from qtstrap import *
from stagehand.actions import FilterStackItem
from codex import SubscriptionManager


@SubscriptionManager.subscribe
class Stomp4Filter(QWidget, FilterStackItem):
    name = 'Stomp 4'

    def __init__(self, changed, owner=None) -> None:
        super().__init__()

        self.owner = owner
        self.stomps = {}
        self.adapter = None
        self.current_guid = None

        self.device = QComboBox()
        self.device.currentIndexChanged.connect(changed)
        self.device.currentTextChanged.connect(self.device_changed)

        self.signal = QComboBox()
        self.state = {
            '1': False,
            '2': False,
            '3': False,
            '4': False,
        }

        # [f'{n} {d}' for n, d in zip(['1','2','3','4','5'], ['Up', 'Down'])]
        self.signal.addItems([
            '1 Down', '1 Up',
            '2 Down', '2 Up',
            '3 Down', '3 Up',
            '4 Down', '4 Up',
        ])
        self.signal.currentIndexChanged.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.device)
            layout.add(self.signal)

    def device_changed(self, guid):
        if guid in self.stomps:
            if self.adapter:
                self.adapter.kill()
                self.adapter.deleteLater()
            self.adapter = self.stomps[guid].signals.adapter()
            self.adapter.button_pressed.connect(self.button_pressed)
            self.adapter.button_released.connect(self.button_released)

    def button_pressed(self, button):
        if self.signal.currentText()[0] == button:
            self.state[button] = True

    def button_released(self, button):
        if self.signal.currentText()[0] == button:
            self.state[button] = False

    def refresh_devices(self):
        with SignalBlocker(self.device):
            selected = self.device.currentText()
            self.device.clear()
            items = sorted(self.stomps.keys())
            if selected:
                if selected not in items:
                    items.insert(0, selected)
            self.device.addItems(items)
            if selected:
                self.device.setCurrentText(selected)

    def device_added(self, device):
        if device.profile_name == self.name:
            # the full GUID is way too long, so truncate it at six characters
            self.stomps[device.guid[-6:]] = device
            self.refresh_devices()
            self.device_changed(self.device.currentText())

    def check(self) -> bool:
        button = self.signal.currentText()[0]
        state = self.state[button]
        
        if self.signal.currentText()[2:] == 'Down':
            return state
        else:
            return not state

    def set_data(self, data):
        try:
            if data['device'] not in self.devices:
                self.device.addItem(data['device'])
            self.device.setCurrentText(data['device'])
            self.signal.setCurrentText(data['signal'])
        except:
            pass

    def get_data(self):
        return {
            'signal': self.signal.currentText(),
            'device': self.device.currentText(),
        }
