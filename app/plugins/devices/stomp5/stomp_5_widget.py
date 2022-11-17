from qtstrap import *
from stagehand.actions import ActionWidget, ActionWidgetGroup


class PedalActions(QWidget):
    def __init__(self, name, group, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.state = QLabel('up')
        self.press = ActionWidget(f'{name} Pressed', group)
        self.release = ActionWidget(f'{name} Released', group)

        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel(f'{self.name} Status:'))
                layout.add(self.state)
            layout.add(self.press)
            layout.add(self.release)


class Stomp5Widget(QWidget):
    def __init__(self, guid, parent=None):
        super().__init__(parent=parent)
        self.guid = guid

        self.group = ActionWidgetGroup(f'input_devices/{guid}', self)
        self.pedals = [PedalActions(f'Pedal {i}', self.group) for i in range(1, 6)]

        self.status = QLabel("Not Connected")

        with CVBoxLayout(self, margins=0, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Device Status:'))
                layout.add(self.status)

            layout.add(QWidget())
            layout.add(HLine())

            for pedal in self.pedals:
                layout.add(pedal)

            layout.add(QWidget(), 1)

    def connect_device(self, device):
        self.status.setText('Connected')
        self.adapter = device.signals.adapter()
        self.adapter.button_pressed.connect(self.button_pressed)
        self.adapter.button_released.connect(self.button_released)

    def button_pressed(self, button):
        number = int(button) - 1
        self.pedals[number].press.run()
        self.pedals[number].state.setText('down')

    def button_released(self, button):
        number = int(button) - 1
        self.pedals[number].release.run()
        self.pedals[number].state.setText('up')