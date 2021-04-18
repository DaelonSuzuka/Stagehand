from qtstrap import *
from codex import DeviceManager
from obs import ActionWidget


@DeviceManager.subscribe_to("judipedals")
class PedalActionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        default = {f'Pedal {i} Pressed': ActionWidget.default_data(f'Pedal {i} Pressed') for i in range(1, 5)}
        prev_presses = QSettings().value('pedal_actions/presses', default)
        self.press = [ActionWidget(data=data, changed=self.save_actions) for _, data in prev_presses.items()]

        default = {f'Pedal {i} Released': ActionWidget.default_data(f'Pedal {i} Released') for i in range(1, 5)}
        prev_releases = QSettings().value('pedal_actions/releases', default)
        self.release = [ActionWidget(data=data, changed=self.save_actions) for _, data in prev_releases.items()]

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

    def save_actions(self):
        data = {action.name: action.to_dict() for action in self.press}
        QSettings().setValue('pedal_actions/presses', data)

        data = {action.name: action.to_dict() for action in self.release}
        QSettings().setValue('pedal_actions/releases', data)