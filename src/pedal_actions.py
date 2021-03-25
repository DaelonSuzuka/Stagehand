from qtstrap import *
from codex import DeviceManager
from obs import ActionWidget


@DeviceManager.subscribe_to("judipedals")
class PedalActionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.press = [ActionWidget(f'Pedal {i} Pressed') for i in range(1, 5)]
        self.release = [ActionWidget(f'Pedal {i} Released') for i in range(1, 5)]
        self.state = [QLabel('up') for i in range(1, 5)]

        self.status = QLabel("No Pedals Connected")
        
        with CVBoxLayout(self, align='top') as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Device Status:'))
                layout.add(self.status)

            layout.add(QLabel())
            layout.add(HLine())

            for i in range(4):
                with layout.hbox(align='left'):
                    layout.add(QLabel(f'Pedal {i+1} Status:'))
                    layout.add(self.state[i])
                layout.add(self.press[i])
                layout.add(self.release[i])

            layout.add(QLabel(), 1)

    def connected(self, device):
        self.status.setText('Pedals Connected')
        device.signals.button_pressed.connect(self.button_pressed)
        device.signals.button_released.connect(self.button_released)

    def button_pressed(self, button):
        number = int(button) - 1
        self.press[number].run()
        self.state[number].setText('down')

    def button_released(self, button):
        number = int(button) - 1
        self.release[number].run()
        self.state[number].setText('up')