from dataclasses import dataclass
from math import sqrt

import qtawesome as qta
from qtpy.QtCore import QLineF, QPoint, QRectF, Qt, Signal
from qtpy.QtGui import QColor, QCursor, QIcon, QPainter, QPainterPath, QRegion, QVector2D
from qtpy.QtWidgets import (
    QDialog,
    QGraphicsObject,
    QGraphicsPathItem,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
)


SIZE = (40 + 40) * 2


class BaseGraphicsObject(QGraphicsObject):
    def __init__(self):
        super().__init__()

        self.setAcceptHoverEvents(True)
        self.setPos(SIZE // 2, SIZE // 2)
        self.setZValue(1000)

        self.setBoundingRegionGranularity(1)

        if MenuScene.active_scene:
            MenuScene.active_scene.addItem(self)

    def boundingRect(self):
        return self.childrenBoundingRect()

    def paint(self, *_):
        pass


class CenterSegment(BaseGraphicsObject):
    clicked = Signal()

    def __init__(self, radius=40):
        super().__init__()

        startRect = QRectF(-radius, -radius, radius * 2, radius * 2)

        self.path = QPainterPath()
        self.path.moveTo(QLineF.fromPolar(radius, 0).p2())
        self.path.arcTo(startRect, 0, 360)
        self.path.closeSubpath()

        self.item = QGraphicsPathItem(self.path, self)
        self.item.setPen(QColor(Qt.GlobalColor.black))
        self.item.setBrush(QColor(255, 255, 255))

    def hoverEnterEvent(self, event):
        pass

    def hoverLeaveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        self.clicked.emit()


@dataclass
class SegmentColors:
    bg: QColor


class ArcSegment(BaseGraphicsObject):
    clicked = Signal()

    def __init__(self, start: int, end: int, radius=40, width=40, icon: QIcon = None):
        super().__init__()

        # self.normal_bg
        # self.hover_bg
        # self.normal_outline
        # self.hover_outline

        startRect = QRectF(-radius, -radius, radius * 2, radius * 2)
        outer = radius + width
        endRect = QRectF(-outer, -outer, outer * 2, outer * 2)

        self.path = QPainterPath()
        self.path.moveTo(QLineF.fromPolar(outer, start).p2())
        self.path.arcTo(endRect, start, (end - start))
        self.path.lineTo(QLineF.fromPolar(radius, end).p2())
        self.path.arcTo(startRect, end, -(end - start))
        self.path.closeSubpath()

        self.item = QGraphicsPathItem(self.path, self)

        self.set_normal_colors()

        if icon is not None:
            iconSize = int(sqrt(width**2 / 2))
            pixmap = icon.pixmap(iconSize)
            iconItem = QGraphicsPixmapItem(pixmap, self)
            iconItem.setZValue(self.zValue() + 1)
            midAngle = start + (end - start) / 2
            iconPos = QLineF.fromPolar(radius + width * 0.5, midAngle).p2()
            iconItem.setPos(iconPos)
            iconItem.setOffset(-pixmap.rect().center())

    def set_normal_colors(self):
        self.item.setPen(QColor(Qt.GlobalColor.black))
        self.item.setBrush(QColor(180, 140, 70))

    def set_hover_colors(self):
        self.item.setPen(QColor(Qt.GlobalColor.red))
        self.item.setBrush(QColor(Qt.GlobalColor.white))

    def hoverEnterEvent(self, event):
        self.set_hover_colors()

    def hoverLeaveEvent(self, event):
        self.set_normal_colors()

    # def hoverMoveEvent(self, event):
    #     if self.item.shape().contains(event.pos()):
    #         self.set_hover_colors()
    #     else:
    #         self.set_normal_colors()

    def mousePressEvent(self, event):
        self.clicked.emit()


class MenuScene(QGraphicsScene):
    active_scene: QGraphicsScene = None

    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setSceneRect(0, 0, SIZE, SIZE)

        self.view = QGraphicsView(self, parent)
        self.view.setRenderHints(QPainter.RenderHint.Antialiasing)

    def __enter__(self):
        MenuScene.active_scene = self
        return self

    def __exit__(self, *_):
        MenuScene.active_scene = None


class RadialPopup(QDialog):
    buttonClicked = Signal(object)

    def __init__(self, action_names: list[str], bg=None):
        super().__init__()
        self.setModal(True)

        region = QRegion(0, 0, SIZE, SIZE, QRegion.RegionType.Ellipse)
        self.setMask(region)

        # self.setStyleSheet('background:transparent;')
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Window
            # | Qt.WindowType.Tool
            # | Qt.WindowType.Popup
            | Qt.WindowType.NoDropShadowWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        with MenuScene(self) as self.scene:
            CenterSegment()

            for i, angle in enumerate(range(0, 360, 60)):
                ArcSegment(
                    start=angle,
                    end=angle + 60,
                    icon=qta.icon('fa.list', color='gray'),
                ).clicked(lambda x=action_names[i]: self.button_clicked(x))

            # for angle in range(0, 180, 45):
            #     ArcSegment(start=angle, end=angle + 45)
            # ArcSegment(start=180, end=360)

            # for angle in range(0, 360, 90):
            #     ArcSegment(start=angle + 45, end=angle + 135, radius=80)

        self.move_to_cursor()

    def leaveEvent(self, event):
        pos = QCursor().pos()

        radius = SIZE // 2

        vec = QVector2D(self.origin - pos)
        norm = vec.normalized() * (radius - 5)
        norm.setX(-norm.x())
        norm.setY(-norm.y())

        QCursor().setPos(self.origin + norm.toPoint())

        event.accept()
        return super().leaveEvent(event)

    def move_to_cursor(self):
        self.origin = QCursor().pos()
        x = self.origin.x() - SIZE // 2
        y = self.origin.y() - SIZE // 2
        self.setGeometry(x, y, SIZE, SIZE)

    def button_clicked(self, id):
        self.buttonClicked.emit(id)
        self.accept()
