from qtstrap import *
from codex import SerialDevice, JudiStandardMixin
from .stomp_4_widget import Stomp4Widget


class Signals(QObject):
    button_pressed = Signal(str)
    button_released = Signal(str)

    @property
    def message_tree(self):
        return {
            "update": {
                "button_pressed": self.button_pressed.emit,
                "button_released": self.button_released.emit
            }
        }


class Stomp4(JudiStandardMixin, SerialDevice):
    profile_name = "Stomp 4"
    widget = Stomp4Widget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signals = Signals()
        self.message_tree.merge(self.signals.message_tree)
        self.message_tree.merge(self.common_message_tree)