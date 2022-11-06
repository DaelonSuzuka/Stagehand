from qtstrap import *
from .actions import ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandWidget
import qtawesome as qta


class ActionsWidget(QWidget):
    def __init__(self, name='', parent=None):
        super().__init__(parent=parent)
        self.name = name

        self.group = ActionWidgetGroup(f'generic_actions/{name}', self)
        self.actions = [ActionWidget(f'Action {i}', group=self.group) for i in range(1, 13)]

        with CVBoxLayout(self, margins=(0,0,0,0), align='top') as layout:
            layout.add(self.actions)
            layout.add(QWidget(), 1)


class ActionsContainer(StagehandWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, icon_name='mdi.format-list-checkbox', **kwargs)

        self.widgets = []
        self.widget_list = QListWidget()
        self.widget_stack = QStackedWidget()
        self.widget_list.currentRowChanged.connect(self.widget_stack.setCurrentIndex)

        self.create_page_btn = QPushButton(icon=qta.icon('mdi.playlist-plus'), clicked=self.create_page)

        self.add(ActionsWidget('1'))
        self.add(ActionsWidget('2'))
        self.add(ActionsWidget('3'))

        with PersistentCSplitter('generic_actions/splitter', self, orientation='h', margins=(0,0,0,0)) as split:
            with CVBoxLayout(split, 1) as layout:
                with layout.hbox(align='r'):
                    layout.add(self.create_page_btn)
                layout.add(self.widget_list)
            split.add(self.widget_stack, 4)

    def create_page(self):
        pass

    def add(self, widget):
        self.widget_stack.addWidget(widget)
        self.widget_list.addItem(widget.name)
