import sys
from views import ScrollableCanvas, ControlPanel, CanvasSizeDialog
from models import Model
from controllers import Controller
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
)

class MainWindow(QMainWindow):

    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.setWindowTitle("Microsoft Paint Clone")

        self._canvas_width = canvas_width
        self._canvas_height = canvas_height
        self._model = Model()

        # Setup UI
        self._setup_ui()

        # Create and connect controls to controller
        self._controller = Controller(self._model, self._scrollable_canvas.canvas)

        # Connect control panel to controller
        self._control_panel.colour_control.colour_changed.connect(
            self._controller.set_color
        )
        self._control_panel.brush_size_control.slider_changed.connect(
            self._controller.set_brush_size
        )
        self._control_panel.clear_canvas_control.clear_canvas_requested.connect(
            self._controller.clear_canvas
        )
        self._control_panel.tool_control.tool_changed.connect(
            self._controller.set_tool
        )

    def _setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

        # Main drawing canvas (scrollable container)
        self._scrollable_canvas = ScrollableCanvas(
            self._canvas_width, 
            self._canvas_height
        )
        main_layout.addWidget(self._scrollable_canvas, stretch=1)

        # Control panel
        self._control_panel = ControlPanel(self._model)
        main_layout.addWidget(self._control_panel)

        self.setCentralWidget(central_widget)
        
        # Set window size based on canvas size (with some padding)
        window_width = min(self._canvas_width + 250, 1400)
        window_height = min(self._canvas_height + 100, 900)
        self.resize(window_width, window_height)

    @property
    def canvas(self):
        """Access the drawing canvas."""
        return self._scrollable_canvas.canvas


def main():
    app = QApplication(sys.argv)

    # Show canvas size dialog first
    width, height, accepted = CanvasSizeDialog.get_canvas_size()
    
    if not accepted:
        # User cancelled, exit the application
        sys.exit(0)

    # Create main window with selected canvas size
    window = MainWindow(width, height)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()