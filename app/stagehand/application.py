from qtstrap import *
from codex import DeviceManager, SerialDevice
import codex
import qtawesome as qta
from .app_updater import ApplicationUpdater
from .plugin_loader import Plugins


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()
        
        Plugins()

        self.updater = ApplicationUpdater()
        # self.updater.check_latest()

        self.device_manager = DeviceManager(self)
        self.aboutToQuit.connect(self.device_manager.close)