from stagehand.application import Application
from stagehand.main_window import MainWindow

import PySide6.QtAsyncio as QtAsyncio


def main():
    Application()
    MainWindow()

    QtAsyncio.run(handle_sigint=True)


if __name__ == '__main__':
    main()
