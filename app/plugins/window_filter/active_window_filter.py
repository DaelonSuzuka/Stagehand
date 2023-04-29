from qtstrap import *
from stagehand.actions import FilterStackItem
from .windows import getAllWindowTitles, getForegroundWindowTitle


class ActiveWindowFilter(FilterStackItem):
    name = 'active window'

    def __init__(self, changed, owner=None) -> None:
        super().__init__()

        self.owner = owner
        self.window = QComboBox()
        self.window.currentIndexChanged.connect(changed)

        self.refresh()

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.window)

    def refresh(self):
        with SignalBlocker(self.window):
            selection = self.window.currentText()
            self.window.clear()
            self.window.addItems(getAllWindowTitles())
            self.window.setCurrentText(selection)

    def check(self) -> bool:
        return self.window.currentText() == getForegroundWindowTitle()
    
    def set_data(self, data: dict) -> None:
        if 'window' in data:
            self.window.setCurrentText(data['window'])

    def get_data(self) -> dict:
        return {
            'window': self.window.currentText(),
        }
