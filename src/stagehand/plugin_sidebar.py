from qtstrap import *
from stagehand.components import StagehandSidebar


class PluginSidebar(StagehandSidebar):
    name = 'plugins'
    display_name = 'Plugins'
    icon_name = 'mdi.puzzle'

    def __init__(self) -> None:
        super().__init__()

        with CVBoxLayout(self) as layout:
            layout.add(QLabel('Plugin browser coming soon...'))
            layout.add(QLabel('This is a placeholder sidebar panel.'))
