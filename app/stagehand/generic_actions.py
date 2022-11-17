from qtstrap import *
from .actions import ActionWidget, ActionWidgetGroup
from stagehand.components import StagehandWidget
import qtawesome as qta
import json


class PageItem(QListWidgetItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ActionsPage(QWidget):
    changed = Signal()
    
    def __init__(self, name='', changed=None, data=None, parent=None):
        super().__init__(parent=parent)
        self.name = name

        self.item = PageItem(name)
        self.item.page = self

        self.label = LabelEdit(f'Page {name}', changed=self.name_changed)
        self.group = ActionWidgetGroup(name, changed=self.on_change, parent=self, autosave=False)

        self.actions = []
        self.actions_container = CVBoxLayout()

        if changed:
            self.changed.connect(changed)

        if data is not None:
            self.set_data(data)
        
        with CVBoxLayout(self, margins=0) as layout:
            with layout.hbox(margins=0):
                layout.add(self.label)
                layout.add(QWidget(), 1)
                # layout.add(QPushButton('Add Action'))
                layout.add(self.group.filter)
            with layout.scroll(margins=0):
                layout.setStretchFactor(layout._layout, 1)
                layout.add(self.actions_container)
                layout.add(QWidget(), 1)

    def name_changed(self):
        self.item.setText(self.label.text())
        self.changed.emit()

    def on_change(self):
        self.changed.emit()

    def set_data(self, data):
        self.data = data
        self.group.set_data(self.data)

        label = f'Page {self.name}'
        if 'label' in data:
            label = data['label']
        self.label.setText(label)
        self.item.setText(label)

        if 'actions' in data:
            for name in data['actions']:
                action = ActionWidget(name, group=self.group)
                self.actions.append(action)
                self.actions_container.add(action)
        else:
            actions = {}
            for i in range(1, 13):
                name = f'Action {i}'
                actions[name] = {
                    "name": name,
                    "label": name,
                    "action_type": "sandbox",
                    "action": "",
                    "trigger": {
                        "enabled": True,
                        "trigger_type": "sandbox",
                        "trigger": ""
                    },
                    "filter": {
                        "enabled": True,
                        "filters": []
                    }
                }
            data['actions'] = actions
            self.group.set_data(data)

            self.actions = [ActionWidget(f'Action {i}', group=self.group) for i in range(1, 13)]
            self.actions_container.add(self.actions)
            
    def get_data(self):
        data = {
            'label': self.label.text(),
            **self.group.get_data(),
        }
        return data


class PageList(QListWidget):
    removed = Signal(QWidget)

    def __init__(self, removed, selection_changed):
        super().__init__()

        self.removed.connect(removed)
        self.currentRowChanged.connect(selection_changed)
        self.setEditTriggers(QAbstractItemView.DoubleClicked)

    def contextMenuEvent(self, event):
        selection = self.selectedItems()[0]
        print(selection)
        menu = QMenu()
        # menu.addAction('Rename Page').triggered.connect(lambda:)
        menu.addAction('Rename Page')
        menu.addAction('Remove Page').triggered.connect(lambda: self.remove_page(selection))
        menu.exec_(event.globalPos())

    def remove_page(self, item):
        self.takeItem(self.row(item))
        self.removed.emit(item.page)


class ActionsContainer(StagehandWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, icon_name='mdi.format-list-checkbox', **kwargs)

        self.saving_disabled = True

        self.pages = []
        self.page_stack = QStackedWidget()
        self.page_list = PageList(self.page_removed, self.page_stack.setCurrentIndex)

        self.create_page_btn = QPushButton(icon=qta.icon('mdi.playlist-plus'), clicked=self.create_page)
        self.load()

        call_later(self.enable_saving, 250)

        with PersistentCSplitter('generic_actions/splitter', self, orientation='h', margins=0) as split:
            with CVBoxLayout(split, 1) as layout:
                with layout.hbox(align='r'):
                    layout.add(self.create_page_btn)
                layout.add(self.page_list)
            split.add(self.page_stack, 4)

    def enable_saving(self):
        self.saving_disabled = False

    def create_page(self):
        i = 1

        for page in self.pages:
            if page.name == str(i):
                i += 1

        new_page = ActionsPage(str(i), changed=self.save, data={})
        self.add(new_page)
        self.page_stack.setCurrentWidget(new_page)

    def page_removed(self, page):
        self.pages.remove(page)
        self.save()

    def add(self, page):
        self.page_stack.addWidget(page)
        self.page_list.addItem(page.item)
        self.pages.append(page)

    def load(self):
        data = {}
        try:
            with open('settings.json', 'r') as f:
                data = json.loads(f.read())
        except:
            pass
  
        if 'pages' in data:
            for name, page_data in data['pages'].items():
                page = ActionsPage(name, changed=self.save, data=page_data)
                self.add(page)
        else:
            self.add(ActionsPage('1', changed=self.save, data={}))
            self.add(ActionsPage('2', changed=self.save, data={}))
            self.add(ActionsPage('3', changed=self.save, data={}))

    def save(self):
        if self.saving_disabled:
            return

        data = {
            'pages': {p.name: p.get_data() for p in self.pages},
        }
        
        with open('settings.json', 'w') as f:
            f.write(json.dumps(data, indent=4))
