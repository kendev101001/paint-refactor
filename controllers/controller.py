from PyQt6.QtCore import QObject, QPoint


class Controller(QObject):
    """
    Handles user interactions and coordinates between Model and View (Canvas).
    
    - Receives input signals from Canvas
    - Receives input signals from ControlPanel
    - Reads state from Model
    - Commands Canvas to draw
    """
    
    def __init__(self, model, canvas, control_panel=None):
        super().__init__()
        self.model = model
        self.canvas = canvas
        self.control_panel = control_panel
        
        # Drawing state (transient, belongs in controller)
        self._is_drawing = False
        self._last_point = None

        # Connect canvas input signals to handlers
        self.canvas.clicked.connect(self._handle_canvas_click)
        self.canvas.mouse_moved.connect(self._handle_mouse_move)
        self.canvas.mouse_released.connect(self._handle_mouse_release)
        
        # Connect control panel signals if provided
        if self.control_panel:
            self._connect_control_panel()
    
    def _connect_control_panel(self):
        """Connect all control panel signals to their handlers."""
        
        # Colour control
        if hasattr(self.control_panel, 'colour_control'):
            self.control_panel.colour_control.colour_changed.connect(
                self._handle_colour_changed
            )
        
        # Brush size control
        if hasattr(self.control_panel, 'brush_size_control'):
            self.control_panel.brush_size_control.slider_changed.connect(
                self._handle_brush_size_changed
            )
        
        # Clear canvas control
        if hasattr(self.control_panel, 'clear_canvas_control'):
            self.control_panel.clear_canvas_control.clear_canvas_requested.connect(
                self._handle_clear_canvas
            )
        
        # Tool control (for future use)
        if hasattr(self.control_panel, 'tool_control'):
            self.control_panel.tool_control.tool_changed.connect(
                self._handle_tool_changed
            )
    
    # ==================== Drawing Handlers ====================
    
    def _handle_canvas_click(self, x, y):
        """Handle mouse press - start a new stroke."""
        if self.model.current_tool == "freehand":
            self._is_drawing = True
            self._last_point = QPoint(x, y)
            
            # Draw initial point (for single clicks / dots)
            self.canvas.draw_point(
                point=self._last_point,
                colour=self.model.line_colour,
                size=self.model.brush_size
            )
    
    def _handle_mouse_move(self, x, y):
        """Handle mouse drag - continue the stroke."""
        if not self._is_drawing or self._last_point is None:
            return
        
        if self.model.current_tool == "freehand":
            current_point = QPoint(x, y)
            
            # Draw line segment from last position to current
            self.canvas.draw_line(
                start_point=self._last_point,
                end_point=current_point,
                colour=self.model.line_colour,
                size=self.model.brush_size
            )
            
            # Update last point for next segment
            self._last_point = current_point
    
    def _handle_mouse_release(self):
        """Handle mouse release - end the stroke."""
        self._is_drawing = False
        self._last_point = None
    
    # ==================== Control Panel Handlers ====================
    
    def _handle_colour_changed(self, colour):
        """Handle colour change from control panel."""
        self.model.line_colour = colour
        print(f"Colour changed to: {colour.name()}")  # Debug output
    
    def _handle_brush_size_changed(self, size):
        """Handle brush size change from control panel."""
        self.model.brush_size = size
        print(f"Brush size changed to: {size}")  # Debug output
    
    def _handle_clear_canvas(self):
        """Handle clear canvas request from control panel."""
        self.canvas.clear()
        print("Canvas cleared")  # Debug output
    
    def _handle_tool_changed(self, tool_name):
        """Handle tool change from control panel (for future use)."""
        self.model.current_tool = tool_name
        print(f"Tool changed to: {tool_name}")  # Debug output
    
    # ==================== Public API for Programmatic Control ====================
    
    # def set_brush_size(self, size):
    #     """Update brush size programmatically."""
    #     self.model.brush_size = size
    
    # def set_line_colour(self, colour):
    #     """Update line colour programmatically."""
    #     self.model.line_colour = colour
    
    # def clear_canvas(self):
    #     """Clear the entire canvas programmatically."""
    #     self.canvas.clear()
    
    # def get_brush_size(self):
    #     """Get current brush size."""
    #     return self.model.brush_size
    
    # def get_line_colour(self):
    #     """Get current line colour."""
    #     return self.model.line_colour