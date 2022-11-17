from qtstrap import *
from stagehand.actions import TriggerItem
from .events import events
from .event_widgets import widgets
from .obs_socket import ObsSocket


class ObsTrigger(QWidget, TriggerItem):
    name = 'obs'
    triggered = Signal()

    def __init__(self, changed, run, owner=None):
        super().__init__()

        self.owner = owner
        self.changed = changed
        self.triggered.connect(run)

        self.event_widget = None

        ObsSocket().event_recieved.connect(self.event_recieved)

        self.type = QComboBox()
        self.type.addItems(events.keys())
        
        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.change_type)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.type)

    def event_recieved(self, event):
        if self.event_widget and self.event_widget.validate_event(event):
            self.triggered.emit()

    def change_type(self, *_):
        if self.event_widget:
            self.layout().removeWidget(self.event_widget)
            self.event_widget.deleteLater()
            
        self.event_widget = widgets[self.type.currentText()](self.changed)
        self.layout().add(self.event_widget, 1)

    def set_data(self, data):
        try:
            self.type.setCurrentText(data['type'])
            # self.value.setText(data['value'])
        except:
            pass

    def get_data(self):
        return {
            'type': self.type.currentText(),
            # 'value': self.value.text(),
        }
