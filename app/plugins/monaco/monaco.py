from qtstrap import *
from stagehand.components import StagehandPage
from monaco import MonacoWidget


from qtpy.QtQuick import QQuickWindow, QSGRendererInterface
QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
QQuickWindow.setGraphicsApi(QSGRendererInterface.OpenGLRhi)


class MonacoExample(StagehandPage):
    page_type = 'Monaco Notes'
    changed = Signal()
    
    def __init__(self, name='', changed=None, data=None):
        super().__init__()
        self.name = name
        self.icon_name = 'mdi.text'

        if changed:
            self.changed.connect(changed)

        self.label = LabelEdit(f'Monaco {name}', changed=self.changed)
        self.monaco = MonacoWidget(self)

        with CVBoxLayout(self) as layout:
            layout.add(self.label)
            layout.add(self.monaco, 1)
        
    def get_name(self):
        return self.label.text()

    def set_data(self, data):
        self.label.setText(data.get('name', self.name))

    def get_data(self):
        data = {
            'page_type': self.page_type,
            'name': self.label.text(),
        }
        return data