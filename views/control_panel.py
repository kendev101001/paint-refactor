from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtSignal
from controls import (
    ColourControl,
    SliderControl,
    ToolControl,
    ClearCanvasControl
)


class ControlPanel(QWidget):
    """
    Control panel widget containing all drawing controls.
    
    This is a "dumb" view - it:
    - Emits signals for user input
    - Provides methods for the controller to initialize and update state
    - Knows nothing about the Model
    """
    
    # Signals emitted when user interacts with controls
    # These are what is used for bubbling up as these same signals are emitted from the controls too
    colour_changed = pyqtSignal(QColor)
    brush_size_changed = pyqtSignal(int)
    tool_changed = pyqtSignal(str)
    clear_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.setFixedWidth(200)
        self.setStyleSheet("background-color: grey;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Create controls with default/placeholder values
        # Controller will initialize them properly
        self._colour_control = ColourControl()
        layout.addWidget(self._colour_control)

        self._brush_size_control = SliderControl("Brush Size")
        layout.addWidget(self._brush_size_control)

        self._tool_control = ToolControl()
        layout.addWidget(self._tool_control)

        self._clear_canvas_control = ClearCanvasControl()
        layout.addWidget(self._clear_canvas_control)

        layout.addStretch()

        # Connect child signals to our own signals
        self._connect_internal_signals()

    def _connect_internal_signals(self):
        """
        Bubble up signals from child controls.
        - Means that controller doesn't need to access the actual controls
        - Just the signals emitted by the controls
        """
        self._colour_control.colour_changed.connect(self.colour_changed)
        self._brush_size_control.slider_changed.connect(self.brush_size_changed)
        self._tool_control.tool_changed.connect(self.tool_changed)
        self._clear_canvas_control.clear_canvas_requested.connect(self.clear_requested)

    # ==================== Initialization Methods (called by Controller) ====================

    def initialize_colour(self, colour: QColor):
        """Initialize the colour control with a value."""
        self._colour_control.set_colour(colour)

    def initialize_brush_size(self, min_val: int, max_val: int, current_val: int):
        """Initialize the brush size slider with range and value."""
        self._brush_size_control.set_range(min_val, max_val)
        self._brush_size_control.set_value(current_val)

    def initialize_tool(self, tool_name: str):
        """Initialize the selected tool."""
        self._tool_control.set_tool(tool_name)

    # ==================== Update Methods (called by Controller if needed) ====================

    def set_colour(self, colour: QColor):
        """Update the displayed colour."""
        self._colour_control.set_colour(colour)

    def set_brush_size(self, size: int):
        """Update the displayed brush size."""
        self._brush_size_control.set_value(size)

    def set_tool(self, tool_name: str):
        """Update the selected tool."""
        self._tool_control.set_tool(tool_name)