from qtstrap import *
from codex import SerialDevice, JudiStandardMixin
from .stomp_4_widget import Stomp4Widget


class Stomp4(JudiStandardMixin, SerialDevice):
    profile_name = "Stomp 4"
    widget = Stomp4Widget
    
    class Signals(Adapter):
        button_pressed = Signal(str)
        button_released = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signals = self.Signals()

        self.message_tree.merge(self.common_message_tree)
        self.message_tree['update']['button_pressed'] = self.signals.button_pressed.emit
        self.message_tree['update']['button_released'] = self.signals.button_released.emit