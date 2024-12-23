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

DEFAULT_RADIUS = 40
DEFAULT_WIDTH = 40

Z_VALUE = 1000

# SIZE = (DEFAULT_RADIUS + DEFAULT_WIDTH + 10) * 2
SIZE = 300


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
    ):
        super().__init__()

        self.start = start
        self.end = end
        self.radius = radius
        self.width = width

        self.icon = icon

        self.normal_bg = QColor(normal_bg or QColor('#676767'))
        self.hover_bg = QColor(hover_bg or QColor('#0078d4'))

        self.build()

        if self.icon:
            self.set_icon(icon)

    def build(self):
        path = ArcPath(self.start, self.end, self.radius, self.width)
        self.item = QGraphicsPathItem(path, self)
        self.item.setBrush(self.normal_bg)

    def set_icon(self, icon: QIcon):
        iconSize = int(sqrt(self.width**2 / 2))
        pixmap = icon.pixmap(iconSize)
        self.icon = QGraphicsPixmapItem(pixmap, self)
        self.icon.setZValue(self.zValue() + 10)
        midAngle = self.start + (self.end - self.start) / 2
        iconPos = QLineF.fromPolar(self.radius + self.width * 0.5, midAngle).p2()
        self.icon.setPos(iconPos)
        self.icon.setOffset(-pixmap.rect().center())

    def hoverEnterEvent(self, event):
        self.setZValue(Z_VALUE + 1)

        self.setScale(1.1)
        self.item.setBrush(self.hover_bg)

    def hoverLeaveEvent(self, event):
        self.setZValue(Z_VALUE)

        self.setScale(1.0)
        self.item.setBrush(self.normal_bg)

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

    def __init__(self, action_names: list[str], bg: QColor = None, hover: QColor = None):
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

        with MenuScene(self) as self.scene:
            # CenterSegment()

            icons = [
                qta.icon('mdi.content-cut', color='white'),
                qta.icon('mdi.content-copy', color='white'),
                qta.icon('mdi.wrench', color='white'),
                qta.icon('mdi.content-paste', color='white'),
            ]

            # for i, angle in enumerate(range(0, 360, 180)):
            #     ArcSegment(
            #         start=angle + 90,
            #         end=angle + 180 + 90,
            #         icon=icons[i],
            #         normal_bg=bg,
            #         hover_bg=hover,
            #     ).clicked(lambda x=action_names[i]: self.button_clicked(x))

            for i, angle in enumerate(range(0, 360, 90)):
                ArcSegment(
                    start=angle + 45,
                    end=angle + 90 + 45,
                    icon=icons[i],
                    normal_bg=bg,
                    hover_bg=hover,
                ).clicked(lambda x=action_names[i]: self.button_clicked(x))

            # for i, angle in enumerate(range(0, 360, 60)):
            #     ArcSegment(
            #         start=angle,
            #         end=angle + 60,
            #         icon=icons[i],
            #         normal_bg=bg,
            #         hover_bg=hover,
            #     ).clicked(lambda x=action_names[i]: self.button_clicked(x))

            # for angle in range(0, 360, 45):
            #     ArcSegment(start=angle + 45, end=angle + 90, radius=80)

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
