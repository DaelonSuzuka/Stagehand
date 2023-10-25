from qtstrap import *
from codex import SerialDevice, JudiStandardMixin


class Stomp4(JudiStandardMixin, SerialDevice):
    profile_name = 'Stomp 4'

    events = [
        '1 Down',
        '1 Up',
        '2 Down',
        '2 Up',
        '3 Down',
        '3 Up',
        '4 Down',
        '4 Up',
    ]

    class Signals(Adapter):
        event_received = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signals = self.Signals()

        self.message_tree.merge(self.common_message_tree)
        self.message_tree['update']['button_pressed'] = lambda b: self.signals.event_received.emit(f'{b} Down')
        self.message_tree['update']['button_released'] = lambda b: self.signals.event_received.emit(f'{b} Up')
