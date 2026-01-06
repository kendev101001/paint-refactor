from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSlider
from PyQt6.QtCore import Qt


class SliderControl(QWidget):
    """
    Slider control widget with label.
    
    Dumb view - emits signals, accepts commands, knows nothing about model.
    """

    slider_changed = pyqtSignal(int)

    def __init__(self, label_text: str):
        super().__init__()
        
        self._label_text = label_text
        
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        self.setLayout(layout)

        self._label = QLabel(f"{self._label_text}: ")
        layout.addWidget(self._label)

        self._slider = QSlider(Qt.Orientation.Horizontal)
        self._slider.valueChanged.connect(self._on_slider_changed)
        layout.addWidget(self._slider)

        self._value_label = QLabel("0")
        self._value_label.setFixedWidth(30)
        layout.addWidget(self._value_label)

    def _on_slider_changed(self, value: int):
        """Handle slider value change and emit signal."""
        self._value_label.setText(str(value))
        self.slider_changed.emit(value)

    # ==================== Methods for Controller ====================

    def set_range(self, min_val: int, max_val: int):
        """Set the slider range (called by controller during initialization)."""
        self._slider.setMinimum(min_val)
        self._slider.setMaximum(max_val)

    def set_value(self, value: int):
        """Set the slider value (called by controller)."""
        # Block signals to prevent feedback loop when controller sets value
        self._slider.blockSignals(True)
        self._slider.setValue(value)
        self._value_label.setText(str(value))
        self._slider.blockSignals(False)