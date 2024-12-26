from dataclasses import dataclass
from math import sqrt

from qtpy.QtCore import QEasingCurve, QLineF, QPointF, QPropertyAnimation, QRectF, Qt, Signal
from qtpy.QtGui import QColor, QCursor, QIcon, QPainter, QPainterPath, QRegion, QVector2D
from qtpy.QtWidgets import (
    QDialog,
    QGraphicsObject,
    QGraphicsPathItem,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
)

DEFAULT_RADIUS = 40
DEFAULT_WIDTH = 40

Z_VALUE = 1000

# SIZE = (DEFAULT_RADIUS + DEFAULT_WIDTH + 10) * 2
SIZE = 600
CENTER = QPointF(SIZE // 2, SIZE // 2)


class BaseGraphicsObject(QGraphicsObject):
    clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setAcceptHoverEvents(True)
        self.setPos(SIZE // 2, SIZE // 2)
        self.setZValue(Z_VALUE)

        self.setBoundingRegionGranularity(0.8)

        if MenuScene.active_scene:
            MenuScene.active_scene.addItem(self)

    def boundingRect(self):
        return self.childrenBoundingRect()

    def paint(self, *_):
        pass

    def mousePressEvent(self, event):
        self.clicked.emit()


class CenterSegment(BaseGraphicsObject):
    def __init__(self, radius=DEFAULT_RADIUS):
        super().__init__()

        startRect = QRectF(-radius, -radius, radius * 2, radius * 2)

        path = QPainterPath()
        path.moveTo(QLineF.fromPolar(radius, 0).p2())
        path.arcTo(startRect, 0, 360)
        path.closeSubpath()

        self.item = QGraphicsPathItem(path, self)
        # self.item.setPen(QColor(Qt.GlobalColor.black))
        self.item.setBrush(QColor(255, 255, 255, 1))

    def hoverEnterEvent(self, event):
        pass

    def hoverLeaveEvent(self, event):
        pass

    def contextMenuEvent(self, event):
        return super().contextMenuEvent(event)


@dataclass
class ArcSize:
    start: int
    end: int
    radius: int
    width: int


@dataclass
class SegmentColors:
    bg: QColor


class ArcPath(QPainterPath):
    def __init__(self, start: int, end: int, radius: int, width: int):
        super().__init__()

        start_rect = QRectF(-radius, -radius, radius * 2, radius * 2)
        outer = radius + width
        end_rect = QRectF(-outer, -outer, outer * 2, outer * 2)

        self.moveTo(QLineF.fromPolar(radius + width, start).p2())
        self.arcTo(end_rect, start, (end - start))
        self.lineTo(QLineF.fromPolar(radius, end).p2())
        self.arcTo(start_rect, end, -(end - start))
        self.closeSubpath()


class ArcSegment(BaseGraphicsObject):
    def __init__(
        self,
        start: int,
        end: int,
        radius=DEFAULT_RADIUS,
        width=DEFAULT_WIDTH,
        icon: QIcon = None,
        normal_bg: QColor = None,
        hover_bg: QColor = None,
        normal_outline: QColor = None,
        hover_outline: QColor = None,
    ):
        super().__init__()
        # dimensions
        self.start = start
        self.end = end
        self.radius = radius
        self.width = width

        self.icon = icon

        # colors
        self.normal_bg = QColor(normal_bg or QColor('#676767'))
        self.hover_bg = QColor(hover_bg or QColor('#0078d4'))
        self.normal_outline = QColor(normal_outline or QColor(0, 0, 0, 0))
        self.hover_outline = QColor(hover_outline or QColor(255, 255, 255))

        # behavior
        self.offset = QPointF()
        if False:
            # fix the center point
            path = ArcPath(self.start, self.end, self.radius, self.width)
            self.offset = path.boundingRect().center()
            self.setPos(CENTER + self.offset)

        self.scale_anim = QPropertyAnimation(self, b'scale', duration=100)
        self.scale_anim.setEasingCurve(QEasingCurve.Type.OutQuad)

        self.build()

    def build(self):
        path = ArcPath(self.start, self.end, self.radius, self.width)
        path.translate(-self.offset)
        self.item = QGraphicsPathItem(path, self)
        self.item.setPen(self.normal_outline)
        self.item.setBrush(self.normal_bg)

        if self.icon:
            self.build_icon()

    def build_icon(self):
        icon_size = int(sqrt(self.width**2 / 2))
        pixmap = self.icon.pixmap(icon_size)
        self.icon_pixmap = QGraphicsPixmapItem(pixmap, self)
        self.icon_pixmap.setZValue(self.zValue() + 10)
        mid_angle = self.start + (self.end - self.start) / 2
        iconPos = QLineF.fromPolar(self.radius + self.width * 0.5, mid_angle).p2()
        self.icon_pixmap.setPos(iconPos - self.offset)
        self.icon_pixmap.setOffset(-pixmap.rect().center())

    def scale_to(self, scale: float):
        self.scale_anim.stop()
        self.scale_anim.setStartValue(self.scale())
        self.scale_anim.setEndValue(scale)
        self.scale_anim.start()

    def hoverEnterEvent(self, event):
        self.setZValue(Z_VALUE + 1)
        self.scale_to(1.1)

        self.item.setBrush(self.hover_bg)
        self.item.setPen(self.hover_outline)

    def hoverLeaveEvent(self, event):
        self.setZValue(Z_VALUE)
        self.scale_to(1.0)

        self.item.setBrush(self.normal_bg)
        self.item.setPen(self.normal_outline)

    # def hoverMoveEvent(self, event):
    #     if self.item.shape().contains(event.pos()):
    #         self.set_hover_colors()
    #     else:
    #         self.set_normal_colors()

    def contextMenuEvent(self, event):
        return super().contextMenuEvent(event)


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

    def __init__(self):
        super().__init__()
        self.setModal(True)

        region = QRegion(0, 0, SIZE, SIZE, QRegion.RegionType.Ellipse)
        self.setMask(region)

        self.setStyleSheet('background:transparent;')
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Window
            # | Qt.WindowType.Tool
            # | Qt.WindowType.Popup
            | Qt.WindowType.NoDropShadowWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.capture_cursor = False

        self.move_to_cursor()

    def leaveEvent(self, event):
        if self.capture_cursor:
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
