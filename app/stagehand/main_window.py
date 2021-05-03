from qtstrap import *
from codex import DeviceControlsDockWidget
from .mic_voter import MicVoterWidget
from .sandbox import Sandbox
import qtawesome as qta
from .generic_actions import GenericActionsWidget
from .web_interface import WebInterfaceManager
from .about import AboutDialog
from .input_devices import InputDeviceManager
from .plugin_loader import Plugins


class FontSizeMenu(QMenu):
    def __init__(self, parent=None, default=12):
        super().__init__(parent=parent)
        self.setTitle('Font Size')

        self.default_size = default
        self.font_size = QSettings().value('font_size', self.default_size)
        self.set_font_size(self.font_size)

        self.addAction(QAction('+', self, triggered=lambda: self.set_font_size(self.font_size + 2)))
        self.addAction(QAction('-', self, triggered=lambda: self.set_font_size(self.font_size - 2)))
        self.addAction(QAction('Reset', self, triggered=lambda: self.set_font_size(self.default_size)))

    def set_font_size(self, size):
        set_font_options(self.parent(), {'setPointSize': int(size)})
        self.font_size = int(size)
        QSettings().setValue('font_size', size)


class MainWindow(BaseMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.force_close = False

        self.font_menu = FontSizeMenu(self)

        self.about = AboutDialog(self)
        self.device_controls = DeviceControlsDockWidget(self)
        
        self.obs = Plugins().obs_core.ObsManager(self)
        self.sandbox = Sandbox(self.obs, self)
        if not self.restoreDockWidget(self.sandbox.tools_dock):
            self.addDockWidget(self.sandbox.tools_dock.starting_area, self.sandbox.tools_dock)

        self.load_settings()

        self.voter = MicVoterWidget(self)
        self.actions = GenericActionsWidget(self)
        # self.web_actions = WebInterfaceManager(self)
        self.input_devices = InputDeviceManager(self)

        def scroll(widget):
            return widget
            scroll = QScrollArea(parent=self)
            scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setWidget(widget)
            return scroll

        tabs = {
            'OBS Manager': self.obs,
            'Mic Voter': scroll(self.voter),
            'Actions': scroll(self.actions),
            # 'Web Actions': scroll(self.web_actions),
            'Input Devices': scroll(self.input_devices),
        }

        self.tabs = PersistentTabWidget('main_tabs', tabs=tabs)
        self.setCentralWidget(self.tabs)

        self.tab_shortcuts = []
        for i in range(10):
            shortcut = QShortcut(f'Ctrl+{i + 1}', self, activated=lambda i=i: self.tabs.setCurrentIndex(i))
            self.tab_shortcuts.append(shortcut)

        self.init_tray_stuff()
        self.init_statusbar()

        qApp.updater.update_found.connect(self.display_update_available)

    def display_update_available(self):
        self.tray_icon.showMessage('An update is available.', 'an update is available')

    def init_statusbar(self):
        self.status = BaseToolbar(self, 'statusbar', location='bottom', size=30)
        self.status.setContextMenuPolicy(Qt.PreventContextMenu)
        
        self.status.addWidget(self.init_settings_btn())
        self.status.addSeparator()
        
        self.status.add_spacer()
        # self.status.addWidget(self.minimize_to_tray)
        self.status.addSeparator()
        self.status.addWidget(self.obs.status_widget)

    def init_settings_btn(self):
        settings_btn = QToolButton(self.status, icon=qta.icon('fa.gear', color='gray'))
        menu = QMenu(settings_btn)
        settings_btn.setMenu(menu)
        settings_btn.setPopupMode(QToolButton.InstantPopup)

        # settings popup menu
        menu.addSeparator()
        menu.addAction(self.sandbox.tools_dock.toggleViewAction())
        menu.addAction(self.device_controls.toggleViewAction())

        menu.addSeparator()
        menu.addMenu(self.font_menu)

        menu.addSeparator()
        menu.addAction(self.minimize_to_tray)

        menu.addSeparator()
        menu.addAction(qApp.updater.check_for_updates_action())
        menu.addAction(self.about.show_action())
        
        menu.addSeparator()
        menu.addAction(QAction('&Exit', menu, 
            shortcut='Ctrl+Q',
            statusTip='Exit application',
            triggered=self._close)
        )

        return settings_btn

    def _close(self):
        self.force_close = True
        self.close()

    def closeEvent(self, event):
        self.save_settings()

        if not self.force_close and self.minimize_to_tray.isChecked():
            event.ignore()
            self.hide()
        else:
            self.tray_icon.hide()
            super().closeEvent(event)

    def init_tray_stuff(self):
        self.tray_icon = QSystemTrayIcon(self)
        icon = QIcon(qta.icon('fa.circle','fa5s.video', options=[{'color':'gray'}, {'scale_factor':0.5, 'color':'white'}]))
        self.tray_icon.setIcon(icon)

        self.tray_menu = QMenu()
        self.tray_menu.addAction(QAction("Stagehand", self, enabled=False))
        self.tray_menu.addAction(QAction("Open", self, triggered=self.show))
        self.tray_menu.addAction(QAction("Quit", self, triggered=qApp.quit))
        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.show()

        self.minimize_to_tray = PersistentCheckableAction(
            'mainwindow/minimize_to_tray', 
            'Minimize to tray'
        )