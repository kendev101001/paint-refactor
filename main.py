import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
)
from views.canvas import Canvas
from models.model import Model
from controllers.controller import Controller

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Microsoft Paint Clone")

        self.model = Model()

        # setup UI
        self._setup_ui()

        # create and connect controls to controller
        self.controller = Controller(self.model, self.canvas)
        self._connect_controls()

    def _setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

        self.canvas = Canvas()
        main_layout.addWidget(self.canvas, stretch=1)

        # Create right panel with fixed width and purple background
        right_panel = QWidget()
        right_panel.setFixedWidth(200)
        right_panel.setStyleSheet("background-color: purple;")
        main_layout.addWidget(right_panel)

        self.setCentralWidget(central_widget)
        self.resize(800, 400)

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