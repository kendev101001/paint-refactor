from PyQt6.QtCore import QObject, QPoint


class Controller(QObject):
    """
    Handles user interactions and coordinates between Model and Views.
    
    Responsibilities:
    - Initialize views with values from the model
    - Connect view signals to handlers
    - Update model when user interacts with views
    - Command views to draw/update
    """

    def __init__(self, model, canvas, control_panel):
        super().__init__()
        self._model = model
        self._canvas = canvas
        self._control_panel = control_panel

        # Drawing state (transient, controller-owned)
        self._is_drawing = False
        self._last_point = None

        # Initialize views with model values
        self._initialize_views()
        
        # Connect all signals
        self._connect_canvas_signals()
        self._connect_control_panel_signals()

    def _initialize_views(self):
        """Initialize all views with current model values."""
        # Initialize control panel
        self._control_panel.initialize_colour(self._model.line_colour)
        self._control_panel.initialize_brush_size(
            self._model.min_brush_size,
            self._model.max_brush_size,
            self._model.brush_size
        )
        self._control_panel.initialize_tool(self._model.current_tool)

    def _connect_canvas_signals(self):
        """Connect canvas input signals to handlers."""
        self._canvas.clicked.connect(self._handle_canvas_click)
        self._canvas.mouse_moved.connect(self._handle_mouse_move)
        self._canvas.mouse_released.connect(self._handle_mouse_release)

    def _connect_control_panel_signals(self):
        """Connect control panel signals to handlers."""
        # Without bubbling up, controller would have to do this:
        # self._control_panel._colour_control.colour_changed.connect(self._handle_colour_changed)
        self._control_panel.colour_changed.connect(self._handle_colour_changed)
        self._control_panel.brush_size_changed.connect(self._handle_brush_size_changed)
        self._control_panel.tool_changed.connect(self._handle_tool_changed)
        self._control_panel.clear_requested.connect(self._handle_clear_canvas)

    # ==================== Canvas Event Handlers ====================

    def _handle_canvas_click(self, x: int, y: int):
        """Handle mouse press - start a new stroke."""
        if self._model.current_tool == "freehand":
            self._is_drawing = True
            self._last_point = QPoint(x, y)

            self._canvas.draw_point(
                point=self._last_point,
                colour=self._model.line_colour,
                size=self._model.brush_size
            )

    def _handle_mouse_move(self, x: int, y: int):
        """Handle mouse drag - continue the stroke."""
        if not self._is_drawing or self._last_point is None:
            return

        if self._model.current_tool == "freehand":
            current_point = QPoint(x, y)

            self._canvas.draw_line(
                start_point=self._last_point,
                end_point=current_point,
                colour=self._model.line_colour,
                size=self._model.brush_size
            )

            self._last_point = current_point

    def _handle_mouse_release(self):
        """Handle mouse release - end the stroke."""
        self._is_drawing = False
        self._last_point = None

    # ==================== Control Panel Event Handlers ====================

    def _handle_colour_changed(self, colour):
        """User changed colour via control panel - update model."""
        self._model.line_colour = colour

    def _handle_brush_size_changed(self, size: int):
        """User changed brush size via control panel - update model."""
        self._model.brush_size = size

    def _handle_tool_changed(self, tool_name: str):
        """User changed tool via control panel - update model."""
        self._model.current_tool = tool_name

    def _handle_clear_canvas(self):
        """User requested canvas clear - command canvas to clear."""
        self._canvas.clear()