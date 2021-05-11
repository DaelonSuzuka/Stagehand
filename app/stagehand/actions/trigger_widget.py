from qtstrap import *
import abc


class TriggerStackItem:
    @abc.abstractmethod
    def __init__(self, changed) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def from_dict(self, data: dict):
        raise NotImplementedError

    @abc.abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    @abc.abstractmethod
    def reset(self):
        pass


class SandboxTriggerWidget(QWidget, TriggerStackItem):
    def __init__(self, changed, parent=None):
        super().__init__(parent=parent)

        self.trigger = QLineEdit()
        self.trigger.textChanged.connect(changed)
        
        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.trigger)

    def from_dict(self, data: dict):
        try:
            self.trigger.setText(data['trigger'])
        except:
            pass

    def to_dict(self):
        return {
            'trigger': self.trigger.text()
        }


class TriggerStack(QWidget):
    changed = Signal()

    triggers = {
        'sandbox': SandboxTriggerWidget,
    }

    def __init__(self, changed, trigger_type='sandbox', trigger='', parent=None):
        super().__init__(parent=parent)

        self.type = QComboBox()
        self.stack = QStackedWidget()

        for name, trigger in self.triggers.items():
            self.type.addItem(name)
            self.stack.addWidget(trigger(changed))

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.stack.setCurrentIndex)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.stack)

    def set_data(self, data):
        if data:
            if 'trigger_type' not in data:
                data['trigger_type'] = 'sandbox'

            self.type.setCurrentText(data['trigger_type'])
            self.stack.currentWidget().from_dict(data)

    def to_dict(self):
        return {
            'trigger_type': self.type.currentText(),
            **self.stack.currentWidget().to_dict(),
        }