from qtstrap import *
from codex import DeviceControlsDockWidget
from .sandbox import Sandbox
import qtawesome as qta
from .about import AboutDialog
from .components import StagehandWidget, StagehandStatusBarItem, SidebarButton


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

        # hack
        from . import generic_actions
        from . import input_devices

        self.about = AboutDialog(self)
        self.device_controls = DeviceControlsDockWidget(self)
        
        self.sandbox = Sandbox(self)
        if not self.restoreDockWidget(self.sandbox.tools_dock):
            self.addDockWidget(self.sandbox.tools_dock.starting_area, self.sandbox.tools_dock)

        self.load_settings()

        self.stack = QStackedWidget()

        self.widgets = []
        for widget in StagehandWidget.__subclasses__():
            w = widget(self)
            self.widgets.append(w)
            self.stack.addWidget(w)

        self.setCentralWidget(self.stack)

        self.init_tray_stuff()
        self.init_statusbar()
        self.init_sidebar()

        # restore active widget
        prev_widget = QSettings().value('mainwindow/active_widget', 0)
        self.stack.widget(int(prev_widget)).sidebar_button.click()

        qApp.updater.update_found.connect(self.display_update_available)

    def set_widget(self, widget):
        enable_children(self.sidebar)
        self.stack.setCurrentWidget(widget)
        QSettings().setValue('mainwindow/active_widget', self.stack.currentIndex())

    def display_update_available(self):
        self.tray_icon.showMessage('An update is available.', 'an update is available')

    def init_sidebar(self):
        self.sidebar = BaseToolbar(self, 'sidebar', location='left', size=40)
        self.sidebar.setContextMenuPolicy(Qt.PreventContextMenu)

        for w in self.widgets:
            if hasattr(w, 'sidebar_button'):
                self.sidebar.addWidget(w.sidebar_button)

    def init_statusbar(self):
        self.status = BaseToolbar(self, 'statusbar', location='bottom', size=30)
        self.status.setContextMenuPolicy(Qt.PreventContextMenu)
        
        self.status.addWidget(self.init_settings_btn())
        self.status.add_spacer()

        for widget in StagehandStatusBarItem.__subclasses__():
            self.status.addWidget(widget(self))

        for w in self.widgets:
            if hasattr(w, 'status_widget'):
                self.status.addWidget(w.status_widget)

        self.status.addWidget(QLabel())

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
            qApp.quit()

    def init_tray_stuff(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(OPTIONS.app_info.AppIconName))

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