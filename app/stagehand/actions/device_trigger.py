from qtstrap import *
import qtawesome as qta
from stagehand.actions import TriggerItem
from codex import DeviceManager, SubscriptionManager
from enum import Enum


class Status(Enum):
    CONNECTED = 0
    DISCONNECTED = 1


@singleton
class KnownDevices:
    def __init__(self):
        # TODO: sanitization
        self._registry: list = QSettings().value('devices/known_devices', [])

    def append(self, device):
        if device not in self._registry:
            self._registry.append(device)
            self._registry = sorted(self._registry)
            QSettings().setValue('devices/known_devices', self._registry)

    def get_display_name(self, full_name):
        parts = full_name.split(':')
        return f'{parts[0]}: {parts[1][-6:]}'

    def get_display_names(self):
        return [self.get_display_name(i) for i in self._registry]

    def get_full_name(self, display_name):
        name_map = {self.get_display_name(i): i for i in self._registry}
        return name_map[display_name]


@SubscriptionManager.subscribe
class DeviceTrigger(QWidget, TriggerItem):
    name = 'device'
    triggered = Signal()
    
    def __init__(self, changed, run, owner=None):
        super().__init__()

        self.changed = changed
        self.owner = owner
        self.triggered.connect(run)

        self.adapter = None
        self.current_guid = None

        self.device_selector = QComboBox()
        self.device_selector.setMinimumWidth(200)
        self.device_selector.currentIndexChanged.connect(changed)
        self.device_selector.currentTextChanged.connect(self.device_changed)
        
        self.event_selector = QComboBox()
        self.event_selector.setMinimumWidth(150)
        self.event_selector.currentIndexChanged.connect(changed)

        self.connected = qta.icon('mdi.link-variant').pixmap(QSize(25, 25))
        self.disconnected = qta.icon('mdi.link-variant-off').pixmap(QSize(25, 25))

        self.status = QLabel('')
        self.set_status(Status.DISCONNECTED)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.device_selector)
            layout.add(self.status)
            layout.add(QLabel('Event:'))
            layout.add(self.event_selector)
    
    def set_status(self, status:Status):
        if status is Status.CONNECTED:
            self.status.setEnabled(True)
            self.status.setToolTip('Device is connected')
            self.status.setPixmap(self.connected)

        if status is Status.DISCONNECTED:
            self.status.setEnabled(False)
            self.status.setToolTip('Device is disconnected')
            self.status.setPixmap(self.disconnected)

    def device_changed(self, display_name):
        self.set_status(Status.DISCONNECTED)

        full_name = KnownDevices().get_full_name(display_name)
        parts = full_name.split(':')
        name = parts[0]
        guid = parts[1]

        if guid in self.devices:
            if self.adapter:
                self.adapter.deleteLater()
            self.adapter = self.devices[guid].signals.adapter()
            
            if hasattr(self.adapter, 'event_recieved'):
                self.adapter.event_recieved.connect(self.event_recieved)
            self.set_status(Status.CONNECTED)

        profile = DeviceManager.profiles()[name]
        if hasattr(profile, 'events'):
            with SignalBlocker(self.event_selector):
                selected = self.event_selector.currentText()
                self.event_selector.clear()

                items = profile.events

                if selected:
                    if selected not in items:
                        items.insert(0, selected)
                self.event_selector.addItems(items)
            if selected:
                self.event_selector.setCurrentText(selected)
        else:
            self.event_selector.clear()

    def event_recieved(self, event):
        if event == self.event_selector.currentText():
            self.triggered.emit()

    def refresh_devices(self):
        with SignalBlocker(self.device_selector):
            selected = self.device_selector.currentText()
            self.device_selector.clear()

            items = KnownDevices().get_display_names()

            if selected:
                if selected not in items:
                    items.insert(0, selected)
            self.device_selector.addItems(items)
            if selected:
                self.device_selector.setCurrentText(selected)

    def device_added(self, device):
        KnownDevices().append(f'{device.profile_name}:{device.guid}')
        self.refresh_devices()

        display_name = self.device_selector.currentText()
        full_name = KnownDevices().get_full_name(display_name)
        parts = full_name.split(':')
        name = parts[0]
        guid = parts[1]

        if device.profile_name == name and device.guid == guid:
            self.device_changed(self.device_selector.currentText())

    def set_data(self, data):
        self.refresh_devices()
        if 'device' in data:
            self.device_selector.setCurrentText(data['device'])
            self.event_selector.setCurrentText(data['event'])
            self.device_changed(data['device'])

    def get_data(self):
        return {
            'device': self.device_selector.currentText(),
            'event': self.event_selector.currentText(),
        }