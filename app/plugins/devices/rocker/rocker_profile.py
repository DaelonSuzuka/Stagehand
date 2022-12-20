from qtstrap import *
from codex import SerialDevice, JudiStandardMixin
import json


class Rocker(JudiStandardMixin, SerialDevice):
    profile_name = "Rocker"

    events = [
        'Channel 0 Changed',
        'Channel 1 Changed',
    ]
    
    class Signals(Adapter):
        event_received = Signal(str)
        value_changed = Signal(str, int)
        channel_0_changed = Signal(int)
        channel_1_changed = Signal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signals = self.Signals()

        self.value_0 = 0
        self.value_1 = 0

        self.message_tree.merge(self.common_message_tree)

    def receive(self, string):
        super().receive(string)
        msg = json.loads(string)
        update = msg.get('update', {})
        value_changed = update.get('value_changed', {})

        channel = value_changed.get('channel', '')
        value = value_changed.get('value', '')
        if channel and value:
            if channel == '0':
                self.value_0 = value
                self.signals.channel_0_changed.emit(value)
            if channel == '1':
                self.value_1 = value
                self.signals.channel_1_changed.emit(value)
            self.signals.event_received.emit(f'Channel {channel} Changed')