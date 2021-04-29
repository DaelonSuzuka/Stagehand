from qtstrap import *
from codex import DeviceManager
from .actions import ActionWidget, ActionWidgetGroup


class InputDeviceInfoTab(QWidget):
    def __init__(self, known_devices, parent=None):
        super().__init__(parent=parent)
    
        self.known_devices = QListWidget(self)
        for _, d in known_devices.items():
            self.known_devices.addItem(f"{d['profile_name']} - {d['guid']}")

        with CHBoxLayout(self) as layout:
            with layout.vbox(1):
                layout.add(QLabel("Known Devices:"))
                layout.add(self.known_devices)
            with layout.vbox(1):
                layout.add(QLabel('wat'))


@DeviceManager.subscribe
class InputDeviceManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.known_devices = QSettings().value(f'input_devices/known_devices', {})
        self.widgets = {}
        self.info_tab = InputDeviceInfoTab(self.known_devices)

        self.tabs = PersistentTabWidget('input_devices/tabs')
        self.tabs.addTab(self.info_tab, 'Device Info')

        with CVBoxLayout(self) as layout:
            layout.add(self.tabs)

        for guid, device in self.known_devices.items():
            self.create_widget(guid, device['profile_name'])

        self.tabs.restore_state()

    def create_widget(self, guid, profile_name):
        if profile_name in DeviceManager.profiles():
            profile = DeviceManager.profiles()[profile_name]
            if hasattr(profile, 'widget'):
                widget = profile.widget(guid, self)
                self.widgets[guid] = widget
                self.tabs.addTab(widget, profile_name)

    def device_added(self, device):
        if device.guid not in self.known_devices:
            self.known_devices[device.guid] = device.description
            self.create_widget(device.guid, device.profile_name)

            QSettings().setValue(f'input_devices/known_devices', self.known_devices)
        
        if device.guid in self.widgets:
            self.widgets[device.guid].connect_device(device)
            
