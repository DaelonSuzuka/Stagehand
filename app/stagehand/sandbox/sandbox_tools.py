from qtstrap import *


class SandboxTools(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.output = QTextEdit(readOnly=True)
        self.clear_output = QPushButton('Clear', clicked=self.output.clear)

        with CVBoxLayout(self, margins=2) as layout:
            with layout.hbox(margins=0) as layout:
                layout.add(QLabel(), 1)
                layout.add(self.clear_output)
            layout.add(self.output)

    def print(self, *args):
        scrollbar = self.output.verticalScrollBar()
        at_bottom = False
        if scrollbar.value() == scrollbar.maximum():
            at_bottom = True
        
        s = ''
        for arg in args:
            s += str(arg)

        if t := self.output.toPlainText():
            s = t + '\n' + s

        out = '\n'.join(l for l in s.split('\n') if l)
        self.output.setPlainText(out)
        
        if at_bottom:
            scrollbar.setValue(scrollbar.maximum())


class SandboxToolsDockWidget(QDockWidget):
    def __init__(self, widget: QWidget):
        super().__init__('Sandbox Output')
        self.setObjectName('SandboxOutput')

        self.setWidget(widget)
        self.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        self.starting_area = Qt.RightDockWidgetArea
        self.closeEvent = lambda x: self.hide()

    def toggleViewAction(self):
        action = super().toggleViewAction()
        action.setShortcut('Ctrl+T')
        return action