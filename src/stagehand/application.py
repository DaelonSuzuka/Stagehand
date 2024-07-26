from qtstrap import *
from qtstrap.extras import log_monitor
from codex import DeviceManager
from .app_updater import ApplicationUpdater
from .plugin_loader import Plugins


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()

        log_monitor.exception_logger_name = 'stagehand.exceptions'
        log_monitor.install()

        Plugins()

        self.updater = ApplicationUpdater()
        # self.updater.check_latest()

        self.device_manager = DeviceManager(self)
        self.aboutToQuit.connect(self.device_manager.close)
