from stagehand.application import Application
from stagehand.main_window import MainWindow

import asyncio
import functools
import sys

import aiohttp


from qtstrap import *

import qasync
from qasync import asyncSlot, asyncClose, QEventLoop
from codex import DeviceManager, SerialDevice
import codex
import qtawesome as qta
from appdirs import AppDirs
from pathlib import Path
from stagehand.app_updater import ApplicationUpdater
from stagehand.plugin_loader import Plugins
import app_info as info
import signal


class Application(BaseApplication):
    def __init__(self) -> None:
        super().__init__()

        icon = QIcon(qta.icon('fa.circle','fa5s.video', options=[{'color':'gray'}, {'scale_factor':0.5, 'color':'white'}]))
        self.setWindowIcon(icon)

        self.updater = ApplicationUpdater()
        # self.updater.check_latest()

        self.device_manager = DeviceManager(self)

        self.window = MainWindow()
        self.window.show()

    def closeEvent(self, event):
        self.device_manager.close()
        return super().closeEvent(event)


def install_ctrlc_handler(app):
    def ctrlc_handler(sig=None, frame=None):
        app.closeAllWindows() # this makes sure the MainWindow's .close() method gets called
        app.quit()
       
    # grab the keyboard interrupt signal 
    signal.signal(signal.SIGINT, ctrlc_handler)

    # empty timer callback
    def update():
        pass
    
    # create timer to force python interpreter to get some runtime
    app._timer = QTimer()
    app._timer.timeout.connect(update)
    app._timer.start(10)


def install_app_info(app):
    if info.AppPublisher:
        app.setOrganizationName(info.AppPublisher)
    if info.AppPublisher:
        app.setOrganizationDomain(info.AppPublisher)
    if info.AppName:
        app.setApplicationName(info.AppName)
    if info.AppVersion:
        app.setApplicationVersion(info.AppVersion)


async def main():

    
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel("Close Application")

    loop = asyncio.get_event_loop()
    future = asyncio.Future()


    app = QApplication.instance()
    install_ctrlc_handler(app)
    install_app_info(app)

    icon = QIcon(qta.icon('fa.circle','fa5s.video', options=[{'color':'gray'}, {'scale_factor':0.5, 'color':'white'}]))
    app.setWindowIcon(icon)

    app.updater = ApplicationUpdater()
    app.device_manager = DeviceManager(app)

    
    if hasattr(app, 'aboutToQuit'):
        getattr(app, 'aboutToQuit').connect(functools.partial(close_future, future, loop))


    window = MainWindow()
    window.show()

    await future

    return True


if __name__ == "__main__":
    
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)