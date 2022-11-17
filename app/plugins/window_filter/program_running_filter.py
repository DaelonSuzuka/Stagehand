from qtstrap import *
from stagehand.actions import FilterStackItem
import subprocess


last_update = TimeStamp()
prev_names = set()


# this function uses a timestamp based cache to get around the fact that checking all processes
# is EXTREMELY slow using psutil (1.2+ seconds!) and fairly slow using tasklist(.5 seconds)
def get_process_names():
    global prev_names
    names = set()

    if prev_names and last_update.time_since() < 10:
        return prev_names

    s = subprocess.check_output('tasklist /nh', shell=True).decode()
    for line in s.split('\n'):
        names.add(line.split(' ')[0])

    prev_names = sorted(names)
    return prev_names


class ProgramRunningFilter(QWidget, FilterStackItem):
    name = 'program running'

    def __init__(self, changed, owner=None) -> None:
        super().__init__()

        self.owner = owner
        self.process = QComboBox()
        self.process.addItems(get_process_names())
        self.process.currentIndexChanged.connect(changed)

        self.refresh()

        self.refresh_btn = QPushButton(clicked=self.refresh)

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.process, 1)
            layout.add(self.refresh_btn)

    def refresh(self):
        with SignalBlocker(self.process):
            selection = self.process.currentText()
            self.process.clear()
            names = get_process_names()
            if selection not in names:
                names.insert(0, selection)
            self.process.addItems(names)
            self.process.setCurrentText(selection)

    def check(self) -> bool:
        return self.process.currentText() in get_process_names()
    
    def set_data(self, data: dict) -> None:
        self.process.setCurrentText(data['type'])

    def get_data(self) -> dict:
        return {
            'type': self.process.currentText(),
        }
