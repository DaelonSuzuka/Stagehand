
from qt import *
from main_window import MainWindow
from devices import DeviceManager


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()

        self.init_app_info()

        self.device_manager = DeviceManager(self)

        # create window
        self.window = MainWindow()
        self.window.show()

    def init_app_info(self):
        self.setOrganizationName("DaelonCo")
        self.setOrganizationDomain("DaelonCo")
        self.setApplicationName("Stagehand")
        self.setApplicationVersion("v0.1")


def run():    
    # Create the Qt Application
    app = Application()

    # Run the main Qt loop
    app.exec_()

if __name__ == "__main__":
    run()