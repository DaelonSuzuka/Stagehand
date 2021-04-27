from qtstrap import *
import qtawesome as qta


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with CVBoxLayout(self) as layout:
            with layout.vbox() as layout:
                layout.add(QLabel('Version: xx.xx.xx'))
                layout.add(QLabel())

                layout.add(QLabel('Built with:'))
                layout.add(QLabel('Python: 3.8+'))
                layout.add(QLabel('PySide2: 5.15.2'))
                layout.add(QLabel())

                layout.add(QLabel('Designed for:'))
                layout.add(QLabel('OBS Studio: 26.1.1'))
                layout.add(QLabel('obs-websocket: 4.9.0'))
                
            layout.add(QLabel(), 1)
            with layout.hbox() as layout:
                layout.add(QLabel(), 1)
                layout.add(QPushButton('Ok', clicked=self.accept))

    def _open(self):
        self.center_on_parent()
        self.open()

    def center_on_parent(self):
        r = self.parent().frameGeometry()
        rect = QRect(r.x() - (self.width() / 2), r.y(), r.width(), r.height() - (self.height() / 2))
        self.move(rect.center())

    def show_action(self):
        action = QAction('About', parent=self)
        action.triggered.connect(self._open)
        return action