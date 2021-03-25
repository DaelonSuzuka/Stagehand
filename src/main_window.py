from qtstrap import *
from codex import DeviceControlsDockWidget
from pedal_actions import PedalActionsWidget
from mic_voter import MicVoterWidget
from obs import ObsManager, Sandbox
import qtawesome as qta
from generic_actions import GenericActionsWidget
from web_interface import WebInterfaceManager


class MainWindow(BaseMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("MainWindow")

        set_font_options(self, {'setPointSize': 12})

        self.device_controls = DeviceControlsDockWidget(self)
        
        self.obs = ObsManager(self)
        self.sandbox = Sandbox(self.obs, self)
        if not self.restoreDockWidget(self.sandbox.editor_dock):
            self.addDockWidget(self.sandbox.editor_dock.starting_area, self.sandbox.editor_dock)
        if not self.restoreDockWidget(self.sandbox.tools_dock):
            self.addDockWidget(self.sandbox.tools_dock.starting_area, self.sandbox.tools_dock)

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

        self.init_statusbar()

    def init_statusbar(self):
        self.status = BaseToolbar(self, 'statusbar', location='bottom', size=30)
        self.status.setContextMenuPolicy(Qt.PreventContextMenu)

        # settings button
        settings_btn = QToolButton(self.status, icon=qta.icon('fa.gear', color='gray'))
        menu = QMenu(settings_btn)
        settings_btn.setMenu(menu)
        settings_btn.setPopupMode(QToolButton.InstantPopup)
        self.status.addWidget(settings_btn)
        self.status.addSeparator()
        
        # settings popup menu
        menu.addSeparator()
        menu.addAction(self.sandbox.tools_dock.toggleViewAction())
        menu.addAction(self.sandbox.editor_dock.toggleViewAction())
        menu.addAction(self.device_controls.toggleViewAction())

        menu.addSeparator()
            
        menu.addAction(QAction('&Exit', menu, 
            shortcut='Ctrl+Q', 
            statusTip='Exit application',
            triggered=self.close))
        
        self.status.add_spacer()
        self.status.addSeparator()
        self.status.addWidget(self.obs.status_widget)