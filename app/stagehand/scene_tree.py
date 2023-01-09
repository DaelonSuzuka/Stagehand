from qtstrap import *
from qtpy.shiboken import isValid, delete
import qtawesome as qta
from .components import StagehandDockWidget


class SceneTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, parent, node):
        super().__init__(parent)

        self.node = node
        self.obj = node.obj

        obj = node.obj
        
        name = obj.objectName()
        klass = type(obj).__name__

        self.setText(0, klass)

        if isinstance(obj, QWidget):
            self.update_visibility_icon()

    def update_visibility_icon(self):
        if self.obj.isVisible():
            self.setIcon(1, qta.icon('fa5.eye'))
        else:
            self.setIcon(1, qta.icon('fa5.eye-slash'))

    def toggle_visibility(self):
        if self.obj.isVisible():
            self.obj.hide()
        else:
            self.obj.show()

        self.update_visibility_icon()


class TreeNode(QObject):
    inverse = {}

    def __init__(self, obj=None, parent=None, item_parent=None):
        super().__init__()
        self.obj = obj
        self.parent = parent
        self._children = []
        self.item = SceneTreeWidgetItem(item_parent, self)

        self.inverse[obj] = self

        self.obj.installEventFilter(self)
        # self.obj.destroyed.connect(self.obj_destroyed)

    def eventFilter(self, watched, event) -> bool:
        if not isValid(self.item):
            return False
        
        if event.type() in (QEvent.Show, QEvent.Hide):
            self.item.update_visibility_icon()

        if event.type() == QEvent.ChildAdded:
            new_obj = event.child()
            if isinstance(new_obj, (QWidget, QLayout)):
                self.scan()

        return False

    def obj_destroyed(self, obj):
        if obj in self.inverse:
            node = self.inverse[obj]
            if isValid(node.item):
                node.item.parent().removeChild(node.item)
                delete(node.item)

            self.inverse.pop(obj)

    def scan(self):
        for child_obj in self.obj.children():
            if child_obj in self.inverse:
                continue
            if isinstance(child_obj, (QWidget, QLayout)):
                node = TreeNode(obj=child_obj, parent=self, item_parent=self.item)
                self._children.append(node)
                node.scan()


class SceneTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.header().hide()
        self.setColumnCount(2)
        self.header().setMinimumSectionSize(1)
        self.header().setStretchLastSection(False)
        self.header().setSectionResizeMode(0, QHeaderView.Stretch)

        self.itemClicked.connect(self.click)
        self.itemDoubleClicked.connect(self.double_click)
        self.itemSelectionChanged.connect(self.selection_changed)

    def click(self, item, column):
        if column == 1:
            item.toggle_visibility()

    def double_click(self, item, column):
        pass

    def selection_changed(self):
        pass

    def contextMenuEvent(self, event):
        pos = event.globalPos()
        item = self.itemAt(self.viewport().mapFromGlobal(pos))
        menu = QMenu()

        if isinstance(item.obj, QWidget):
            if item.obj.isVisible():
                menu.addAction('Hide').triggered.connect(item.toggle_visibility)
            else:
                menu.addAction('Show').triggered.connect(item.toggle_visibility)
        
        menu.exec_(pos)

    def scan(self, obj):
        self.clear()
        self.root_node = TreeNode(obj=obj, item_parent=self)
        self.root_node.scan()
        self.root_node.item.setExpanded(True)

class SceneTreeDockWidget(StagehandDockWidget):
    _title = 'Scene Tree'
    _starting_area = Qt.LeftDockWidgetArea
    _shortcut = 'Ctrl+L'

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.tree = SceneTree()

        call_later(lambda: self.tree.scan(self.parent()), 2000)

        with CVBoxLayout(self._widget, margins=2) as layout:
            layout.add(self.tree)
