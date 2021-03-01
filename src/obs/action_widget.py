from qt import *
from obs import Sandbox


class ActionWidget(QWidget):
    renamed = Signal(str)

    def __init__(self, name, changed=None, parent=None):
        super().__init__(parent=parent)

        self.name = name
        label = QSettings().value(f'{name}_label', name)
        self.label = LabelEdit(label, changed=self.on_rename)
        self.action = PersistentLineEdit(f'{name}_action')
        self.run_btn = QPushButton('Run', clicked=self.run)

        if changed:
            self.renamed.connect(changed)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.label)
            layout.add(self.action, 1)
            layout.add(self.run_btn)

    def contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction(QAction('Reset', self, triggered=self.reset))
        menu.exec_(event.globalPos())

    def reset(self):
        self.label.setText(self.name)
        self.action.clear()
        QSettings().setValue(f'{self.name}_label', self.name)

    def run(self):
        Sandbox().run(self.action.text())

    def on_rename(self, new_name):
        QSettings().setValue(f'{self.name}_label', new_name)
        self.renamed.emit(new_name)