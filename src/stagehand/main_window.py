from codex import DeviceControlsDockWidget
from qtstrap import *
from qtstrap.extras.command_palette import Command, CommandPalette

# from qtstrap.extras.devtools import ReplDockWidget, SceneTreeDockWidget, StyleEditorDockWidget
from qtstrap.extras.log_monitor import LogMonitorDockWidget
import qtawesome as qta

from .about import AboutDialog
from .components import StagehandStatusBarItem, StagehandSidebar, SidebarContainer
from .sandbox import Sandbox
from .tabs import MainTabWidget
# Import library to ensure StagehandSidebar subclasses are discovered
from . import library


class FontSizeMenu(QMenu):
    def __init__(self, parent=None, default=12) -> None:
        super().__init__(parent=parent)
        self.setTitle('Font Size')

        self.default_size = default
        self.font_size: int = int(QSettings().value('font_size', self.default_size))
        self.set_font_size(self.font_size)

        self.addAction('+').triggered.connect(lambda: self.set_font_size(self.font_size + 2))
        self.addAction('-').triggered.connect(lambda: self.set_font_size(self.font_size - 2))
        self.addAction('Reset').triggered.connect(lambda: self.set_font_size(self.default_size))

    def set_font_size(self, size: int | str) -> None:
        self.font_size = int(size)
        set_font_options(self.parent(), {'setPointSize': self.font_size})
        QSettings().setValue('font_size', self.font_size)


@singleton
class MainWindow(BaseMainWindow):
    closing = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.force_close = False

        self.font_menu = FontSizeMenu(self)
        self.theme_menu = ThemeMenu(self)

        self.setTabPosition(
            Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea | Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea,
            QTabWidget.North,
        )

        self.about = AboutDialog(self)
        self.device_controls = DeviceControlsDockWidget(self)
        self.device_controls.hide()

        # self.style_editor = StyleEditorDockWidget(self)
        # self.repl = ReplDockWidget(self)
        # self.scene_tree = SceneTreeDockWidget(self)
        self.log_monitor = LogMonitorDockWidget(self)
        self.sandbox = Sandbox(self)
        self.command_palette = CommandPalette(self)

        self.load_settings()

        self.tabs = MainTabWidget()
        self.sidebar = SidebarContainer(self)
        self.sidebar.hide()

        with PersistentCSplitter('main_split', self, margins=0) as splitter:
            splitter.add(self.sidebar)
            splitter.add(self.tabs)

        self.create_activity_bar()
        self.restore_sidebar_state()

        self.tab_shortcuts = []
        for i in range(10):
            shortcut = QShortcut(f'Ctrl+{i + 1}', self, activated=lambda i=i: self.tabs.setCurrentIndex(i))
            self.tab_shortcuts.append(shortcut)

        self.commands = [
            Command('Minimize to tray'),
            Command('Quit Application', triggered=self.close, shortcut='Ctrl+Q'),
            Command('Theme: Set to Light Mode', triggered=lambda: App().change_theme('light')),
            Command('Theme: Set to Dark Mode', triggered=lambda: App().change_theme('dark')),
        ]

        self.init_tray_stuff()

        self.create_statusbar()
        self.init_statusbar_items()
        self.init_settings_menu()

        App().updater.update_found.connect(self.display_update_available)

        self.show()

    def display_update_available(self) -> None:
        self.tray_icon.showMessage('An update is available.', 'an update is available')

    def create_activity_bar(self):
        self.activity_bar = BaseToolbar(self, 'activitybar', location='left', size=40)
        self.sidebar_buttons: dict[str, QToolButton] = {}
        
        # Create buttons for each sidebar panel
        for name, cls in StagehandSidebar.get_subclasses().items():
            icon = qta.icon(cls.icon_name, color='gray') if cls.icon_name else qta.icon('fa.file', color='gray')
            btn = QToolButton(icon=icon)
            btn.setCheckable(True)
            btn.setToolTip(cls.display_name)
            btn.clicked.connect(lambda checked, n=name: self.toggle_sidebar_panel(n))
            self.activity_bar.addWidget(btn)
            self.sidebar_buttons[name] = btn

    def toggle_sidebar_panel(self, name: str):
        """Toggle visibility of a sidebar panel and update button state."""
        if name not in self.sidebar.panels:
            return
        
        is_visible = self.sidebar.toggle_panel(name)
        
        # Update all button states
        for btn_name, btn in self.sidebar_buttons.items():
            btn.setChecked(btn_name == name and is_visible)
        
        # Save sidebar state
        if is_visible:
            QSettings().setValue('sidebar/current_panel', name)
        else:
            QSettings().remove('sidebar/current_panel')
    
    def restore_sidebar_state(self):
        """Restore sidebar visibility from saved settings."""
        panel_name = QSettings().value('sidebar/current_panel', '')
        if panel_name and panel_name in self.sidebar.panels:
            self.sidebar.show_panel(panel_name)
            if panel_name in self.sidebar_buttons:
                self.sidebar_buttons[panel_name].setChecked(True)

    def init_statusbar_items(self) -> None:
        self.statusbar.add_spacer()

        for widget in StagehandStatusBarItem.__subclasses__():
            self.statusbar.addWidget(widget(self.statusbar))

        self.statusbar.addWidget(QLabel())

    def init_settings_menu(self):
        menu = self.settings_menu

        menu.addAction(self.command_palette.action)
        menu.addSeparator()
        menu.addAction(self.sandbox.tools_dock.toggleViewAction())
        menu.addAction(self.device_controls.toggleViewAction())
        menu.addAction(self.log_monitor.toggleViewAction())

        # menu.addAction(self.style_editor.toggleViewAction())
        # menu.addAction(self.repl.toggleViewAction())
        # menu.addAction(self.scene_tree.toggleViewAction())

        menu.addSeparator()
        menu.addMenu(self.font_menu)
        menu.addMenu(self.theme_menu)

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
            App().quit()

    def init_tray_stuff(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(OPTIONS.ICON_PATH))

        self.tray_menu = QMenu()
        self.tray_menu.addAction(QAction('Open', self, triggered=self.show))
        self.tray_menu.addAction(QAction('Quit', self, triggered=App().quit))
        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.show()
        self.tray_icon.setToolTip('Stagehand')

        self.minimize_to_tray = PersistentCheckableAction('mainwindow/minimize_to_tray', 'Minimize to tray')
