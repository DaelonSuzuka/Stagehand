from qtstrap import *
from codex import DeviceManager
from .app_updater import ApplicationUpdater


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()
        
        self.updater = ApplicationUpdater()
        # self.updater.check_latest()

        self.device_manager = DeviceManager(self)
        self.aboutToQuit.connect(self.device_manager.close)