from qtstrap import *
from codex import DeviceManager
from .app_updater import ApplicationUpdater
import qtawesome as qta


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()

        default_theme = 'Light'
        self.current_theme: str = QSettings().value('theme', default_theme)
        self.update_theme(self.current_theme)
        
        self.updater = ApplicationUpdater()
        # self.updater.check_latest()

        self.device_manager = DeviceManager(self)
        self.aboutToQuit.connect(self.device_manager.close)

    def update_theme(self, theme: str):
        self.current_theme = theme
        OPTIONS.theme = theme.lower()
        QSettings().setValue('theme', self.current_theme)

        if theme == qta.styles.DEFAULT_DARK_PALETTE:
            qta.reset_cache()
            qta.dark(self)
        else:
            qta.reset_cache()
            qta.light(self)
