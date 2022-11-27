from qtstrap import *
from qtstrap.extras.command_palette import Command
from .actions import ActionsPage
from stagehand.components import StagehandPage
import json
import qtawesome as qta


default_page_type = 'Generic Actions'


class MainTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        self.setIconSize(QSize(25, 25))

        tab_bar = self.tabBar()
        tab_bar.setContextMenuPolicy(Qt.CustomContextMenu)
        tab_bar.customContextMenuRequested.connect(self.tab_context_menu)

        self.currentChanged.connect(self.save)

        more_pages_button = QPushButton('New Page')
        page_menu = QMenu(more_pages_button)
        more_pages_button.setMenu(page_menu)
        
        for c in StagehandPage.__subclasses__():
            page_menu.addAction(c.page_type).triggered.connect(lambda _=None, p=c: self.create_page(p.page_type))

        corner = QWidget()
        with CHBoxLayout(corner, margins=0) as layout:
            # layout.add(QPushButton(qta.icon('mdi.plus'), '', clicked=self.create_page))
            layout.add(more_pages_button)

        self.setCornerWidget(corner)
        self.saving_disabled = True

        self.setMovable(True)

        self.pages = []
        
        self.load()
        
        call_later(self.enable_saving, 250)

    def tab_context_menu(self, pos:QPoint):
        tab_bar = self.tabBar()
        tab_idx = tab_bar.tabAt(pos)
        page = self.widget(tab_idx)

        menu = QMenu()
        # if hasattr(page, ''):
        menu.addAction('Rename Page').triggered.connect(lambda: self.rename_page(tab_idx))
        menu.addAction('Delete Page').triggered.connect(lambda: self.remove_page(tab_idx))
        menu.exec_(self.mapToGlobal(pos))

    def enable_saving(self):
        self.saving_disabled = False

    def fix_tab_names(self):
        [self.setTabText(i, self.widget(i).get_name()) for i in range(self.count())]

    def rename_page(self, index):
        self.setCurrentIndex(index)
        page = self.widget(index)
        page.label.start_editing()

    def remove_page(self, index):
        page = self.widget(index)
        self.pages.remove(page)
        self.removeTab(index)
        page.deleteLater()
        self.save()

    def create_page(self, page_type=default_page_type):
        i = 1

        for page in self.pages:
            if page.name == str(i):
                i += 1

        page_class = StagehandPage.get_subclasses()[page_type]

        new_page = page_class(str(i), changed=self.save, data={})
        self.add(new_page)
        self.save()

    def page_removed(self, page):
        self.pages.remove(page)
        self.save()

    def add(self, page):
        self.pages.append(page)
        idx = self.addTab(page, page.get_name())
        if hasattr(page, 'icon_name'):
            icon = qta.icon(page.icon_name)
            self.setTabIcon(idx, icon)

    def load(self):
        data = {}
        try:
            with open('settings.json', 'r') as f:
                data = json.loads(f.read())
        except:
            pass
  
        if 'pages' in data:
            for name, page_data in data['pages'].items():
                page_type = page_data.get('page_type', default_page_type)
                page_class = StagehandPage.get_subclasses()[page_type]
                page = page_class(name, changed=self.save, data=page_data)
                self.add(page)
            if 'current_tab' in data:
                self.setCurrentIndex(data['current_tab'])
        else:
            self.add(ActionsPage('1', changed=self.save, data={}))
            self.add(ActionsPage('2', changed=self.save, data={}))
            self.add(ActionsPage('3', changed=self.save, data={}))

    def save(self):
        self.fix_tab_names()

        if self.saving_disabled:
            return

        pages = [self.widget(i) for i in range(self.count())]

        data = {
            'current_tab': self.currentIndex(),
            'pages': {p.name: p.get_data() for p in pages},
        }
        
        with open('settings.json', 'w') as f:
            f.write(json.dumps(data, indent=4))