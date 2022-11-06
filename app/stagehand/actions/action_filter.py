from qtstrap import *
import abc
import qtawesome as qta
import json
from stagehand.sandbox import Sandbox


class FilterStackItem:
    @classmethod
    def get_subclasses(cls):
        return {c.name: c for c in cls.__subclasses__()}

    @classmethod
    def get_item(cls, name):
        return cls.get_subclasses()[name]

    @abc.abstractmethod
    def __init__(self, changed) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def set_data(self, data: dict) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self) -> dict:
        raise NotImplementedError

    def reset(self) -> None:
        pass

    @abc.abstractmethod
    def check(self) -> bool:
        raise NotImplementedError


class SandboxFilterWidget(QWidget, FilterStackItem):
    name = 'sandbox'

    def __init__(self, changed, owner=None) -> None:
        super().__init__()

        self.owner = owner
        self.filter = QLineEdit()
        self.filter.textChanged.connect(changed)
        
        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.filter)

    def check(self) -> bool:
        Sandbox().eval(self.filter.text())
        return True

    def set_data(self, data: dict) -> None:
        self.filter.setText(data['filter'])

    def get_data(self) -> dict:
        return {
            'filter': self.filter.text()
        }


class FilterStack(QWidget):
    changed = Signal()

    def __init__(self, changed=lambda: ..., filter_type='sandbox', filter='', owner=None) -> None:
        super().__init__()

        self.owner = owner
        self.type = QComboBox()
        self.stack = QStackedWidget()
        self.remove = QPushButton('X', clicked=self.on_remove)

        self.pls_delete = False
        
        for name, filt in FilterStackItem.get_subclasses().items():
            self.type.addItem(name)
            self.stack.addWidget(filt(changed, owner=owner))

        self.type.currentIndexChanged.connect(changed)
        self.type.currentIndexChanged.connect(self.stack.setCurrentIndex)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.type)
            layout.add(self.stack)
            layout.add(self.remove)

    def check(self):
        return self.stack.currentWidget().check()

    def on_remove(self):
        self.type.setVisible(False)
        self.stack.setVisible(False)
        self.remove.setVisible(False)
        self.pls_delete = True

    def set_data(self, data):
        if 'filter_type' not in data:
            data['filter_type'] = 'sandbox'

        self.type.setCurrentText(data['filter_type'])
        self.stack.currentWidget().set_data(data)

    def get_data(self):
        return {
            'filter_type': self.type.currentText(),
            **self.stack.currentWidget().get_data(),
        }


class ActionFilterDialog(QDialog):
    def __init__(self, filters, owner=None):
        super().__init__()
        self.setWindowTitle("Filter Editor")
        
        self.owner = owner
        self.filters = filters

        self.add_btn = QPushButton('New Filter', clicked=self.on_add)
        self.cancel_btn = QPushButton('Cancel', clicked=self.reject)
        self.ok_btn = QPushButton('Ok', clicked=self.accept)

        self.filter_box = CVBoxLayout(align='top')

        with CVBoxLayout(self) as layout:
            with layout.hbox(align='right') as layout:
                layout.add(self.add_btn)
            layout.add(HLine())
            layout.add(self.filter_box)
            layout.add(QLabel(), 1)

            layout.add(HLine())
            with layout.hbox(align='right') as layout:
                layout.add(self.cancel_btn)
                layout.add(self.ok_btn)

    def on_add(self):
        filt = FilterStack()
        self.filters.append(filt)
        self.filter_box.add(filt)

    def set_data(self, data):
        self.setWindowTitle(f"{data['label']} - Filter Editor")


class ActionFilter(QWidget):
    changed = Signal()

    def __init__(self, changed, owner=None):
        super().__init__()

        self.owner = owner
        self.changed.connect(changed)

        self.filters = []

        self.enabled = QAction('Filter Enabled', self, triggered=changed, checkable=True)
        self.open_btn = QPushButton('', clicked=self.open_editor, icon=qta.icon('mdi.filter-menu-outline'), parent=self)
        self.number_of_filters = QLabel('0')

        self.editor = ActionFilterDialog(self.filters, owner)
        self.editor.accepted.connect(self.on_accept)

        with CHBoxLayout(self, margins=(0,0,0,0)) as layout:
            layout.add(self.open_btn)
            layout.add(self.number_of_filters)
            layout.add(VLine())

    def open_editor(self, *_):
        self.data['filter'] = self.get_data()['filter']
        self.editor.set_data(self.data)

        if self.filters == []:
            self.filters.append(FilterStack())

        for f in self.filters:
            self.editor.filter_box.add(f)

        self.editor.open()

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction(QAction('Copy Filters', self, triggered=self.copy))
        menu.addAction(QAction('Paste Filters', self, triggered=self.paste))
        menu.addAction(QAction('Reset Filters', self, triggered=self.reset))
        menu.exec_(event.globalPos())

    def copy(self):
        data = json.dumps(self.get_data())
        QClipboard().setText(data)

    def paste(self):
        data = json.loads(QClipboard().text())
        self.set_data(data)

    def reset(self):
        self.filters = []
        self.number_of_filters.setText('0')

    def on_accept(self):
        filts = [f for f in self.filters if not f.pls_delete]
        self.number_of_filters.setText(str(len(filts)))
        self.changed.emit()

        delete = []
        for f in self.filters:
            if f.pls_delete:
                delete.append(f)

        for f in delete:
            self.filters.remove(f)
            f.deleteLater()

    def check_filters(self) -> bool:
        if not self.enabled.isChecked():
            return True
        return all([f.check() for f in self.filters])

    def set_data(self, data):
        if 'label' in data:
            self.data = data
            self.editor.set_data(data)

        if 'filter' in data:
            if 'enabled' in data['filter']:
                self.enabled.setChecked(data['filter']['enabled'])

            self.filters.clear()
            for f in data['filter']['filters']:
                filt = FilterStack()
                filt.set_data(f)
                self.filters.append(filt)

        self.number_of_filters.setText(str(len(self.filters)))

    def get_data(self):
        return {
            'filter': {
                'enabled': self.enabled.isChecked(),
                'filters': [f.get_data() for f in self.filters if not f.pls_delete],
            }
        }