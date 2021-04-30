from qtstrap import *
from stagehand.actions import ActionWidget, ActionWidgetGroup


class PedalActions(QWidget):
    def __init__(self, name, group, parent=None):
        super().__init__(parent=parent)
        self.name = name
        self.state = QLabel('up')
        self.press = ActionWidget(f'{name} Pressed', group)
        self.release = ActionWidget(f'{name} Released', group)

        with CVBoxLayout(self, margins=(0,0,0,0)) as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel(f'{self.name}'))
                layout.add(QLabel(''), 1)
                layout.add(QLabel(f'Status:'))
                layout.add(self.state)
            layout.add(self.press)
            layout.add(self.release)


class Click4Widget(QWidget):
    def __init__(self, guid, parent=None):
        super().__init__(parent=parent)
        self.guid = guid

        self.group = ActionWidgetGroup(f'input_devices/{guid}', self)

        self.buttons = []
        for i in range(1, 5):
            self.buttons.append(PedalActions(f'Button {i}', self.group))

        self.status = QLabel("Not Connected")

        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Device Status:'))
                layout.add(self.status)

            layout.add(QLabel())
            layout.add(HLine())

            for pedal in self.buttons:
                layout.add(pedal)

            layout.add(QLabel(), 1)

    def connect_device(self, device):
        self.status.setText('Connected')
        device.signals.button_pressed.connect(self.button_pressed)
        device.signals.button_released.connect(self.button_released)

    def button_pressed(self, button):
        number = int(button) - 1
        self.buttons[number].press.run()
        self.buttons[number].state.setText('down')

    def button_released(self, button):
        number = int(button) - 1
        self.buttons[number].release.run()
        self.buttons[number].state.setText('up')
