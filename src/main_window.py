from qt import *
from devices import DeviceControlsDockWidget
from judipedal_controls import JudiPedalsControls
import json
from mic_voter import MicVoterWidget
from obs import ObsManager
import qtawesome as qta



class ObsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._id = 0
        self.active = False


        self.payload = QLineEdit()
        self.payload.returnPressed.connect(self.enter)
        self.history = QTextEdit()

        self.obs.message_recieved.connect(lambda s: self.history.append(s))

        self.scenes = QListWidget()
        self.current_scene = QLabel('Unknown')
        self.sources = QListWidget()


        with CVBoxLayout(self) as layout:
            layout.add(self.mic_voter)
            
            # with layout.hbox() as layout:
            #     with layout.vbox() as layout:
            #         layout.add(QLabel('Scenes:'))
            #         layout.add(self.scenes)
            #         layout.add(QLabel('Sources:'))
            #         layout.add(self.current_scene)
            #         layout.add(self.sources)
            #     with layout.vbox() as layout:    
            #         layout.add(self.payload)
            #         layout.add(self.history)


    # def pedal(self, number):
    #     if not self.active:
    #         return

    #     actions = {
    #         1: lambda: self.obs.send({"request-type": "GetSceneList"}),
    #         2: lambda: self.obs.send({"request-type": "GetSourcesList"}),
    #         3: lambda: self.obs.send({"request-type": "GetAuthRequired"}),
    #         4: lambda: self.obs.send({"request-type": "GetAuthRequired"}),
    #     }

    #     actions[number]()

    def enter(self):
        try:
            payload = json.dumps(self.payload.text())
            self.obs.send(payload)
        except:
            pass


class MainWindow(BaseMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("MainWindow")

        self.device_controls = DeviceControlsDockWidget(self)
        
        self.obs = ObsManager(self)
        self.pedals = JudiPedalsControls(obs=self.obs)        
        self.voter = MicVoterWidget(obs=self.obs)

        tabs = {
            'OBS Manager': self.obs,
            'Mic Voter': self.voter,
            'Pedals': self.pedals,
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