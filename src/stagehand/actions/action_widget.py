import json

import qtawesome as qta
from qtstrap import *

from stagehand.sandbox import Sandbox
from stagehand.library import SaveToLibraryDialog, save_to_library

from .action_filter import ActionFilter
from .action_trigger import ActionTrigger
from .items import ActionItem


class ActionWidgetGroup(QObject):
    action_changed = Signal()

    def __init__(self, name, parent=None, changed=None, autosave=True):
        super().__init__(parent=parent)
        self.this = parent
        self.name = name
        self.autosave = autosave

        self.data = {'actions': {}, 'filter': {'enabled': True, 'filters': []}}

        self.filter = ActionFilter(self.action_changed, owner=self)
        self.active = True

        if changed:
            self.action_changed.connect(changed)

        self.actions = []
        if autosave:
            self.load()

    def register(self, action):
        self.actions.append(action)

        action.changed.connect(self.on_action_change)
        action.action.this = self.this

    def on_action_change(self):
        if self.autosave:
            self.save()
        self.action_changed.emit()

    def set_active(self, value: bool):
        self.active = value

    def can_run(self) -> bool:
        if not self.active:
            return False
        if not self.filter.check_filters():
            return False
        return True

    def set_data(self, data):
        self.data = data
        self.filter.set_data(self.data)
        self.filter.enabled.setChecked(True)

    def get_data(self):
        data = {
            'actions': [a.get_data() for a in self.actions],
            **self.filter.get_data(),
        }
        return data


class Action(QWidget):
    changed = Signal()

    def __init__(self, changed, action_type='sandbox', action='', owner=None):
        super().__init__()

        self.owner = owner
        self.type = QComboBox()
        self.action = None
        self._changed = changed
        self.data = None
        self.this = None

        for action in ActionItem.__subclasses__():
            self.type.addItem(action.name)

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.type_changed)

        self.action_box = CHBoxLayout(margins=0)

        with CHBoxLayout(self, margins=0) as layout:
            with layout.vbox(align='top'):
                self.label = layout.add(QLabel('Action:', minimumWidth=60))
            with layout.vbox(align='top'):
                layout.add(self.type)
            layout.add(self.action_box, 1)

    def type_changed(self):
        if self.action:
            self.action.deleteLater()
            self.action = None
        self.action = ActionItem.get_item(self.type.currentText())(self._changed, self.owner)
        if self.data:
            self.action.set_data(self.data['action'])
        self.action_box.add(self.action)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction(QAction('Copy Action', self, triggered=self.copy))
        menu.addAction(QAction('Paste Action', self, triggered=self.paste))
        menu.addAction(QAction('Reset Action', self, triggered=self.reset))
        menu.addSeparator()
        menu.addAction('Save Action to Library').triggered.connect(self.save_to_library)
        menu.exec_(event.globalPos())

    def copy(self):
        data = json.dumps(self.get_data())
        QClipboard().setText(data)

    def paste(self):
        data = json.loads(QClipboard().text())
        self.set_data(data)

    def reset(self):
        self.type.setCurrentText('sandbox')
        self.action.reset()

    def save_to_library(self):
        """Open dialog to save this output to the library."""
        data = self.get_data()
        dialog = SaveToLibraryDialog('outputs', data, self)
        if dialog.exec() == QDialog.Accepted and dialog.get_name():
            save_to_library('outputs', data, dialog.get_name())

    def _refresh_library_sidebar(self):
        """Find and refresh the library sidebar tree."""
        from stagehand.library.sidebar import LibraryTreeWidget
        
        for widget in QApplication.allWidgets():
            if isinstance(widget, LibraryTreeWidget):
                widget.refresh()
                return

    def set_data(self, data):
        if 'action' in data:
            self.data = data
            if 'type' not in data['action']:
                data['action']['type'] = 'sandbox'

            self.type.setCurrentText(data['action']['type'])
            self.type_changed()

    def get_data(self):
        return {
            'action': {
                'type': self.type.currentText(),
                **(self.action.get_data() if self.action else {}),
            }
        }

    def run(self):
        self.action.run()


class CustomAnimatedToggle(AnimatedToggle):
    def sizeHint(self):
        return QSize(50, 32)


