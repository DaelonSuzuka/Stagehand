from qtstrap import *
from stagehand.actions import TriggerItem
from qtpy.shiboken import isValid


@singleton
class StartupRegistry(QObject):
    def register(self, trigger: TriggerItem, time: int):
        call_later(lambda: self.trigger(trigger), time)

    def trigger(self, trigger):
        if isValid(trigger):
            trigger.triggered.emit()


class StartupTrigger(QWidget, TriggerItem):
    name = 'startup'
    triggered = Signal()

    def __init__(self, changed, run, owner=None):
        super().__init__()

        self.changed = changed
        self.owner = owner
        self.triggered.connect(run)
        
        self.delay = QLineEdit()
        self.delay.setText('1000')
        self.delay.setValidator(QIntValidator())
        self.delay.textChanged.connect(changed)
        
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(QLabel('Delay:'))
            layout.add(self.delay)
            layout.add(QLabel('ms'), 1)

    def reset(self):
        pass
        
    def set_data(self, data: dict):
        time = data.get('delay', '1000')
        self.delay.setText(time)
        StartupRegistry().register(self, int(time))

    def get_data(self):
        return {
            'delay': self.delay.text()
        }
