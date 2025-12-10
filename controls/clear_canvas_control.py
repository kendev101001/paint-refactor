
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class ClearCanvasControl(QWidget):

    clear_canvas_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        delete_button = QPushButton("Clear Canvas")
        delete_button.clicked.connect(self.clear_canvas_requested.emit)
        
        layout.addWidget(delete_button)
        