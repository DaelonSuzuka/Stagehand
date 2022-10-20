from stagehand.components import StagehandWidget, SidebarButton
from monaco import MonacoWidget
import qtawesome as qta
from qtstrap import *
from qtpy.QtQuick import QQuickWindow, QSGRendererInterface


QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
QQuickWindow.setGraphicsApi(QSGRendererInterface.OpenGLRhi)


class MonacoExample(StagehandWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.sidebar_button = SidebarButton(target=self, icon=qta.icon('mdi.text'))

        self.monaco = MonacoWidget(self)

        with CVBoxLayout(self) as layout:
            layout.add(self.monaco)