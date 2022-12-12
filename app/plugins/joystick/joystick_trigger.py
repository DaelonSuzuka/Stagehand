from qtstrap import *
from stagehand.actions import TriggerItem
from ._utils import get_joysticks, get_joystick_names, get_joystick_sources


button_name_map = {
    'xbox': {
        'axes': {
            0: 'Left X-axis',
            1: 'Left Y-axis',
            2: 'Right X-axis',
            3: 'Right Y-axis',
            4: 'Left Trigger',
            5: 'Right Trigger',
        },
        'buttons': {
            0: 'A Button',
            1: 'B Button',
            2: 'X Button',
            3: 'Y Button',
            4: 'Left Bumper',
            5: 'Right Bumper',
            6: 'Back Button',
            7: 'Start Button',
            8: 'Left Stick',
            9: 'Right Stick',
        },
        'hats': {
            (0, 1): 'D-Pad N',
            (0, -1): 'D-Pad S',
            (-1, 0): 'D-Pad W',
            (1, 0): 'D-Pad E',
            (1, 1): 'D-Pad NE',
            (1, -1): 'D-Pad SE',
            (-1, 1): 'D-Pad NW',
            (-1, -1): 'D-Pad SW',
        }
    }
}


class JoystickScanner(QObject):
    class Signals(Adapter):
        event = Signal(str, int, object)

    def __init__(self, joystick):
        super().__init__()
        self.signals = self.Signals()

        joystick.init()
        self.joystick = joystick

        self.state = {}
        self.prev_state = {}

    def event(self, cb):
        self.signals.event.connect(cb)

    def scan(self):
        if self.joystick is None:
            return

        self.prev_state = dict.copy(self.state)
        new_state = {}

        for i in range(self.joystick.get_numaxes()):
            new_state[f'axis:{i}'] = self.joystick.get_axis(i)

        for i in range(self.joystick.get_numbuttons()):
            new_state[f'button:{i}'] = self.joystick.get_button(i)

        for i in range(self.joystick.get_numhats()):
            new_state[f'hat:{i}'] = self.joystick.get_hat(i)

        self.state = new_state

        if not self.prev_state:
            return

        for n in new_state:
            if new_state[n] != self.prev_state[n]:
                parts = n.split(':')
                self.signals.event.emit(parts[0], int(parts[1]), new_state[n])


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

    def __init__(self, changed, run, owner=None):
        super().__init__()

        self.owner = owner
        self.changed.connect(changed)
        self.triggered.connect(run)

        self.listener = JoystickListener()

        self.adapter = None

        self.prev_joystick = ''
        self.joystick = QComboBox()
        self.joystick.currentIndexChanged.connect(self.refresh)

        self.source = QComboBox()
        self.source.setMinimumWidth(100)
        self.source.currentIndexChanged.connect(self.refresh)

        self.selected_button = None

        self.refresh()

        with CHBoxLayout(self, margins=0) as layout:
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

            if sources := get_joystick_sources(self.joystick.currentText()):
                for s in sources['buttons']:
                    s = button_name_map['xbox']['buttons'].get(s, None)
                    if s:
                        self.source.addItem(s)
                for _, direction in button_name_map['xbox']['hats'].items():
                    self.source.addItem(direction)
            self.source.setCurrentText(selection)

        if self.joystick.currentText() != self.prev_joystick:
            self.listener.get_joystick(self.joystick.currentText()).event(self.on_event)

        self.prev_joystick = self.joystick.currentText()

        self.changed.emit()

    def on_event(self, name, idx, value):
        if name == 'axis':
            axis = button_name_map['xbox']['axes'].get(idx, None)
            return
        if name == 'button':
            button = button_name_map['xbox']['buttons'].get(idx, None)
            if button and (button == self.source.currentText()) and value == True:
                self.triggered.emit()
        if name == 'hat':
            hat = button_name_map['xbox']['hats'].get(value, None)
            if hat and (hat == self.source.currentText()):
                self.triggered.emit()

    def set_data(self, data):
        try:
            self.joystick.setCurrentText(data['joystick'])
            self.source.setCurrentText(data['source'])
            
            self.refresh()
        except:
            pass

    def get_data(self):
        return {
            'joystick': self.joystick.currentText(),
            'source': self.source.currentText(),
        }