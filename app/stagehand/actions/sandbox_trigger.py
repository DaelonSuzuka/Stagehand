from qtstrap import *
from .items import TriggerItem


class SandboxTrigger(TriggerItem):
    name = 'sandbox'
    triggered = Signal()

    def __init__(self, changed, run, owner=None):
        super().__init__()

        self.owner = owner
        self.trigger = QLineEdit()
        self.trigger.textChanged.connect(changed)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.trigger)

    def reset(self):
        self.trigger.clear()

    def set_data(self, data: dict):
        if 'trigger' in data:
            self.trigger.setText(data['trigger'])

    def get_data(self):
        return {'trigger': self.trigger.text()}
