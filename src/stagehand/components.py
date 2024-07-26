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
    name = ''

    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}
