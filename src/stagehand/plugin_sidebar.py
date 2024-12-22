from qtstrap import *
from stagehand.components import StagehandSidebar


class PluginSidebar(StagehandSidebar):
    def __init__(self) -> None:
        super().__init__()

        with CVBoxLayout(self) as layout:
            layout.add(QLabel('sidebar'))
