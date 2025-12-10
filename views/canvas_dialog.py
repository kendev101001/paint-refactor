from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QPushButton,
    QGroupBox,
    QComboBox
)
from PyQt6.QtCore import Qt


class CanvasSizeDialog(QDialog):
    """Dialog for selecting canvas dimensions before creating a new canvas."""

    # Common preset sizes
    PRESETS = {
        "Custom": (0, 0),
        "Small (640x480)": (640, 480),
        "Medium (800x600)": (800, 600),
        "Large (1024x768)": (1024, 768),
        "HD (1280x720)": (1280, 720),
        "Full HD (1920x1080)": (1920, 1080),
        "Square Small (512x512)": (512, 512),
        "Square Medium (1024x1024)": (1024, 1024),
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self._width = 800
        self._height = 600
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("New Canvas")
        self.setModal(True)
        self.setFixedSize(300, 250)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Preset selection
        preset_group = QGroupBox("Presets")
        preset_layout = QVBoxLayout()
        preset_group.setLayout(preset_layout)

        self._preset_combo = QComboBox()
        self._preset_combo.addItems(self.PRESETS.keys())
        self._preset_combo.setCurrentText("Medium (800x600)")
        self._preset_combo.currentTextChanged.connect(self._on_preset_changed)
        preset_layout.addWidget(self._preset_combo)

        layout.addWidget(preset_group)

        # Dimensions group
        dimensions_group = QGroupBox("Dimensions (pixels)")
        dimensions_layout = QVBoxLayout()
        dimensions_group.setLayout(dimensions_layout)

        # Width input
        width_layout = QHBoxLayout()
        width_label = QLabel("Width:")
        width_label.setFixedWidth(50)
        self._width_spinbox = QSpinBox()
        self._width_spinbox.setRange(1, 10000)
        self._width_spinbox.setValue(self._width)
        self._width_spinbox.setSuffix(" px")
        self._width_spinbox.valueChanged.connect(self._on_dimension_changed)
        width_layout.addWidget(width_label)
        width_layout.addWidget(self._width_spinbox)
        dimensions_layout.addLayout(width_layout)

        # Height input
        height_layout = QHBoxLayout()
        height_label = QLabel("Height:")
        height_label.setFixedWidth(50)
        self._height_spinbox = QSpinBox()
        self._height_spinbox.setRange(1, 10000)
        self._height_spinbox.setValue(self._height)
        self._height_spinbox.setSuffix(" px")
        self._height_spinbox.valueChanged.connect(self._on_dimension_changed)
        height_layout.addWidget(height_label)
        height_layout.addWidget(self._height_spinbox)
        dimensions_layout.addLayout(height_layout)

        layout.addWidget(dimensions_group)

        # Buttons
        button_layout = QHBoxLayout()
        
        self._create_button = QPushButton("Create")
        self._create_button.setDefault(True)
        self._create_button.clicked.connect(self.accept)
        
        self._cancel_button = QPushButton("Cancel")
        self._cancel_button.clicked.connect(self.reject)
        
        button_layout.addStretch()
        button_layout.addWidget(self._create_button)
        button_layout.addWidget(self._cancel_button)

        layout.addStretch()
        layout.addLayout(button_layout)

    def _on_preset_changed(self, preset_name):
        """Handle preset selection change."""
        if preset_name != "Custom":
            width, height = self.PRESETS[preset_name]
            self._width_spinbox.blockSignals(True)
            self._height_spinbox.blockSignals(True)
            self._width_spinbox.setValue(width)
            self._height_spinbox.setValue(height)
            self._width_spinbox.blockSignals(False)
            self._height_spinbox.blockSignals(False)

    def _on_dimension_changed(self):
        """Handle manual dimension change."""
        self._preset_combo.blockSignals(True)
        self._preset_combo.setCurrentText("Custom")
        self._preset_combo.blockSignals(False)

    def get_dimensions(self):
        """Return the selected canvas dimensions."""
        return self._width_spinbox.value(), self._height_spinbox.value()

    @staticmethod
    def get_canvas_size(parent=None):
        """
        Static method to show dialog and return dimensions.
        Returns (width, height, accepted) tuple.
        """
        dialog = CanvasSizeDialog(parent)
        result = dialog.exec()
        if result == QDialog.DialogCode.Accepted:
            width, height = dialog.get_dimensions()
            return width, height, True
        return 0, 0, False