from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox


class ToolControl(QWidget):
    """
    Tool selection control widget.
    
    Dumb view - emits signals, accepts commands, knows nothing about model.
    """

    tool_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)
        self.setLayout(layout)

        label = QLabel("Tool: ")
        layout.addWidget(label)

        self._combo = QComboBox()
        self._combo.addItems(["freehand", "line", "rectangle", "ellipse"])
        self._combo.currentTextChanged.connect(self._on_tool_changed)
        layout.addWidget(self._combo)
        
        layout.addStretch()

    def _on_tool_changed(self, tool_name: str):
        """Handle tool selection change and emit signal."""
        self.tool_changed.emit(tool_name)

    # ==================== Methods for Controller ====================

    def set_tool(self, tool_name: str):
        """Set the selected tool (called by controller)."""
        # Block signals to prevent feedback loop
        self._combo.blockSignals(True)
        index = self._combo.findText(tool_name)
        if index >= 0:
            self._combo.setCurrentIndex(index)
        self._combo.blockSignals(False)
