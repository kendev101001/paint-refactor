from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt6.QtCore import Qt, pyqtSignal, QPoint
from PyQt6.QtWidgets import (
    QLabel,
    QScrollArea,
    QWidget,
    QVBoxLayout,
    QSizePolicy,
)


class Canvas(QLabel):
    """Fixed-size canvas widget for drawing."""

    # Signal - for when you have clicked on the canvas
    clicked = pyqtSignal(int, int)
    mouse_moved = pyqtSignal(int, int)
    mouse_released = pyqtSignal()

    def __init__(self, width=800, height=600):
        super().__init__()
        
        self._canvas_width = width
        self._canvas_height = height
        
        self._setup_canvas()

    def _setup_canvas(self):
        """Initialize the canvas with fixed dimensions."""
        dpr = self.devicePixelRatio()
        
        # Set fixed size for the canvas (no expanding)
        self.setFixedSize(self._canvas_width, self._canvas_height)
        
        # Align to top-left
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        # Create pixmap with device pixel ratio for sharp rendering
        pixmap = QPixmap(
            int(self._canvas_width * dpr), 
            int(self._canvas_height * dpr)
        )
        pixmap.setDevicePixelRatio(dpr)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)
        
        # Add border to show canvas boundaries
        self.setStyleSheet("border: 1px solid #888;")

    def get_canvas_size(self):
        """Return the canvas dimensions."""
        return self._canvas_width, self._canvas_height

    def resize_canvas(self, width, height):
        """Resize the canvas to new dimensions."""
        self._canvas_width = width
        self._canvas_height = height
        
        dpr = self.devicePixelRatio()
        old_pixmap = self.pixmap()
        
        # Create new pixmap
        new_pixmap = QPixmap(
            int(width * dpr), 
            int(height * dpr)
        )
        new_pixmap.setDevicePixelRatio(dpr)
        new_pixmap.fill(Qt.GlobalColor.white)
        
        # Preserve existing content
        if old_pixmap and not old_pixmap.isNull():
            painter = QPainter(new_pixmap)
            painter.drawPixmap(0, 0, old_pixmap)
            painter.end()
        
        self.setFixedSize(width, height)
        self.setPixmap(new_pixmap)

    def clear(self):
        """Clear the canvas to white."""
        pixmap = self.pixmap()
        if pixmap:
            pixmap.fill(Qt.GlobalColor.white)
            self.setPixmap(pixmap)
            self.update()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(ev.pos().x(), ev.pos().y())

    def mouseMoveEvent(self, ev):
        if ev.buttons() & Qt.MouseButton.LeftButton:
            self.mouse_moved.emit(ev.pos().x(), ev.pos().y())

    def mouseReleaseEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.mouse_released.emit()


class ScrollableCanvas(QScrollArea):
    """Scrollable container for the canvas, similar to Photoshop behavior."""

    def __init__(self, canvas_width=800, canvas_height=600):
        super().__init__()
        
        self._setup_ui(canvas_width, canvas_height)

    def _setup_ui(self, canvas_width, canvas_height):
        # Create the actual canvas
        self._canvas = Canvas(canvas_width, canvas_height)
        
        # Container widget to center the canvas
        container = QWidget()
        container.setStyleSheet("background-color: #404040;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._canvas)
        container.setLayout(layout)
        
        # Setup scroll area
        self.setWidget(container)
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Style the scroll area
        self.setStyleSheet("""
            QScrollArea {
                background-color: #404040;
                border: none;
            }
        """)

    @property
    def canvas(self):
        """Access the underlying canvas."""
        return self._canvas

    def get_canvas_size(self):
        """Return the canvas dimensions."""
        return self._canvas.get_canvas_size()