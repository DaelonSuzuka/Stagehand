from qtstrap import *
from .main_window import MainWindow
from codex import DeviceManager, SerialDevice
import codex
import qtawesome as qta
from appdirs import AppDirs
from pathlib import Path
from .app_updater import ApplicationUpdater
from .plugin_loader import Plugins


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()

        icon = QIcon(qta.icon('fa.circle','fa5s.video', options=[{'color':'gray'}, {'scale_factor':0.5, 'color':'white'}]))
        self.setWindowIcon(icon)

        self.updater = ApplicationUpdater()
        self.updater.check_latest()

        self.device_manager = DeviceManager(self)

    def closeEvent(self, event):
        self.device_manager.close()
        return super().closeEvent(event)


def run():
    # Create the Qt Application
    app = Application()

    # create window
    window = MainWindow()
    window.show()

    # Run the main Qt loop
    app.exec_()

if __name__ == "__main__":
    run()