
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColor


class Model(QObject):
    def __init__(self):
        super().__init__()

        self._line_colour = QColor(0, 0, 0, 255)
        self._min_brush_size = 1
        self._max_brush_size = 20
        self._init_brush_size = 5

    @property
    def line_colour(self):
        return self._line_colour
    
    @property
    def min_brush_size(self):
        return self._min_brush_size
    
    @property
    def max_brush_size(self):
        return self._max_brush_size
    
    @property
    def init_brush_size(self):
        return self._init_brush_size