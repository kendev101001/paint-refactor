

from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QColorDialog

class ColourControl(QWidget):

    colour_changed = pyqtSignal(QColor)

    def __init__(self, initial_color):
        super().__init__()

        self._current_colour = initial_color

        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        
        # Text description for control
        label = QLabel("Line Colour: ")
        layout.addWidget(label)

        # Colour control button
        self._colour_button = QPushButton()
        self._colour_button.setFixedSize(20, 20)
        self._update_button_colour()
        self._colour_button.clicked.connect(self._choose_color)
        layout.addWidget(self._colour_button)
        layout.addStretch()
    
    def _update_button_colour(self):
        self._colour_button.setStyleSheet(
            f"background-color: {self._current_colour.name()};"
        )

    def _choose_color(self):
        colour = QColorDialog.getColor(self._current_colour, self, "Choose Line Color")
        if colour.isValid():
            self._current_colour = colour
            self._update_button_colour()
            self.colour_changed.emit(colour)


