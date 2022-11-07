from qtstrap import *
from qtstrap.extras.log_monitor import LogMonitorDropdown
from qtstrap.extras.command_palette import CommandPalette, Command
from codex import DeviceControlsDockWidget
from .sandbox import Sandbox
from .about import AboutDialog
from .components import StagehandWidget, StagehandStatusBarItem


class FontSizeMenu(QMenu):
    def __init__(self, parent=None, default=12) -> None:
        super().__init__(parent=parent)
        self.setTitle('Font Size')

        self.default_size = default
        self.font_size:int = QSettings().value('font_size', self.default_size)
        self.set_font_size(self.font_size)

        self.addAction('+').triggered.connect(lambda: self.set_font_size(self.font_size + 2))
        self.addAction('-').triggered.connect(lambda: self.set_font_size(self.font_size - 2))
        self.addAction('Reset').triggered.connect(lambda: self.set_font_size(self.default_size))

    def set_font_size(self, size) -> None:
        set_font_options(self.parent(), {'setPointSize': int(size)})
        self.font_size = int(size)
        QSettings().setValue('font_size', size)


class MainWindow(BaseMainWindow):
    closing = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.force_close = False

        self.font_menu = FontSizeMenu(self)

        # hack
        from . import generic_actions

        self.about = AboutDialog(self)
        self.device_controls = DeviceControlsDockWidget(self)
        self.log_monitor = LogMonitorDropdown(self)
        self.command_palette = CommandPalette(self)
        
        self.sandbox = Sandbox(self)
        if not self.restoreDockWidget(self.sandbox.tools_dock):
            self.addDockWidget(self.sandbox.tools_dock.starting_area, self.sandbox.tools_dock)

        self.load_settings()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.widgets = []

        self.commands = [
            Command("Minimize to tray"),
            Command("Quit Application", triggered=self.close, shortcut='Ctrl+Q'),
        ]

        self.init_tray_stuff()

        self.create_sidebar()
        self.create_statusbar()
        self.init_statusbar_items()
        self.init_settings_menu()

        self.init_widgets()

        App().updater.update_found.connect(self.display_update_available)

    def set_widget(self, widget) -> None:
        enable_children(self.sidebar)
        self.stack.setCurrentWidget(widget)
        QSettings().setValue('mainwindow/active_widget', self.stack.currentIndex())

    def display_update_available(self) -> None:
        self.tray_icon.showMessage('An update is available.', 'an update is available')

    def init_widgets(self) -> None:
        for widget in StagehandWidget.__subclasses__():
            w = widget(parent=self.stack)
            self.widgets.append(w)
            self.stack.addWidget(w)
            if hasattr(w, 'on_app_close'):
                self.closing.connect(w.on_app_close)
            if hasattr(w, 'sidebar_button'):
                self.sidebar.addWidget(w.sidebar_button)

        # restore active widget
        prev_widget = int(QSettings().value('mainwindow/active_widget', 0))
        if prev_widget < self.stack.count():
            self.stack.widget(prev_widget).sidebar_button.click()

    def init_statusbar_items(self) -> None:
        self.statusbar.add_spacer()

        for widget in StagehandStatusBarItem.__subclasses__():
            w: StagehandStatusBarItem = widget(self.statusbar)
            self.statusbar.addWidget(w)

        self.statusbar.addWidget(QLabel())

    def init_settings_menu(self):
        menu = self.settings_menu

        menu.addAction(self.command_palette.action)
        menu.addSeparator()
        menu.addAction(self.sandbox.tools_dock.toggleViewAction())
        menu.addAction(self.device_controls.toggleViewAction())
        menu.addAction(self.log_monitor.toggleViewAction())

        menu.addSeparator()
        menu.addMenu(self.font_menu)

        menu.addSeparator()
        menu.addAction(self.minimize_to_tray)

        menu.addSeparator()
        menu.addAction(App().updater.check_for_updates_action())
        menu.addAction(self.about.show_action())
        
        menu.addSeparator()
        menu.addAction('&Exit', shortcut='Ctrl+Q').triggered.connect(self._close)

    def _close(self):
        self.force_close = True
        self.close()

    def closeEvent(self, event):
        self.save_settings()

        if not self.force_close and self.minimize_to_tray.isChecked():
            event.ignore()
            self.hide()
        else:
            self.closing.emit()
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