from qtstrap import *
from codex import DeviceControlsDockWidget
from pedal_actions import PedalActionsWidget
from mic_voter import MicVoterWidget
from obs import ObsManager, Sandbox
import qtawesome as qta
from generic_actions import GenericActionsWidget
from web_interface import WebInterfaceManager
from about import AboutDialog


class MainWindow(BaseMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        set_font_options(self, {'setPointSize': 12})

        self.about = AboutDialog(self)
        self.device_controls = DeviceControlsDockWidget(self)
        
        self.obs = ObsManager(self)
        self.sandbox = Sandbox(self.obs, self)
        if not self.restoreDockWidget(self.sandbox.editor_dock):
            self.addDockWidget(self.sandbox.editor_dock.starting_area, self.sandbox.editor_dock)
        if not self.restoreDockWidget(self.sandbox.tools_dock):
            self.addDockWidget(self.sandbox.tools_dock.starting_area, self.sandbox.tools_dock)

        # self.load_settings()
        self.pedals = PedalActionsWidget(self)        
        self.voter = MicVoterWidget(self)
        self.actions = GenericActionsWidget(self)
        self.web_actions = WebInterfaceManager(self)

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
            'Web Actions': scroll(self.web_actions),
            'Pedal Actions': scroll(self.pedals),
        }

        self.tabs = PersistentTabWidget('main_tabs', tabs=tabs)
        self.setCentralWidget(self.tabs)

        self.tab_shortcuts = []
        for i in range(10):
            shortcut = QShortcut(f'Ctrl+{i + 1}', self, activated=lambda i=i: self.tabs.setCurrentIndex(i))
            self.tab_shortcuts.append(shortcut)

        self.init_tray_stuff()
        self.init_statusbar()

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
        menu.addAction(self.sandbox.editor_dock.toggleViewAction())
        menu.addAction(self.device_controls.toggleViewAction())

        menu.addSeparator()
        menu.addAction(self.about.show_action())

        menu.addSeparator()
        menu.addAction(self.minimize_to_tray)
        
        menu.addSeparator()
        menu.addAction(QAction('&Exit', menu, 
            shortcut='Ctrl+Q', 
            statusTip='Exit application',
            triggered=qApp.quit)
        )

        return settings_btn

    def closeEvent(self, event):
        if self.minimize_to_tray.isChecked():
            event.ignore()
            self.hide()
        else:
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