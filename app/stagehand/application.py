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

        self.window = MainWindow()
        self.window.show()

    def closeEvent(self, event):
        self.device_manager.close()
        return super().closeEvent(event)