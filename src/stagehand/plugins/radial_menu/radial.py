from math import sqrt

from qtpy import QtCore, QtGui, QtWidgets


class RadialMenu(QtWidgets.QGraphicsObject):
    buttonClicked = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptHoverEvents(True)
        self.buttons = {}

    def addButton(self, id, innerRadius, size, startAngle, angleSize, icon=None):
        # if a button already exists with the same id, remove it
        if id in self.buttons:
            oldItem = self.buttons.pop(id)
            if self.scene():
                self.scene().removeItem(oldItem)
            oldItem.setParent(None)

        # compute the extents of the inner and outer "circles"
        startRect = QtCore.QRectF(-innerRadius, -innerRadius, innerRadius * 2, innerRadius * 2)
        outerRadius = innerRadius + size
        endRect = QtCore.QRectF(-outerRadius, -outerRadius, outerRadius * 2, outerRadius * 2)

        center_path = QtGui.QPainterPath()
        center_path.moveTo(QtCore.QLineF.fromPolar(innerRadius, 0).p2())
        center_path.arcTo(startRect, 0, 360)
        center_path.closeSubpath()

        self.center = QtWidgets.QGraphicsPathItem(center_path, self)
        self.center.setPen(QtGui.QColor(QtCore.Qt.black))
        self.center.setBrush(QtGui.QColor(QtGui.QColor(255, 255, 255, 1)))

        # create the circle section path
        path = QtGui.QPainterPath()
        # move to the start angle, using the outer circle
        path.moveTo(QtCore.QLineF.fromPolar(outerRadius, startAngle).p2())
        # draw the arc to the end of the angle size
        path.arcTo(endRect, startAngle, angleSize)
        # draw a line that connects to the inner circle
        path.lineTo(QtCore.QLineF.fromPolar(innerRadius, startAngle + angleSize).p2())
        # draw the inner circle arc back to the start angle
        path.arcTo(startRect, startAngle + angleSize, -angleSize)
        # close the path back to the starting position; theoretically unnecessary,
        # but better safe than sorry
        path.closeSubpath()

        # create a child item for the "arc"
        item = QtWidgets.QGraphicsPathItem(path, self)
        item.setPen(QtGui.QColor(QtCore.Qt.black))
        item.setBrush(QtGui.QColor(180, 140, 70))
        self.buttons[id] = item

        if icon is not None:
            # the maximum available size is at 45 degrees, use the Pythagorean
            # theorem to compute it and create a new pixmap based on the icon
            iconSize = int(sqrt(size**2 / 2))
            pixmap = icon.pixmap(iconSize)
            # create the child icon (pixmap) item
            iconItem = QtWidgets.QGraphicsPixmapItem(pixmap, self)
            # push it above the "arc" item
            iconItem.setZValue(item.zValue() + 1)
            # find the mid of the angle and put the icon there
            midAngle = startAngle + angleSize / 2
            iconPos = QtCore.QLineF.fromPolar(innerRadius + size * 0.5, midAngle).p2()
            iconItem.setPos(iconPos)
            # use the center of the pixmap as the offset for centering
            iconItem.setOffset(-pixmap.rect().center())

    def itemAtPos(self, pos):
        for button in self.buttons.values():
            if button.shape().contains(pos):
                return button

    def checkHover(self, pos):
        hoverButton = self.itemAtPos(pos)
        for button in self.buttons.values():
            if button == hoverButton:
                button.setPen(QtGui.QColor(QtCore.Qt.red))
                button.setBrush(QtGui.QColor(QtCore.Qt.white))
            else:
                button.setPen(QtGui.QColor(QtCore.Qt.black))
                button.setBrush(QtGui.QColor(180, 140, 70))

    def hoverEnterEvent(self, event):
        self.checkHover(event.pos())

    def hoverMoveEvent(self, event):
        self.checkHover(event.pos())

    def hoverLeaveEvent(self, event):
        for button in self.buttons.values():
            button.setPen(QtGui.QColor(QtCore.Qt.black))

    def mousePressEvent(self, event):
        clickButton = self.itemAtPos(event.pos())
        if clickButton:
            for id, btn in self.buttons.items():
                if btn == clickButton:
                    event.accept()
                    self.buttonClicked.emit(id)
                    return

        if self.center.shape().contains(event.pos()):
            event.accept()
            self.buttonClicked.emit('center')
            return

        event.accept()
        self.buttonClicked.emit(None)

    def boundingRect(self):
        return self.childrenBoundingRect()

    def paint(self, qp, option, widget):
        # required for QGraphicsObject subclasses
        pass


class RadialPopup(QtWidgets.QDialog):
    buttonClicked = QtCore.Signal(object)

    def __init__(self, action_names: list[str]):
        super().__init__()
        self.setModal(True)

        self.setStyleSheet('background:transparent;')
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint
            | QtCore.Qt.WindowType.Window
            # | QtCore.Qt.WindowType.Tool
            # | QtCore.Qt.WindowType.Popup
            # | QtCore.Qt.WindowType.NoDropShadowWindowHint
            | QtCore.Qt.WindowType.WindowStaysOnTopHint
        )

        self.size = 300

        menu = RadialMenu()
        menu.buttonClicked.connect(self.button_clicked)

        for index, angle in enumerate(range(0, 360, 60)):
            menu.addButton(action_names[index], 40, 40, angle, 60)

        menu.setPos(self.size // 2, self.size // 2)
        menu.setZValue(1000)

        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.addItem(menu)
        self.scene.setSceneRect(0, 0, self.size, self.size)

        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.setRenderHints(QtGui.QPainter.Antialiasing)

        self.move_to_cursor()

    def move_to_cursor(self):
        pos = QtGui.QCursor().pos()
        x = pos.x() - self.size // 2
        y = pos.y() - self.size // 2
        self.setGeometry(x, y, self.size, self.size)

    def button_clicked(self, id):
        print(f'Button id {id} has been clicked')
        self.buttonClicked.emit(id)
        self.accept()
