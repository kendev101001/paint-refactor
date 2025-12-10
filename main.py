import sys
from views import Canvas, ScrollableCanvas, ControlPanel, CanvasSizeDialog
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
        # self._connect_controls()

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

    # def _connect_controls(self):
    #     # Connect colour control
    #     self._control_panel.colour_control.colour_changed.connect(
    #         self._controller.set_line_colour
    #     )
        
    #     # Connect brush size control
    #     self._control_panel.brush_size_control.value_changed.connect(
    #         self._controller.set_brush_size
    #     )
        
    #     # Connect tool control
    #     self._control_panel.tool_control.tool_changed.connect(
    #         self._controller.set_tool
    #     )
        
    #     # Connect clear canvas control
    #     self._control_panel.clear_canvas_control.clear_clicked.connect(
    #         self._controller.clear_canvas
    #     )

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