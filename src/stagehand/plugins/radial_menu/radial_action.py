from qtstrap import *
from stagehand.actions import ActionWidget


class RadialActionWidget(ActionWidget):
    @classmethod
    def make_default_data(cls, name):
        return {
            'name': name,
            'enabled': True,
            'action': {'type': 'sandbox', 'action': f'print("{name}")'},
            'trigger': {'enabled': False, 'trigger_type': 'sandbox', 'trigger': ''},
            'filter': {'enabled': False, 'filters': []},
        }

    def do_layout(self):
        self.action.label.hide()

        with CHBoxLayout(self, margins=0) as layout:
            layout.add(self.label)
            layout.add(VLine())
            layout.add(self.action, 2)
            layout.add(self.run_btn)

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        menu = QMenu()
        menu.addAction('Run').triggered.connect(self.run)
        menu.addAction('Rename').triggered.connect(self.label.start_editing)
        menu.addAction('Copy').triggered.connect(self.copy)
        menu.addAction('Paste').triggered.connect(self.paste)
        menu.addAction('Reset').triggered.connect(self.reset)
        menu.addAction('Remove').triggered.connect(self.remove)
        menu.exec_(event.globalPos())
