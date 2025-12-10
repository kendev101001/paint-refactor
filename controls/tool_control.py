
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox

class ToolControl(QWidget):
    def __init__(self):
        super().__init__()

        self._tool_options = [
            "freehand",
            "line",
            "rectangle",
            "circle"
        ]

        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        label = QLabel("Select Tool")
        layout.addWidget(label)

        combobox = QComboBox()
        combobox.addItems(self._tool_options)
        layout.addWidget(combobox)

        layout.addStretch()
