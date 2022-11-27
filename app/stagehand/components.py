from qtstrap import *
import qtawesome as qta


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


class StagehandWidget(QWidget):
    def __init__(self, *args, icon_name='', **kwargs):
        super().__init__(*args, **kwargs)

        if icon_name:
            self.sidebar_button = SidebarButton(parent=self, target=self, icon=qta.icon(icon_name))


class StagehandStatusBarItem(QWidget):
    pass