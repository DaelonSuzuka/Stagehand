from qtstrap import *
from stagehand.obs import ActionWidget, ActionWidgetGroup


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