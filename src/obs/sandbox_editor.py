from qtstrap import *
from qtstrap.extras import code_editor


class ScriptBrowser(QTreeWidget):
    def __init__(self, *args, changed=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'script_browser'

        self.setUniformRowHeights(True)
        self.setExpandsOnDoubleClick(False)
        self.setHeaderLabels(['Files'])
        
        self.index_column = 3

        self.itemSelectionChanged.connect(self.save_state)

        self.nodes = {}
        self.refresh_nodes()
        self.restore_state()

        if changed:
            self.itemSelectionChanged.connect(changed)
        
    def selected_items(self):
        return [item.text(self.index_column) for item in self.selectedItems()]

    def save_state(self):
        QSettings().setValue(self.name, self.selected_items())

    def restore_state(self):
        prev_items = QSettings().value(self.name)
        if prev_items:
            for name, node in self.nodes.items():
                if name in prev_items:
                    node.setSelected(True)

    def create_intermediate_nodes(self, name):
        parts = name.split('/')
        
        if len(parts) == 2:
            if parts[0] not in self.nodes:
                node = QTreeWidgetItem(self)
                node.setText(0, parts[0])
                node.setText(3, parts[0])
                node.setText(4, 'folder')
                self.nodes[parts[0]] = node

    def create_node(self, name):
        parts = name.split('/')
        if len(parts) == 1:
            node = QTreeWidgetItem(self)
            node.setText(0, parts[-1])
            node.setText(3, name)
            node.setText(4, 'file')
            self.nodes[name] = node

        else:
            self.create_intermediate_nodes(name)
            node = QTreeWidgetItem(self.nodes[parts[-2]])
            node.setText(0, parts[-1])
            node.setText(3, name)
            node.setText(4, 'file')
            self.nodes[name] = node

        return node
        
    def refresh_nodes(self):
        self.clear()
        self.nodes = {}

        files = [f.as_posix()[8:] for f in Path('./sandbox').rglob('*.py')]
    
        for f in files:
            self.create_node(f)

        self.expandAll()

    # def create_folder(self, parent):
    #     node = QTreeWidgetItem(parent)
    #     node.setText(0, 'new_folder')
    #     self.nodes.append(node)

    # def create_file(self):
    #     print('new file')
    #     item = self.create_node('untitled.py')
    #     self.rename_file(item)

    # def on_rename(self):
    #     self.file_created.emit()

    # def rename_file(self, item):
    #     self.openPersistentEditor(item)

    # def stop_renaming(self, item, column):
    #     print(item)
    #     self.closePersistentEditor(item)

    # def contextMenuEvent(self, event: PySide2.QtGui.QContextMenuEvent) -> None:
    #     pos = event.globalPos()
    #     item = self.itemAt(self.viewport().mapFromGlobal(pos))

    #     menu = QMenu()
    #     # menu.addAction(QAction('New Folder', self, triggered=lambda: self.create_folder(item)))
    #     menu.addAction(QAction('New File', self, triggered=self.create_file))
    #     menu.addAction(QAction('Rename', self, triggered=lambda: self.rename_file(item)))
    #     menu.exec_(pos)


class SandboxEditor(QWidget):
    reload = Signal(Slot)

    def __init__(self, obs, parent=None):
        super().__init__(parent=parent)
        self.obs = obs

        self.scripts = {}
        self.scripts_path = Path(OPTIONS.APPLICATION_PATH / 'sandbox')

        for name in [f for f in self.scripts_path.rglob('*.py')]:
            with open(name) as f:
                self.scripts[name.parts[-1]] = f.read()

        self.browser = ScriptBrowser(changed=self.script_changed)
        self.editor = code_editor.CodeEditor()
        self.editor.textChanged.connect(self.save)
        self.error = QLabel()
        
        self.current_file = ''
        self.script_changed()

        with CVBoxLayout(self) as layout:
            with layout.split(name='sandbox_splitter'):
                with layout.vbox(margins=(0,0,0,0)):
                    layout.add(self.browser)
                with layout.vbox(margins=(0,0,0,0)):
                    layout.add(self.editor)
                    layout.add(self.error)

    @Slot()
    def set_error(self, error):
        self.error.setText(error)

    def save(self):
        if items := self.browser.selected_items():
            name = items[0]
            self.scripts[name] = self.editor.toPlainText()
            with open(self.scripts_path / name, 'w') as f:
                f.write(self.scripts[name])
            self.reload.emit(self.set_error)

    def script_changed(self):
        if items := self.browser.selected_items():
            name = items[0]
            if name in self.scripts:
                self.editor.setText(self.scripts[name])
                self.current_file = 'sandbox/' + name
