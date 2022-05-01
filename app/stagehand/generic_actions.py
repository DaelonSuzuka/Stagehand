from qtstrap import *
from .actions import ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandWidget, SidebarButton
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
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.sidebar_button = SidebarButton(target=self, icon=qta.icon('mdi.format-list-checkbox'))

        self.widgets = []
        self.widget_list = QListWidget(fixedWidth=150)
        self.widget_stack = QStackedWidget()
        self.widget_list.currentRowChanged.connect(self.widget_stack.setCurrentIndex)

        self.add(ActionsWidget('1'))
        self.add(ActionsWidget('2'))
        self.add(ActionsWidget('3'))

        with PersistentCSplitter('generic_actions_splitter', self, margins=(0,0,0,0)) as split:
            split.setOrientation(Qt.Horizontal)
            split.add(self.widget_list, 1)
            split.add(self.widget_stack, 1)

    def add(self, widget):
        self.widget_stack.addWidget(widget)
        self.widget_list.addItem(widget.name)
