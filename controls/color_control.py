
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtSignal

class ColorControl(QWidget):

    color_changed = pyqtSignal(QColor)

    def __init__(self, initial_color):
        super().__init__()

        self._current_color = initial_color

        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        
        # Text description for control
        label = QLabel("Line Colour: ")
        layout.addWidget(label)

        #...

