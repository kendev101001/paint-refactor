import sys
from views import Canvas
from models import Model
from controllers.controller import Controller
from controls.colour_control import ColourControl
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Microsoft Paint Clone")

        self._model = Model()

        # setup UI
        self._setup_ui()

        # create and connect controls to controller
        self._controller = Controller(self._model, self._canvas)
        self._connect_controls()

    def _setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)
        
        # Main drawing canvas
        self._canvas = Canvas()
        main_layout.addWidget(self._canvas, stretch=1)
        
        # Control panel
        control_panel = self._create_control_panel()
        main_layout.addWidget(control_panel)

        self.setCentralWidget(central_widget)
        self.resize(800, 400)

    def _create_control_panel(self):
        control_panel = QWidget()
        control_panel.setFixedWidth(200)
        control_panel.setStyleSheet("background-color: purple;")

        # control layout
        control_layout = QVBoxLayout()
        control_layout.setContentsMargins(0, 0, 0, 0)
        control_layout.setSpacing(0)
        control_panel.setLayout(control_layout)

        self._colour_control = ColourControl(self._model.line_colour)
        control_layout.addWidget(self._colour_control)
        
        control_layout.addStretch()  # Optional: pushes controls to top

        return control_panel  # THIS WAS MISSING

    def _connect_controls(self):
        # Add in control stuff later
        pass


def main(): 
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()