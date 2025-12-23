
from PyQt6.QtCore import QObject, QPoint

class Controller(QObject):
    def __init__(self, model, canvas):
        super().__init__()
        self.model = model
        self.canvas = canvas

        # connect canvas clicks to controller
        self.canvas.clicked.connect(self._handle_mouse_press)
        self.canvas.mouse_moved.connect(self._handle_mouse_move)
        self.canvas.mouse_released.connect(self._handle_mouse_release)
    
    def _handle_mouse_press(self, x, y):
        """Start Drawing"""
        if self.model.current_tool == "freehand":
            self.model._is_drawing = True
            # Should it not be QPointF??
            self.model._last_point = QPoint(x, y)

            self.canvas.draw_line(x, y, x, y, 
                                  self.model.line_colour,
                                  self.model.current_brush_size
            )

    def _handle_mouse_move(self, x, y):
        """Continue drawing"""
        if self.model._is_drawing and self.model.current_tool == "freehand":
            if self.model._last_point:
                # Draw a line from the last point to the current point
                self.canvas.draw_line(
                    self.model._last_point.x(),
                    self.model._last_point.y(),
                    x, y,
                    self.model.line_colour,
                    self.model.current_brush_size
                )
                self.model._last_point = QPoint(x, y)
    
    def _handle_mouse_release(self):
        """Stop drawing"""
        self.model._is_drawing = False
        self.model._last_point = None

    def set_brush_size(self, size):
        """Update brush size in model"""
        self.model.current_brush_size = size
    
    def set_color(self, color):
        """Update color in model"""
        self.model.line_colour = color
    
    def set_tool(self, tool):
        """Update current tool in model"""
        self.model.current_tool = tool
    
    def clear_canvas(self):
        """Clear the canvas"""
        self.canvas.clear()