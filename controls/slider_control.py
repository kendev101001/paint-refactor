
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSlider
 
class SliderControl(QWidget):
    """Generic slider control widget"""

    slider_changed = pyqtSignal(int)

    def __init__(self, label_prefix, min_val, max_val, init_val):
        super().__init__()
        self._label_prefix = label_prefix                           # Stored because it always needs to be accessed when slider is changed
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
        self._slider.setMinimum(min_val)
        self._slider.setMaximum(max_val)
        self._slider.setValue(init_val)
        self._slider.valueChanged.connect(self._on_value_changed)
        layout.addWidget(self._slider)
        layout.addStretch()

    def _on_value_changed(self, value):
        self._label.setText(f"{self._label_prefix}: {value}")
        self.slider_changed.emit(value)