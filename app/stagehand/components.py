from qtstrap import *
import qtawesome as qta
from abc import abstractmethod


class SidebarButton(QPushButton):
    def __init__(self, *args, target=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setIconSize(QSize(40, 40))
        self.setFlat(True)
        self.target = target
        self.clicked.connect(self.on_click)

    def on_click(self):
        self.parent().parent().set_widget(self.target)
        self.setEnabled(False)


class StagehandPage(QWidget):
    @classmethod
    def get_subclasses(cls):
        return {c.page_type: c for c in cls.__subclasses__()}

    @abstractmethod    
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def set_data(self, data: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_data(self) -> dict:
        raise NotImplementedError


class StagehandWidget(QWidget):
    def __init__(self, *args, icon_name='', **kwargs):
        super().__init__(*args, **kwargs)

        if icon_name:
            self.sidebar_button = SidebarButton(parent=self, target=self, icon=qta.icon(icon_name))


class StagehandStatusBarItem(QWidget):
    pass


class StagehandDockWidget(QDockWidget):
    _title = ''
    _starting_area = Qt.BottomDockWidgetArea
    _shortcut = ''
    _features = QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable

    def __init__(self, parent=None):
        super().__init__(self._title, parent=parent)
        self.setObjectName(self._title.replace(' ', ''))

        self._widget = QWidget()
        self.setWidget(self._widget)

        self.setFeatures(self._features)
        
        if not parent.restoreDockWidget(self):
            parent.addDockWidget(self._starting_area, self)
            self.hide()
        
        self.closeEvent = lambda x: self.hide()

    def toggleViewAction(self):
        action = super().toggleViewAction()
        if self._shortcut:
            action.setShortcut(self._shortcut)
        return action
