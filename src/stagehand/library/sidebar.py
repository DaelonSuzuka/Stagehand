"""Library sidebar panel for browsing reusable definitions."""

from qtstrap import *
from qtstrap.extras.command_palette import Command
from stagehand.components import StagehandSidebar
from .manager import get_library
import json


class LibraryTreeWidget(QTreeWidget):
    """Tree widget displaying library items organized by category."""
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setHeaderHidden(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        
        # Enable dragging
        self.setDragEnabled(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragDropMode(QAbstractItemView.DragOnly)
        
        self.refresh()
    
    def mimeData(self, items):
        """Create mime data for dragged items."""
        if not items:
            return QMimeData()
        
        item = items[0]  # Single selection
        category = item.data(0, Qt.UserRole)
        index = item.data(0, Qt.UserRole + 1)
        item_data = item.data(0, Qt.UserRole + 2)
        
        # Category headers (index == -1) are not draggable
        if index == -1 or not item_data:
            return QMimeData()
        
        # Remove internal markers
        data = {k: v for k, v in item_data.items() if not k.startswith('_')}
        
        mime = QMimeData()
        payload = json.dumps({
            'category': category,
            'data': data
        })
        mime.setData('library_drop', payload.encode())
        return mime
    
    def refresh(self):
        """Reload library items and rebuild the tree."""
        self.clear()
        
        library = get_library()
        # Reload from disk to catch any changes
        library.load()
        items = library.get_all_items()
        
        # Category display names and icons
        categories = {
            'triggers': ('Triggers', 'mdi.keyboard'),
            'filters': ('Filters', 'mdi.filter'),
            'outputs': ('Outputs', 'mdi.export'),
            'actions': ('Actions', 'mdi.lightning-bolt'),
        }
        
        for category_key, (display_name, icon_name) in categories.items():
            category_items = items.get(category_key, [])
            if not category_items:
                continue
            
            category_item = QTreeWidgetItem(self, [display_name])
            category_item.setExpanded(True)
            category_item.setData(0, Qt.UserRole, category_key)
            category_item.setData(0, Qt.UserRole + 1, -1)  # -1 indicates category header
            
            for idx, item in enumerate(category_items):
                name = item.get('name', 'Unnamed')
                is_builtin = item.get('_builtin', False)
                
                display_text = f"{'🔧 ' if is_builtin else ''}{name}"
                child = QTreeWidgetItem(category_item, [display_text])
                child.setData(0, Qt.UserRole, category_key)
                child.setData(0, Qt.UserRole + 1, idx)
                child.setData(0, Qt.UserRole + 2, item)  # Store full item data
    
    def show_context_menu(self, pos: QPoint):
        """Show context menu for library items."""
        item = self.itemAt(pos)
        if not item:
            return
        
        category = item.data(0, Qt.UserRole)
        index = item.data(0, Qt.UserRole + 1)
        
        # Don't show menu for category headers
        if index == -1:
            return
        
        library = get_library()
        item_data = item.data(0, Qt.UserRole + 2)
        is_builtin = item_data.get('_builtin', False)
        
        menu = QMenu(self)
        
        copy_action = menu.addAction('Copy')
        copy_action.triggered.connect(lambda: self.copy_item(category, index))
        
        if not is_builtin:
            menu.addSeparator()
            rename_action = menu.addAction('Rename')
            rename_action.triggered.connect(lambda: self.rename_item(category, index))
            delete_action = menu.addAction('Delete')
            delete_action.triggered.connect(lambda: self.delete_item(category, index))
        
        menu.exec_(self.mapToGlobal(pos))
    
    def copy_item(self, category: str, index: int):
        """Copy library item to clipboard."""
        import json
        
        library = get_library()
        items = library.get_all_items().get(category, [])
        
        if 0 <= index < len(items):
            item = items[index]
            # Remove internal markers before copying
            copy_data = {k: v for k, v in item.items() if not k.startswith('_')}
            QClipboard().setText(json.dumps(copy_data))
    
    def rename_item(self, category: str, index: int):
        """Rename a library item."""
        library = get_library()
        
        # Index in tree is from merged list (builtin + user)
        # Need to calculate index in user_items
        builtin_count = len(library.builtin_items.get(category, []))
        user_index = index - builtin_count
        
        items = library.user_items.get(category, [])
        
        if 0 <= user_index < len(items):
            current_name = items[user_index].get('name', '')
            new_name, ok = QInputDialog.getText(
                self, 'Rename Item', 'Enter new name:', 
                text=current_name
            )
            
            if ok and new_name:
                library.rename_item(category, user_index, new_name)
                self.refresh()
    
    def delete_item(self, category: str, index: int):
        """Delete a library item."""
        library = get_library()
        
        # Index in tree is from merged list (builtin + user)
        # Need to calculate index in user_items
        builtin_count = len(library.builtin_items.get(category, []))
        user_index = index - builtin_count
        
        reply = QMessageBox.question(
            self, 'Delete Item', 
            'Are you sure you want to delete this item?',
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            library.delete_item(category, user_index)
            self.refresh()


class LibrarySidebar(StagehandSidebar):
    """Sidebar panel for the library of reusable definitions."""
    
    name = 'library'
    display_name = 'Library'
    icon_name = 'mdi.bookshelf'
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.tree = LibraryTreeWidget(self)
        
        with CVBoxLayout(self, margins=0) as layout:
            layout.add(self.tree)
    
    def refresh(self):
        """Refresh the library tree."""
        self.tree.refresh()