#!/usr/bin/python
from qtstrap import *
from NodeGraphQt import BaseNode


def draw_triangle_port(painter, rect, info):
    """
    Custom paint function for drawing a Triangle shaped port.

    Args:
        painter (QPainter): painter object.
        rect (QRectF): port rect used to describe parameters
                              needed to draw.
        info (dict): information describing the ports current state.
            {
                'port_type': 'in',
                'color': (0, 0, 0),
                'border_color': (255, 255, 255),
                'multi_connection': False,
                'connected': False,
                'hovered': False,
            }
    """
    painter.save()

    size = int(rect.height() / 2)
    triangle = QPolygonF()
    triangle.append(QPointF(-size, size))
    triangle.append(QPointF(0.0, -size))
    triangle.append(QPointF(size, size))

    transform = QTransform()
    transform.translate(rect.center().x(), rect.center().y())
    port_poly = transform.map(triangle)

    # mouse over port color.
    if info['hovered']:
        color = QColor(14, 45, 59)
        border_color = QColor(136, 255, 35)
    # port connected color.
    elif info['connected']:
        color = QColor(195, 60, 60)
        border_color = QColor(200, 130, 70)
    # default port color
    else:
        color = QColor(*info['color'])
        border_color = QColor(*info['border_color'])

    pen = QPen(border_color, 1.8)
    pen.setJoinStyle(Qt.MiterJoin)

    painter.setPen(pen)
    painter.setBrush(color)
    painter.drawPolygon(port_poly)

    painter.restore()


def draw_square_port(painter, rect, info):
    """
    Custom paint function for drawing a Square shaped port.

    Args:
        painter (QPainter): painter object.
        rect (QRectF): port rect used to describe parameters
                              needed to draw.
        info (dict): information describing the ports current state.
            {
                'port_type': 'in',
                'color': (0, 0, 0),
                'border_color': (255, 255, 255),
                'multi_connection': False,
                'connected': False,
                'hovered': False,
            }
    """
    painter.save()

    # mouse over port color.
    if info['hovered']:
        color = QColor(14, 45, 59)
        border_color = QColor(136, 255, 35, 255)
    # port connected color.
    elif info['connected']:
        color = QColor(195, 60, 60)
        border_color = QColor(200, 130, 70)
    # default port color
    else:
        color = QColor(*info['color'])
        border_color = QColor(*info['border_color'])

    pen = QPen(border_color, 1.8)
    pen.setJoinStyle(Qt.MiterJoin)

    painter.setPen(pen)
    painter.setBrush(color)
    painter.drawRect(rect)

    painter.restore()


class CustomPortsNode(BaseNode):
    """
    example test node with custom shaped ports.
    """

    # set a unique node identifier.
    __identifier__ = 'nodes.custom.ports'

    # set the initial default node name.
    NODE_NAME = 'node'

    def __init__(self):
        super().__init__()

        # create input and output port.
        self.add_input('in', color=(200, 10, 0))
        self.add_output('default')
        self.add_output('square', painter_func=draw_square_port)
        self.add_output('triangle', painter_func=draw_triangle_port)
