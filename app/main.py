from stagehand.application import Application
from stagehand.main_window import MainWindow
from qtstrap.extras import log_monitor


def main():
    log_monitor.install()
    
    app = Application()
    
    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    main()