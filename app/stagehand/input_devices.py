from qtstrap import *
from codex import DeviceManager
from .actions import ActionWidget, ActionWidgetGroup
from stagehand.main_window import StagehandWidget, SidebarButton
import qtawesome as qta


@DeviceManager.subscribe
class InputDeviceManager(StagehandWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent

        self.known_devices = QSettings().value(f'input_devices/known_devices', {})
        self.widgets = {}

        self.sidebar_button = SidebarButton(target=self, icon=qta.icon('mdi.format-list-text'))

        self.known_devices_list = QListWidget(self, fixedWidth=150)
        self.widget_stack = QStackedWidget()
        self.known_devices_list.currentRowChanged.connect(self.widget_stack.setCurrentIndex)
        
        for _, d in self.known_devices.items():
            self.known_devices_list.addItem(f"{d['profile_name']} - {d['guid']}")

        with CHBoxLayout(self) as layout:
            with layout.vbox():
                layout.add(QLabel("Known Devices:"))
                layout.add(self.known_devices_list)
            layout.add(self.widget_stack, 1)

        for guid, device in self.known_devices.items():
            self.create_widget(guid, device['profile_name'])

    def create_widget(self, guid, profile_name):
        if profile_name in DeviceManager.profiles():
            profile = DeviceManager.profiles()[profile_name]
            if hasattr(profile, 'widget'):
                widget = profile.widget(guid, self.parent)
                self.widgets[guid] = widget
                self.widget_stack.addWidget(widget)

    def device_added(self, device):
        if device.guid not in self.known_devices:
            self.known_devices[device.guid] = device.description
            self.create_widget(device.guid, device.profile_name)

            QSettings().setValue(f'input_devices/known_devices', self.known_devices)
        
        if device.guid in self.widgets:
            self.widgets[device.guid].connect_device(device)
            
