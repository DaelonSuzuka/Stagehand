from qtstrap import *
from stagehand.components import StagehandWidget
from monaco import MonacoWidget
from qtpy.QtQuick import QQuickWindow, QSGRendererInterface


QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
QQuickWindow.setGraphicsApi(QSGRendererInterface.OpenGLRhi)


class MonacoExample(StagehandWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, icon_name='mdi.text', **kwargs)

        self.monaco = MonacoWidget(self)

        with CVBoxLayout(self) as layout:
            layout.add(self.monaco)