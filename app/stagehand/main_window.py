from qtstrap import *
from qtstrap.extras.log_monitor import LogMonitorDropdown
from qtstrap.extras.command_palette import CommandPalette, Command
from qtstrap.extras.code_editor import CodeEditor
from codex import DeviceControlsDockWidget
from .sandbox import Sandbox
from .about import AboutDialog
from .components import StagehandStatusBarItem, StagehandDockWidget
from .tabs import MainTabWidget
from .scene_tree import SceneTreeDockWidget

from monaco import MonacoWidget


class FontSizeMenu(QMenu):
    def __init__(self, parent=None, default=12) -> None:
        super().__init__(parent=parent)
        self.setTitle('Font Size')

        self.default_size = default
        self.font_size: int = QSettings().value('font_size', self.default_size)
        self.set_font_size(self.font_size)

        self.addAction('+').triggered.connect(lambda: self.set_font_size(self.font_size + 2))
        self.addAction('-').triggered.connect(lambda: self.set_font_size(self.font_size - 2))
        self.addAction('Reset').triggered.connect(lambda: self.set_font_size(self.default_size))

    def set_font_size(self, size) -> None:
        set_font_options(self.parent(), {'setPointSize': int(size)})
        self.font_size = int(size)
        QSettings().setValue('font_size', size)


class ThemeMenu(QMenu):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setTitle('Theme')

        self.commands = [
            Command('Theme: Set to Light Mode', triggered=lambda: App().update_theme('light')),
            Command('Theme: Set to Dark Mode', triggered=lambda: App().update_theme('dark')),
        ]

        self.addAction('Light').triggered.connect(lambda: App().update_theme('light'))
        self.addAction('Dark').triggered.connect(lambda: App().update_theme('dark'))


class StyleEditorDockWidget(StagehandDockWidget):
    _title = 'Style Editor'
    _starting_area = Qt.BottomDockWidgetArea
    _shortcut = 'Ctrl+Y'

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        prev_text = QSettings().value('custom_style', '')

        # self.editor = MonacoWidget()
        # self.editor.setText(prev_text)
        # self.editor.setLanguage('css')
        # self.editor.textChanged.connect(lambda t: QSettings().setValue('custom_style', t))

        # with CVBoxLayout(self._widget, margins=2) as layout:
        #     layout.add(self.editor)
        #     with layout.hbox():
        #         layout.add(QLabel(), 1)
        #         layout.add(QPushButton('Apply', clicked=self.apply))

    def apply(self):
        text = self.editor.text()
        self.parent().setStyleSheet(text)


class ReplDockWidget(StagehandDockWidget):
    _title = 'REPL'
    _starting_area = Qt.BottomDockWidgetArea
    _shortcut = 'Ctrl+R'

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        with CVBoxLayout(self._widget, margins=2) as layout:
            layout.add(QLabel('REPL goes here'))


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

        self.style_editor = StyleEditorDockWidget(self)
        self.repl = ReplDockWidget(self)
        self.scene_tree = SceneTreeDockWidget(self)
        self.log_monitor = LogMonitorDropdown(self)
        self.sandbox = Sandbox()
        self.command_palette = CommandPalette(self)
        
        if not self.restoreDockWidget(self.sandbox.tools_dock):
            self.addDockWidget(self.sandbox.tools_dock.starting_area, self.sandbox.tools_dock)

        self.load_settings()

        self.tabs = MainTabWidget()

        self.setCentralWidget(self.tabs)

        self.tab_shortcuts = []
        for i in range(10):
            shortcut = QShortcut(f'Ctrl+{i + 1}', self, activated=lambda i=i: self.tabs.setCurrentIndex(i))
            self.tab_shortcuts.append(shortcut)

        self.commands = [
            Command('Minimize to tray'),
            Command('Quit Application', triggered=self.close, shortcut='Ctrl+Q'),
        ]

        self.init_tray_stuff()

        self.create_statusbar()
        self.init_statusbar_items()
        self.init_settings_menu()

        App().updater.update_found.connect(self.display_update_available)

    def display_update_available(self) -> None:
        self.tray_icon.showMessage('An update is available.', 'an update is available')

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

        menu.addAction(self.style_editor.toggleViewAction())
        menu.addAction(self.repl.toggleViewAction())
        menu.addAction(self.scene_tree.toggleViewAction())

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
            qApp.quit()

    def init_tray_stuff(self):
        self.tray_icon = QSystemTrayIcon(self)
        if files := list(Path(OPTIONS.APPLICATION_PATH).rglob(OPTIONS.app_info.AppIconName)):
            self.tray_icon.setIcon(QIcon(files[0].as_posix()))

        self.tray_menu = QMenu()
        self.tray_menu.addAction(QAction('Stagehand', self, enabled=False))
        self.tray_menu.addAction(QAction('Open', self, triggered=self.show))
        self.tray_menu.addAction(QAction('Quit', self, triggered=qApp.quit))
        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.show()

        self.minimize_to_tray = PersistentCheckableAction('mainwindow/minimize_to_tray', 'Minimize to tray')
