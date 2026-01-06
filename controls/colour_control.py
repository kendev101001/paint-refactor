from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QColorDialog


class ColourControl(QWidget):
    """
    Colour picker control widget.
    
    Dumb view - emits signals, accepts commands, knows nothing about model.
    """

    colour_changed = pyqtSignal(QColor)

    def __init__(self):
        super().__init__()
        
        # Default colour until controller initializes
        self._current_colour = QColor(0, 0, 0)
        
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        
        label = QLabel("Line Colour: ")
        layout.addWidget(label)

        self._colour_button = QPushButton()
        self._colour_button.setFixedSize(30, 20)
        self._update_button_colour()
        self._colour_button.clicked.connect(self._choose_colour)
        layout.addWidget(self._colour_button)
        layout.addStretch()
    
    def _update_button_colour(self):
        """Update button appearance to show current colour."""
        self._colour_button.setStyleSheet(
            f"background-color: {self._current_colour.name()};"
        )

    def _choose_colour(self):
        """Open colour dialog and emit signal if user selects a colour."""
        colour = QColorDialog.getColor(
            self._current_colour, 
            self, 
            "Choose Line Color"
        )
        if colour.isValid():
            self._current_colour = colour
            self._update_button_colour()
            self.colour_changed.emit(colour)

    # ==================== Methods for Controller ====================

    def set_colour(self, colour: QColor):
        """Set the current colour (called by controller)."""
        self._current_colour = QColor(colour)
        self._update_button_colour()