from stagehand.application import Application
from stagehand.main_window import MainWindow

import PySide6.QtAsyncio as QtAsyncio


def main():
    Application()
    MainWindow()

    # qtstrap's BaseApplication owns SIGINT/SIGTERM; handle_sigint=True would
    # clobber its handler with SIG_DFL (immediate, non-graceful death)
    QtAsyncio.run(handle_sigint=False)


if __name__ == '__main__':
    main()
