from stagehand.application import Application
from stagehand.main_window import MainWindow


def main():
    app = Application()

    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == '__main__':
    main()
