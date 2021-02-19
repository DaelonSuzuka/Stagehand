from devices import SerialDevice, JudiStandardMixin
from qt import *


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


class JudiPedals(JudiStandardMixin, SerialDevice):
    profile_name = "judipedals"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signals = Signals()
        self.message_tree.merge(self.signals.message_tree)
        self.message_tree.merge(self.common_message_tree)