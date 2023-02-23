from qtstrap import *
from codex import DeviceManager
from .app_updater import ApplicationUpdater
import qtawesome as qta


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()

        default_style = 'Light'
        self.current_style: str = QSettings().value('style', default_style)
        self.update_style(self.current_style)
        
        self.updater = ApplicationUpdater()
        # self.updater.check_latest()

        self.device_manager = DeviceManager(self)
        self.aboutToQuit.connect(self.device_manager.close)

    def update_style(self, text: str):
        self.current_style = text
        QSettings().setValue('style', self.current_style)

        if text == qta.styles.DEFAULT_DARK_PALETTE:
            qta.reset_cache()
            qta.dark(self)
        else:
            qta.reset_cache()
            qta.light(self)
