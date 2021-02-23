from qt import *
from devices import DeviceControlsDockWidget
from judipedal_controls import JudiPedalsControls
from mic_voter import MicVoterWidget
from obs import ObsManager, Sandbox
import qtawesome as qta


class MainWindow(BaseMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("MainWindow")

        self.device_controls = DeviceControlsDockWidget(self)
        
        self.obs = ObsManager(self)
        self.sandbox = Sandbox(self.obs)

        self.pedals = JudiPedalsControls(obs=self.obs)        
        self.voter = MicVoterWidget(obs=self.obs)

        tabs = {
            'OBS Manager': self.obs,
            'Mic Voter': self.voter,
            'Pedals': self.pedals,
            'Sandbox': self.sandbox
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

        # settings button
        settings_btn = QToolButton(self.status, icon=qta.icon('fa.gear', color='gray'))
        menu = QMenu(settings_btn)
        settings_btn.setMenu(menu)
        settings_btn.setPopupMode(QToolButton.InstantPopup)
        self.status.addWidget(settings_btn)
        
        # settings popup menu
        menu.addSeparator()
        menu.addAction(self.device_controls.toggleViewAction())

        menu.addSeparator()
            
        menu.addAction(QAction('&Exit', menu, 
            shortcut='Ctrl+Q', 
            statusTip='Exit application',
            triggered=self.close))
        
        self.status.add_spacer()
        self.status.addWidget(self.obs.status_widget)