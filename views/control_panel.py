
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from controls import (
    ColourControl,
    SliderControl,
    ToolControl,
    ClearCanvasControl
)


class ControlPanel(QWidget):
    """Control panel widget containing all drawing controls."""

    def __init__(self, model):
        super().__init__()
        self._model = model
        self._setup_ui()

    def _setup_ui(self):
        self.setFixedWidth(200)
        self.setStyleSheet("background-color: grey;")

        # Control layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Colour control
        self.colour_control = ColourControl(self._model.line_colour)
        layout.addWidget(self.colour_control)

        # Brush size control
        self.brush_size_control = SliderControl(
            "Brush Size",
            self._model.min_brush_size,
            self._model.max_brush_size,
            self._model.init_brush_size
        )
        layout.addWidget(self.brush_size_control)

        # Tool control
        self.tool_control = ToolControl()
        layout.addWidget(self.tool_control)

        # Clear canvas control
        self.clear_canvas_control = ClearCanvasControl()
        layout.addWidget(self.clear_canvas_control)

        layout.addStretch()