@draggable
class ActionWidget(QWidget):
    changed = Signal()

    @classproperty
    def default_data(cls):
        return {
            'name': 'Action',
            'enabled': True,
            'action': {'type': 'sandbox', 'action': ''},
            'trigger': {'enabled': True, 'trigger_type': 'keyboard', 'trigger': ''},
            'filter': {'enabled': True, 'filters': []},
        }

    def __init__(
        self,
        name='',
        group: ActionWidgetGroup = None,
        trigger=False,
        data=None,
        changed=None,
        parent=None,
    ):
        super().__init__(parent=parent)

        self.name = name
        action_type = 'sandbox'
        action = ''

        if data:
            self.name = data['name']
            action = data['action']
            if 'type' in data:
                action_type = data['type']

        self.run_btn = QPushButton('', clicked=self.run, icon=qta.icon('fa5.play-circle'))
        self.run_btn.setIconSize(QSize(22, 22))

        self.enabled = CustomAnimatedToggle()
        self.enabled.stateChanged.connect(lambda _: self.changed.emit())

        self.label = LabelEdit(self.name, changed=self.on_change)
        self.action = Action(self.on_change, action_type, action, owner=self)
        self.trigger = ActionTrigger(self.on_change, run=self.run, owner=self)
        self.filter = ActionFilter(self.on_change, owner=self)

        if trigger:
            self.trigger.enabled.setChecked(True)
            self.filter.enabled.setChecked(True)

        self.group: ActionWidgetGroup | None = group
        if group:
            group.register(self)

        if changed:
            self.changed.connect(changed)

        if data:
            self.set_data(data)

        self.do_layout()
        
        # Drag and drop state for library items
        self.setAcceptDrops(True)
        self._drop_target = None
        self._highlighted_widget = None

    def do_layout(self):
        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                layout.add(self.label)
                layout.add(QWidget(), 1)
                layout.add(self.enabled)
                layout.add(self.filter)
            with layout.hbox(margins=0):
                layout.add(self.trigger)
                layout.add(QWidget(), 1)
            with layout.hbox(margins=0):
                layout.add(self.action, 2)
                with layout.vbox(align='top'):
                    layout.add(self.run_btn)
            layout.add(HLine())

    def get_data(self):
        return {
            'name': self.label.text(),
            'enabled': self.enabled.isChecked(),
            **self.action.get_data(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
        }

    def set_data(self, data: dict | None):
        if not data:
            data = self.default_data

        self.enabled.setChecked(data.get('enabled', True))
        self.label.setText(data['name'])
        self.action.set_data(data)
        self.trigger.set_data(data)
        self.filter.set_data(data)
        call_later(self.on_change, 50)  # TODO: this is a hack, find a real solution

    def on_change(self):
        self.filter.setVisible(self.filter.enabled.isChecked())
        self.trigger.setVisible(self.trigger.enabled.isChecked())
        self.changed.emit()

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction('Run').triggered.connect(self.run)
        menu.addAction('Rename').triggered.connect(self.label.start_editing)
        menu.addAction('Copy').triggered.connect(self.copy)
        menu.addAction('Paste').triggered.connect(self.paste)
        menu.addSeparator()
        menu.addAction('Save Action to Library').triggered.connect(self.save_to_library)
        menu.addAction(self.trigger.enabled)
        menu.addAction(self.filter.enabled)
        menu.addAction('Reset').triggered.connect(self.reset)
        menu.addAction('Remove').triggered.connect(self.remove)
        menu.exec_(event.globalPos())

    def get_drag_data(self) -> QMimeData:
        mime = QMimeData()
        data = json.dumps(self.get_data()).encode()
        mime.setData('action_drop', data)
        return mime

    def handle_drop(self, drop):
        if drop == Qt.MoveAction:
            self.remove()

    # ==================== Library Drag & Drop ====================
    
    def dragEnterEvent(self, event):
        """Accept drag events from library items."""
        if event.mimeData().hasFormat('library_drop'):
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragMoveEvent(self, event):
        """Highlight the appropriate slot based on drag position and item category."""
        if not event.mimeData().hasFormat('library_drop'):
            self._clear_highlight()
            event.ignore()
            return
        
        # Parse mime data to get category
        data = json.loads(bytes(event.mimeData().data('library_drop')).decode())
        category = data['category']
        
        pos = event.pos()
        
        if category == 'actions':
            # Highlight entire widget
            self._highlight_widget(self)
            self._drop_target = 'action'
        elif category == 'triggers':
            # Check if hovering over trigger widget
            trigger_rect = self.trigger.geometry()
            if trigger_rect.contains(pos):
                self._highlight_widget(self.trigger)
                self._drop_target = 'trigger'
            else:
                self._clear_highlight()
        elif category == 'outputs':
            # Check if hovering over action (output) widget
            action_rect = self.action.geometry()
            if action_rect.contains(pos):
                self._highlight_widget(self.action)
                self._drop_target = 'output'
            else:
                self._clear_highlight()
        else:
            # Unknown category or filter (not implemented)
            self._clear_highlight()
        
        if self._drop_target:
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragLeaveEvent(self, event):
        """Clear highlight when drag leaves the widget."""
        self._clear_highlight()
    
    def dropEvent(self, event):
        """Handle drop from library sidebar."""
        if not event.mimeData().hasFormat('library_drop'):
            event.ignore()
            return
        
        data = json.loads(bytes(event.mimeData().data('library_drop')).decode())
        category = data['category']
        item_data = data['data']
        
        if category == 'actions':
            # Replace entire action (but keep name)
            name = self.label.text()
            self.set_data(item_data)
            self.label.setText(name)
        elif category == 'triggers' and self._drop_target == 'trigger':
            self.trigger.set_data(item_data)
        elif category == 'outputs' and self._drop_target == 'output':
            self.action.set_data(item_data)
        
        self._clear_highlight()
        self.changed.emit()
        event.acceptProposedAction()
    
    def _highlight_widget(self, widget):
        """Highlight widget with border outline."""
        self._clear_highlight()
        self._highlighted_widget = widget
        # Store original object name to restore later
        self._original_object_name = widget.objectName()
        widget.setObjectName("_drag_highlight_")
        # Use object name selector to prevent cascading to children
        widget.setStyleSheet("QObject#_drag_highlight_ { border: 2px solid #0078D7; border-radius: 3px; }")
    
    def _clear_highlight(self):
        """Clear any active highlight."""
        if self._highlighted_widget:
            # Restore original object name
            self._highlighted_widget.setObjectName(getattr(self, '_original_object_name', ''))
            self._highlighted_widget.setStyleSheet("")
        self._highlighted_widget = None
        self._drop_target = None

    def copy(self):
        data = {
            **self.action.get_data(),
            **self.trigger.get_data(),
            **self.filter.get_data(),
        }
        QClipboard().setText(json.dumps(data))

    def paste(self):
        data = json.loads(QClipboard().text())
        self.action.set_data(data)
        self.trigger.set_data(data)
        self.filter.set_data(data)

    def save_to_library(self):
        """Open dialog to save this action to the library."""
        data = self.get_data()
        dialog = SaveToLibraryDialog('actions', data, self)
        if dialog.exec() == QDialog.Accepted and dialog.get_name():
            save_to_library('actions', data, dialog.get_name())
            self._refresh_library_sidebar()

    def _refresh_library_sidebar(self):
        """Find and refresh the library sidebar tree."""
        from qtstrap import App
        from stagehand.library.sidebar import LibraryTreeWidget
        
        # Find all LibraryTreeWidget instances in the application
        for widget in App.instance().allWidgets():
            if isinstance(widget, LibraryTreeWidget):
                widget.refresh()
                return

    def reset(self):
        self.label.setText(self.name)
        self.action.reset()
        self.trigger.reset()
        self.filter.reset()
        self.on_change()

    def remove(self):
        if self.group:
            self.group.actions.remove(self)
            self.group.parent().actions.remove(self)
            self.group.action_changed.emit()
        self.deleteLater()

    def run(self):
        if self.group:
            if not self.group.can_run():
                return

        if not self.enabled:
            return

        if not self.filter.check_filters():
            return

        Sandbox().this = self
        Sandbox().source = self.sender()
        self.action.run()
        Sandbox().this = None
        Sandbox().source = None


class CompactActionWidget(ActionWidget):
    @classproperty
    def default_data(cls):
        return {
            'name': 'Action',
            'enabled': True,
            'action': {'type': 'sandbox', 'action': ''},
            'trigger': {'enabled': False, 'trigger_type': 'sandbox', 'trigger': ''},
            'filter': {'enabled': False, 'filters': []},
        }

    def do_layout(self):
        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.label)
            layout.add(VLine())
            # layout.add(self.trigger, 1)
            # layout.add(self.filter)
            layout.add(self.action, 2)
            layout.add(self.run_btn)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction('Run').triggered.connect(self.run)
        menu.addAction('Rename').triggered.connect(self.label.start_editing)
        menu.addAction('Copy').triggered.connect(self.copy)
        menu.addAction('Paste').triggered.connect(self.paste)
        menu.addSeparator()
        menu.addAction('Save Action to Library').triggered.connect(self.save_to_library)
        menu.addAction('Reset').triggered.connect(self.reset)
        menu.exec_(event.globalPos())
