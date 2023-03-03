from qtstrap import *
from qtstrap.extras.style import apply_theme
from codex import DeviceManager
from .app_updater import ApplicationUpdater
import qtawesome as qta
from qtstrap.extras.command_palette import CommandPalette


class Application(BaseApplication):
    theme_changed = Signal()

    def __init__(self) -> None:
        super().__init__()

        default_theme = 'light'
        theme = QSettings().value('theme', default_theme)
        self.update_theme(theme)
        
        self.updater = ApplicationUpdater()
        # self.updater.check_latest()

        self.device_manager = DeviceManager(self)
        self.aboutToQuit.connect(self.device_manager.close)

    def update_theme(self, theme: str, force=False):
        if theme == OPTIONS.theme:
            return

        OPTIONS.theme = theme
        QSettings().setValue('theme', theme)

        qta.reset_cache()
        apply_theme(theme, self)

        self.theme_changed.emit()
