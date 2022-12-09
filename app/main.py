from stagehand.application import Application
from stagehand.main_window import MainWindow
from stagehand.plugin_loader import Plugins
from qtstrap.extras import log_monitor


def main():
    log_monitor.install()
    
    Plugins()
    
    app = Application()
    
    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    main()