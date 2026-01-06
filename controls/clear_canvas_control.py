from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton


class ClearCanvasControl(QWidget):
    """
    Clear canvas button control.
    
    Dumb view - emits signal when clicked, knows nothing about model.
    """

    clear_canvas_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        self.setLayout(layout)

        self._button = QPushButton("Clear Canvas")
        self._button.clicked.connect(self.clear_canvas_requested)
        layout.addWidget(self._button)
        
        layout.addStretch()
        