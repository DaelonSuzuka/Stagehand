from qtstrap import *
from main_window import MainWindow
from codex import DeviceManager
import qtawesome as qta
from appdirs import AppDirs
from pathlib import Path


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()
        
        # self.setQuitOnLastWindowClosed(False)
        # self.init_app_tray()

        icon = QIcon(qta.icon('fa.circle','fa5s.video', options=[{'color':'gray'}, {'scale_factor':0.5, 'color':'white'}]))
        self.setWindowIcon(icon)

        self.device_manager = DeviceManager(self)

    def closeEvent(self, event):
        self.device_manager.close()
        return super().closeEvent(event)

    def init_app_tray(self):
        tray = QSystemTrayIcon()
        tray_icon = QIcon(qta.icon('fa5s.video', color='white'))
        tray.setIcon(tray_icon)
        tray.setVisible(True)

        menu = QMenu()
        self.test = QAction('test', triggered=lambda: print('test'))
        menu.addAction(self.test)
        self.quit_action = QAction("Quit", triggered=self.quit)
        menu.addAction(self.quit_action)
        tray.setContextMenu(menu)
        self.tray = tray


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