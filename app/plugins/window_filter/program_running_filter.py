from qtstrap import *
from stagehand.actions import FilterStackItem
from .packages import psutil


def get_process_names():
    names = set()

    for proc in psutil.process_iter(attrs=None, ad_value=None):
        names.add(proc.name())

    return sorted(names)


class ProgramRunningFilter(QWidget, FilterStackItem):
    name = 'program running'

    def __init__(self, changed, parent=None) -> None:
        super().__init__(parent=parent)

        self.process = QComboBox()
        self.process.addItems(get_process_names())
        self.process.currentIndexChanged.connect(changed)

        self.refresh()

        self.refresh_btn = QPushButton(clicked=self.refresh)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.process, 1)
            layout.add(self.refresh_btn)

    def refresh(self):
        with SignalBlocker(self.process):
            selection = self.process.currentText()
            self.process.clear()
            names = get_process_names()
            if selection not in names:
                names.insert(0, selection)
            self.process.addItems(get_process_names())
            self.process.setCurrentText(selection)

    def check(self) -> bool:
        return self.process.currentText() in get_process_names()
    
    def from_dict(self, data: dict) -> None:
        self.process.setCurrentText(data['type'])

    def to_dict(self) -> dict:
        return {
            'type': self.process.currentText(),
        }
