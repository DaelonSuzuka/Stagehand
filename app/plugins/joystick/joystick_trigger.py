from qtstrap import *
from stagehand.actions import TriggerItem
from ._utils import get_joysticks, get_joystick_names, get_joystick_sources


class JoystickScanner(QObject):
    class Signals(Adapter):
        button = Signal(int, bool) # btn number, state
        axis = Signal(int, float) # axis number, value

    def __init__(self, joystick):
        super().__init__()
        self.signals = self.Signals()

        joystick.init()
        self.joystick = joystick

        # self.signals.button.connect(print)

        self.state = {}
        self.prev_state = {}

    def button(self, cb):
        self.signals.button.connect(cb)

    def axis(self, cb):
        self.signals.axis.connect(cb)

    def scan(self):
        self.prev_state = dict.copy(self.state)
        new_state = {}

        for i in range(self.joystick.get_numaxes()):
            new_state[f'axis {i}'] = self.joystick.get_axis(i)

        for i in range(self.joystick.get_numbuttons()):
            new_state[f'button {i}'] = self.joystick.get_button(i)

        self.state = new_state

        if self.prev_state:
            for n in new_state:
                if new_state[n] != self.prev_state[n]:
                    if n.startswith('axis'):
                        self.signals.axis.emit(int(n[len('axis '):]), new_state[n])
                    if n.startswith('button'):
                        self.signals.button.emit(int(n[len('button '):]), new_state[n])

@singleton
class JoystickListener(QObject):
    def __init__(self):
        super().__init__()

        self.joysticks = {}

        for name, js in get_joysticks().items():
            self.joysticks[name] = JoystickScanner(js)

        self.timer = QTimer()
        self.timer.timeout.connect(self.scan_joysticks)
        self.timer.start(20)

    def scan_joysticks(self):
        for name, js in self.joysticks.items():
            js.scan()

    def get_joystick(self, name):
        if name in self.joysticks:
            return self.joysticks[name]


class JoystickTrigger(QWidget, TriggerItem):
    name = 'joystick'
    triggered = Signal()
    changed = Signal()

    def __init__(self, changed, run):
        super().__init__()

        self.changed.connect(changed)

        self.listener = JoystickListener()

        self.adapter = None

        self.prev_joystick = ''
        self.joystick = QComboBox()
        self.joystick.currentIndexChanged.connect(self.refresh)

        self.source = QComboBox()
        self.source.currentIndexChanged.connect(self.refresh)

        self.refresh()

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.joystick)
            layout.add(self.source)

    def refresh(self):
        with SignalBlocker(self.joystick):
            selection = self.joystick.currentText()
            self.joystick.clear()
            self.joystick.addItems(get_joystick_names())
            self.joystick.setCurrentText(selection)

        with SignalBlocker(self.source):
            selection = self.source.currentText()
            self.source.clear()
            self.source.addItems(get_joystick_sources(self.joystick.currentText()))
            self.source.setCurrentText(selection)

        if self.joystick.currentText() != self.prev_joystick:
            self.listener.get_joystick(self.joystick.currentText()).axis(self.on_axis)
            self.listener.get_joystick(self.joystick.currentText()).button(self.on_button)

        self.prev_joystick = self.joystick.currentText()

        self.changed.emit()
        
    @Slot(int, float)
    def on_axis(self, axis, value):
        # print(f'axis {axis}:', value)
        pass

    @Slot(int, bool)
    def on_button(self, button, state):
        print(f'button {button}', state)
        if f'button {button}' == self.source.currentText():
            self.triggered.emit()

    def from_dict(self, data):
        try:
            self.joystick.setCurrentText(data['joystick'])
            self.source.setCurrentText(data['source'])
            
            self.refresh()
        except:
            pass

    def to_dict(self):
        return {
            'joystick': self.joystick.currentText(),
            'source': self.source.currentText(),
        }