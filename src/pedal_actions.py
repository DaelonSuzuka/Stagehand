from qt import *
from devices import DeviceManager
import json
from obs import Sandbox, ActionWidget


class PedalActions(QWidget):
    def __init__(self, name, parent=None):
        super().__init__(parent=parent)
        self.name = QLabel(name)
        self.status = QLabel('up')
        self.pressed_action = PersistentLineEdit(f'{name}_pressed')
        self.released_action = PersistentLineEdit(f'{name}_released')
        self.run_pressed = QPushButton('Run', clicked=self.pressed)
        self.run_released = QPushButton('Run', clicked=self.released)

        with CVBoxLayout(self) as layout:
            with layout.hbox(align='left'):
                layout.add(QLabel('Pedal:'))
                layout.add(self.name)
                layout.add(QLabel(), 1)
                layout.add(QLabel('Status:'))
                layout.add(self.status)
                
            with layout.hbox():
                with layout.vbox():
                    layout.add(QLabel('Pressed:'))
                    layout.add(QLabel('Released:'))
                with layout.vbox():
                    layout.add(self.pressed_action)
                    layout.add(self.released_action)
                with layout.vbox():
                    layout.add(self.run_pressed)
                    layout.add(self.run_released)

    def pressed(self):
        self.status.setText('down')
        Sandbox().run(self.pressed_action.text())

    def released(self):
        self.status.setText('up')
        Sandbox().run(self.released_action.text())


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
        number = int(button)
        self.press[number].run()
        self.state[number].setText('down')

    def button_released(self, button):
        number = int(button)
        self.release[number].run()
        self.state[number].setText('up')