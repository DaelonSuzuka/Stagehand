from qtstrap import *
from codex import DeviceManager
from .actions import ActionWidget, ActionWidgetGroup, TriggerItem
from stagehand.components import StagehandWidget


class DeviceTrigger(QWidget, TriggerItem):
    name = 'device'
    triggered = Signal()

    def __init__(self, changed, run, owner=None):
        super().__init__()

        self.owner = owner
        self.trigger = QLineEdit()
        self.trigger.textChanged.connect(changed)

        self.device = QComboBox()
        self.event_ = QComboBox()
        
        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.device)
            layout.add(self.event_)

    def reset(self):
        self.trigger.clear()
        
    def set_data(self, data: dict):
        if 'trigger' in data:
            self.trigger.setText(data['trigger'])

    def get_data(self):
        return {
            'trigger': self.trigger.text()
        }


class InputDeviceList(QListWidget):
    device_removed = Signal(str)

    def __init__(self, *args, on_remove=None, **kwargs):
        super().__init__(*args, **kwargs)
        if on_remove:
            self.device_removed.connect(on_remove)

    def contextMenuEvent(self, event):
        menu = QMenu('', self)
        menu.addAction(QAction("Remove Device", self, triggered=self.remove_device))
        menu.exec_(event.globalPos())

    def add_device(self, device):
        item = QListWidgetItem(f"{device['profile_name']} - {device['guid']}")
        item.guid = device['guid']
        self.addItem(item)

    def remove_device(self):
        item = self.selectedItems()[0]
        self.device_removed.emit(item.guid)
        self.takeItem(self.row(item))


@DeviceManager.subscribe
class InputDeviceManager(StagehandWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, icon_name='mdi.format-list-text', **kwargs)
        self.parent = parent

        self.known_devices = QSettings().value(f'input_devices/known_devices', {})
        self.widgets = {}

        self.known_devices_list = InputDeviceList(self, on_remove=self.remove_widget, fixedWidth=150)
        self.widget_stack = QStackedWidget()
        self.known_devices_list.currentRowChanged.connect(self.widget_stack.setCurrentIndex)
        
        for _, d in self.known_devices.items():
            self.known_devices_list.add_device(d)

        with PersistentCSplitter('input_devices_splitter', self, margins=(0,0,0,0)) as split:
            split.setOrientation(Qt.Horizontal)
            with CVBoxLayout(margins=(0,0,0,0)) as layout:
                split.add(layout, 1)
                layout.add(QLabel("Known Devices:"))
                layout.add(self.known_devices_list)
            split.add(self.widget_stack, 1)

        for guid, device in self.known_devices.items():
            self.create_widget(guid, device['profile_name'])

    def create_widget(self, guid, profile_name):
        if profile_name in DeviceManager.profiles():
            profile = DeviceManager.profiles()[profile_name]
            if hasattr(profile, 'widget'):
                widget = profile.widget(guid, self.parent)
                self.widgets[guid] = widget
                self.widget_stack.addWidget(widget)

    def remove_widget(self, guid):
        if guid in self.known_devices:
            self.known_devices.pop(guid)
            self.widget_stack.removeWidget(self.widgets.pop(guid))
        
            QSettings().setValue(f'input_devices/known_devices', self.known_devices)

    def device_added(self, device):
        if device.guid not in self.known_devices:
            self.known_devices[device.guid] = device.description
            self.create_widget(device.guid, device.profile_name)
            self.known_devices_list.add_device(device.description)

            QSettings().setValue(f'input_devices/known_devices', self.known_devices)
        
        if device.guid in self.widgets:
            self.widgets[device.guid].connect_device(device)
