from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt6.QtCore import Qt, pyqtSignal, QPoint
from PyQt6.QtWidgets import (
    QLabel,
    QScrollArea,
    QWidget,
    QVBoxLayout,
)


class Canvas(QLabel):
    """
    Fixed-size canvas widget for drawing.
    
    The Canvas is a "dumb" view - it:
    - Emits signals for user input (doesn't handle logic)
    - Provides drawing methods that accept explicit parameters
    - Knows nothing about the Model
    """

    # Signals for user input (emitted, not handled here)
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
        
        self.setFixedSize(self._canvas_width, self._canvas_height)
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        # Create pixmap with device pixel ratio for sharp rendering
        pixmap = QPixmap(
            int(self._canvas_width * dpr), 
            int(self._canvas_height * dpr)
        )
        pixmap.setDevicePixelRatio(dpr)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)
        
        self.setStyleSheet("border: 1px solid #888;")

    # ==================== Drawing Methods ====================
    # These are called by the Controller with explicit parameters
    
    def draw_point(self, point, colour, size):
        """
        Draw a single point on the canvas.
        
        Args:
            point: QPoint - location to draw
            colour: QColor - colour of the point
            size: int - diameter of the point
        """
        pixmap = self.pixmap()
        if pixmap is None:
            return
        
        painter = QPainter(pixmap)
        self._configure_painter(painter, colour, size)
        painter.drawPoint(point)
        painter.end()
        
        self.setPixmap(pixmap)
        self.update()

    def draw_line(self, start_point, end_point, colour, size):
        """
        Draw a line between two points on the canvas.
        
        Args:
            start_point: QPoint - start of line
            end_point: QPoint - end of line
            colour: QColor - colour of the line
            size: int - width of the line
        """
        pixmap = self.pixmap()
        if pixmap is None:
            return
        
        painter = QPainter(pixmap)
        self._configure_painter(painter, colour, size)
        painter.drawLine(start_point, end_point)
        painter.end()
        
        self.setPixmap(pixmap)
        self.update()

    def _configure_painter(self, painter, colour, size):
        """Configure painter with common settings."""
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        pen = QPen(colour)
        pen.setWidth(size)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        
        painter.setPen(pen)

    # ==================== Canvas Management ====================

    def get_canvas_size(self):
        """Return the canvas dimensions."""
        return self._canvas_width, self._canvas_height

    def resize_canvas(self, width, height):
        """Resize the canvas to new dimensions."""
        self._canvas_width = width
        self._canvas_height = height
        
        dpr = self.devicePixelRatio()
        old_pixmap = self.pixmap()
        
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

    # ==================== Mouse Event Handlers ====================
    # These just emit signals - logic is in Controller

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
        self._canvas = Canvas(canvas_width, canvas_height)
        
        container = QWidget()
        container.setStyleSheet("background-color: #404040;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._canvas)
        container.setLayout(layout)
        
        self.setWidget(container)
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # # Style the scroll area
        # self.setStyleSheet("""
        #     QScrollArea {
        #         background-color: #404040;
        #         border: none;
        #     }
        # """)

    @property
    def canvas(self):
        """Access the underlying canvas."""
        return self._canvas

    def get_canvas_size(self):
        """Return the canvas dimensions."""
        return self._canvas.get_canvas_size()