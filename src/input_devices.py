from qtstrap import *
from codex import DeviceManager
from obs import ActionWidget, ActionWidgetGroup


class PedalActions(QWidget):
    def __init__(self, name, group, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.state = QLabel('up')
        self.press = ActionWidget(f'{name} Pressed', group)
        self.release = ActionWidget(f'{name} Released', group)

        with CVBoxLayout(self, margins=(0,0,0,0)) as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel(f'{self.name} Status:'))
                layout.add(self.state)
            layout.add(self.press)
            layout.add(self.release)


class Stomp4Widget(QWidget):
    def __init__(self, guid, parent=None):
        super().__init__(parent=parent)
        self.guid = guid

        self.group = ActionWidgetGroup(f'input_devices/{guid}', self)

        self.pedals = []
        for i in range(1, 5):
            self.pedals.append(PedalActions(f'Pedal {i}', self.group))

        self.status = QLabel("Not Connected")

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Device Status:'))
                layout.add(self.status)

            layout.add(QLabel())
            layout.add(HLine())

            for pedal in self.pedals:
                layout.add(pedal)

            layout.add(QLabel(), 1)

    def connect_device(self, device):
        self.status.setText('Connected')
        device.signals.button_pressed.connect(self.button_pressed)
        device.signals.button_released.connect(self.button_released)

    def button_pressed(self, button):
        number = int(button) - 1
        self.pedals[number].press.run()
        self.pedals[number].state.setText('down')

    def button_released(self, button):
        number = int(button) - 1
        self.pedals[number].release.run()
        self.pedals[number].state.setText('up')


class Stomp5Widget(QWidget):
    def __init__(self, guid, parent=None):
        super().__init__(parent=parent)
        self.guid = guid

        self.group = ActionWidgetGroup(f'input_devices/{guid}', self)
        self.pedals = []
        for i in range(1, 6):
            self.pedals.append(PedalActions(f'Pedal {i}', self.group))

        self.status = QLabel("Not Connected")

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Device Status:'))
                layout.add(self.status)

            layout.add(QLabel())
            layout.add(HLine())

            for pedal in self.pedals:
                layout.add(pedal)

            layout.add(QLabel(), 1)

    def connect_device(self, device):
        self.status.setText('Connected')
        device.signals.button_pressed.connect(self.button_pressed)
        device.signals.button_released.connect(self.button_released)

    def button_pressed(self, button):
        number = int(button) - 1
        self.pedals[number].press.run()
        self.pedals[number].state.setText('down')

    def button_released(self, button):
        number = int(button) - 1
        self.pedals[number].release.run()
        self.pedals[number].state.setText('up')


device_widgets = {
    "Stomp 4": Stomp4Widget,
    "Stomp 5": Stomp5Widget,
}


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
        if profile_name in device_widgets:
            widget = device_widgets[profile_name](guid, self)
            self.widgets[guid] = widget
            self.tabs.addTab(widget, profile_name)

    def device_added(self, device):
        if device.guid not in self.known_devices:
            self.known_devices[device.guid] = device.description
            self.create_widget(device.guid, device.profile_name)

            QSettings().setValue(f'input_devices/known_devices', self.known_devices)
        
        if device.guid in self.widgets:
            self.widgets[device.guid].connect_device(device)
            
