from qtstrap import *
from codex import SerialDevice, JudiStandardMixin


class Rocker(JudiStandardMixin, SerialDevice):
    profile_name = "Rocker"
    
    class Signals(Adapter):
        button_pressed = Signal(str)
        button_released = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signals = self.Signals()

        self.message_tree.merge(self.common_message_tree)
        self.message_tree['update']['button_pressed'] = self.signals.button_pressed.emit
        self.message_tree['update']['button_released'] = self.signals.button_released.emit