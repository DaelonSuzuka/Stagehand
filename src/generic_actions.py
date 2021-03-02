from qt import *
from obs import ActionWidget


class GenericActionsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        with CVBoxLayout(self) as layout:
            for i in range(1, 13):
                layout.add(ActionWidget(f'Action {i}'))
            layout.add(QLabel(), 1)