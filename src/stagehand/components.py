from qtstrap import *
from abc import abstractmethod


class StagehandPage(QWidget):
    page_type = ''
    tags = ['user']

    @classmethod
    def get_subclasses(cls):
        return {c.page_type: c for c in cls.__subclasses__()}

    def tab_context_menu(self, pos: QPoint, tabs, tab_idx: int):
        raise NotImplementedError

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    def set_data(self, data: dict) -> None:
        pass

    def get_data(self) -> dict:
        data = {
            'page_type': self.page_type,
        }
        return data


class SingletonPageMixin:
    tags = ['singleton']

    def get_name(self) -> str:
        return self.page_type

    def tab_context_menu(self, pos: QPoint, tabs, tab_idx: int):
        menu = QMenu()
        menu.addAction('Close').triggered.connect(lambda: tabs.remove_page(tab_idx))
        menu.exec_(pos)


class StagehandStatusBarItem(QWidget):
    pass


class StagehandDockWidget(BaseDockWidget):
    pass


class StagehandSidebar(QWidget):
    """Base class for sidebar panels.
    
    Subclasses must define:
        - name: Unique identifier (used for lookup)
        - display_name: Human-readable name (shown in UI)
        - icon_name: qtawesome icon name (shown in activity bar)
    
    Discovery is automatic via __subclasses__() pattern.
    """
    name = ''
    display_name = ''
    icon_name = ''

    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}


class SidebarContainer(QWidget):
    """Container that manages all sidebar panels in a QStackedWidget.
    
    Discovers all StagehandSidebar subclasses and instantiates them.
    Provides switching and visibility toggling via activity bar buttons.
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        
        self.panels: dict[str, StagehandSidebar] = {}
        self.stack = QStackedWidget(self)
        
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.stack)
        
        # Discover and instantiate all sidebar subclasses
        for name, cls in StagehandSidebar.get_subclasses().items():
            panel = cls(parent=self)
            self.panels[name] = panel
            self.stack.addWidget(panel)
        
        # Initially hidden until a panel is selected
        self.hide()
    
    def show_panel(self, name: str):
        """Show sidebar and switch to named panel."""
        if name in self.panels:
            self.show()
            self.stack.setCurrentWidget(self.panels[name])
    
    def toggle_panel(self, name: str) -> bool:
        """Toggle visibility of named panel. Returns True if now visible."""
        if name not in self.panels:
            return False
        
        current = self.stack.currentWidget()
        is_current = current and current.name == name
        
        if self.isVisible() and is_current:
            self.hide()
            return False
        else:
            self.show_panel(name)
            return True
    
    def current_panel_name(self) -> str:
        """Return name of currently visible panel, or empty string if hidden."""
        if not self.isVisible():
            return ''
        widget = self.stack.currentWidget()
        return widget.name if widget else ''
