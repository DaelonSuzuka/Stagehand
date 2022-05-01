from qtstrap import *


class SidebarButton(QPushButton):
    def __init__(self, *args, target=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setIconSize(QSize(40, 40))
        self.setFlat(True)
        self.target = target
        self.clicked.connect(self.on_click)

    def on_click(self):
        self.parent().parent().set_widget(self.target)
        self.setEnabled(False)


class StagehandWidget(QWidget):
    ...


class StagehandStatusBarItem(QWidget):
    ...