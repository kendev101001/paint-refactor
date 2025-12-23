
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColor


class Model(QObject):
    def __init__(self):
        super().__init__()

        self._line_colour = QColor(0, 0, 0, 255)
        self._min_brush_size = 1
        self._max_brush_size = 20
        self._init_brush_size = 5
        self._current_brush_size = 5 # Do I really need this, can I just change init to just brush size and change that
        self._current_tool = "freehand" # Again, this doesn't have init, and neither does line colour, so do I really need init and current?
        # No setters and getters for these. Why? (Too many function calls - unnecessary??)
        self._is_drawing = False # Why no Setter and Getter for this variable??
        self._last_point = None # And with this as well?

    @property
    def current_brush_size(self):
        return self._current_brush_size
    
    @current_brush_size.setter
    def current_brush_size(self, value):
        self._current_brush_size = value

    @property
    def current_tool(self):
        return self._current_tool
    
    @current_tool.setter
    def current_tool(self, value):
        self._current_tool = value

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