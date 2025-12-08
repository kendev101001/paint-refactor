
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSlider
 
class BrushSizeControl(QWidget):

    slider_changed = pyqtSignal(int)

    def __init__(self, label_prefix, min_val, max_val, init_val):
        super().__init__()
        self._label_prefix = label_prefix
        self._setup_ui(min_val, max_val, init_val)
    
    def _setup_ui(self, min_val, max_val, init_val):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Text description for control
        self._label = QLabel(f"{self._label_prefix}: {init_val}")
        layout.addWidget(self._label)

        # slider control
        self._slider = QSlider(Qt.Orientation.Horizontal)