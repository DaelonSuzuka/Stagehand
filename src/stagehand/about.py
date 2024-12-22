from qtstrap import *
import qtawesome as qta
import sys
import qtpy


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('About Stagehand')

        with CVBoxLayout(self) as layout:
            with layout.vbox() as layout:
                # layout.add(QLabel(f'Stagehand: v{app_info.AppInfo.VERSION}'))
                layout.add(QLabel())

                layout.add(QLabel('Built with:'))
                layout.add(QLabel(f'Python: {sys.version}'))
                layout.add(QLabel(f'Qt: {qtpy.QT_VERSION}'))
                layout.add(QLabel(f'QtPy: {qtpy.__version__}'))
                if qtpy.PYQT5 or qtpy.PYQT6:
                    layout.add(QLabel(f'{qtpy.API_NAME}: {qtpy.PYQT_VERSION}'))
                elif qtpy.PYSIDE2 or qtpy.PYSIDE6:
                    layout.add(QLabel(f'{qtpy.API_NAME}: {qtpy.PYSIDE_VERSION}'))
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
