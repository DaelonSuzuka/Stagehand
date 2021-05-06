from qtstrap import *
from codex import DeviceManager, SerialDevice
import codex
import qtawesome as qta
from .app_updater import ApplicationUpdater
from .plugin_loader import Plugins


def get_application():
    app = QApplication.instance()

    install_ctrlc_handler(app)
    install_app_info(app)
    
    Plugins()

    # icon = QIcon(qta.icon('fa.circle','fa5s.video', options=[{'color':'gray'}, {'scale_factor':0.5, 'color':'white'}]))
    # app.setWindowIcon(icon)

    app.updater = ApplicationUpdater()
    app.updater.check_latest()

    app.device_manager = DeviceManager(app)
    app.aboutToQuit.connect(lambda: app.device_manager.close())

    return app