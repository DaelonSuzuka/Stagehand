from qt import *
from devices import DeviceManager


@DeviceManager.subscribe_to("judipedals")
class JudiPedalsControls(QWidget):
    pedal_pressed = Signal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.one = QPushButton(checkable=True)
        self.two = QPushButton(checkable=True)
        self.three = QPushButton(checkable=True)
        self.four = QPushButton(checkable=True)
        
        with CHBoxLayout(self) as layout:
            with layout.vbox(align='top') as layout:
                layout.add(QLabel('1'))
                layout.add(self.one)
            with layout.vbox(align='top') as layout:
                layout.add(QLabel('2'))
                layout.add(self.two)
            with layout.vbox(align='top') as layout:
                layout.add(QLabel('3'))
                layout.add(self.three)
            with layout.vbox(align='top') as layout:
                layout.add(QLabel('4'))
                layout.add(self.four)

    def connected(self, device):
        device.signals.button_pressed.connect(self.button_pressed)
        device.signals.button_released.connect(self.button_released)

    def button_pressed(self, button):
        if button == '1':
            self.one.setChecked(True)
            self.pedal_pressed.emit(1)
        if button == '2':
            self.two.setChecked(True)
            self.pedal_pressed.emit(2)
        if button == '3':
            self.three.setChecked(True)
            self.pedal_pressed.emit(3)
        if button == '4':
            self.four.setChecked(True)
            self.pedal_pressed.emit(4)

    def button_released(self, button):
        if button == '1':
            self.one.setChecked(False)
        if button == '2':
            self.two.setChecked(False)
        if button == '3':
            self.three.setChecked(False)
        if button == '4':
            self.four.setChecked(False)