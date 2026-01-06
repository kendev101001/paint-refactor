
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QColor


class Model(QObject):
    """
    Stores application state for the paint application.
    The model knows nothing about the view or controller.
    """
    
    # Signals emitted when properties change
    line_colour_changed = pyqtSignal(QColor)
    brush_size_changed = pyqtSignal(int)
    tool_changed = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()

        self._line_colour = QColor(0, 0, 0, 255)
        self._min_brush_size = 1
        self._max_brush_size = 20
        self._brush_size = 5  # Current brush size (mutable)
        self._current_tool = "freehand"

    # --- Line Colour ---
    @property
    def line_colour(self):
        return self._line_colour
    
    @line_colour.setter
    def line_colour(self, colour):
        if self._line_colour != colour:
            self._line_colour = QColor(colour)  # Make a copy
            # self.line_colour_changed.emit(self._line_colour)
    
    # --- Brush Size Constraints ---
    @property
    def min_brush_size(self):
        return self._min_brush_size
    
    @property
    def max_brush_size(self):
        return self._max_brush_size
    
    # --- Current Brush Size ---
    @property
    def brush_size(self):
        return self._brush_size
    
    @brush_size.setter
    def brush_size(self, size):
        # Clamp to valid range
        clamped_size = max(self._min_brush_size, min(self._max_brush_size, size))
        if self._brush_size != clamped_size:
            self._brush_size = clamped_size
            # self.brush_size_changed.emit(self._brush_size)

    # --- Current Tool ---
    @property
    def current_tool(self):
        return self._current_tool
    
    @current_tool.setter
    def current_tool(self, tool):
        if self._current_tool != tool:
            self._current_tool = tool
            # self.tool_changed.emit(self._current_tool)
    
    # --- For backwards compatibility ---
    @property
    def init_brush_size(self):
        """Initial/default brush size."""
        return 5