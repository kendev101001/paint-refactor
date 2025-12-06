
from PyQt6.QtWidgets import (
    QLabel,
    QSizePolicy,
)

from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt, pyqtSignal
class Canvas(QLabel):

    # Signal - for when you have clicked on the canvas
    clicked = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()

        dpr = self.devicePixelRatio()

        # Make the canvas expand to fill available space
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(int(600 * dpr), int(400 * dpr))

        # Initialize with a pixmap
        pixmap = QPixmap(int(600 * dpr), int(300 * dpr))
        pixmap.setDevicePixelRatio(dpr)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)

    def resizeEvent(self, ev):
        """Called when window is resized (and on start up)"""
        super().resizeEvent(ev)
        self._update_display(ev)

    def _update_display(self, ev):
        """Redraw the canvas"""
        new_size = ev.size()
        
        if new_size.width() > 0 and new_size.height() > 0:
            old_pixmap = self.pixmap()
            dpr = self.devicePixelRatio()
            
            # Create new pixmap with new dimensions
            new_pixmap = QPixmap(int(new_size.width() * dpr), int(new_size.height() * dpr))
            new_pixmap.setDevicePixelRatio(dpr)
            new_pixmap.fill(Qt.GlobalColor.white)
            
            # Preserve existing content (important for a paint app)
            if old_pixmap and not old_pixmap.isNull():
                painter = QPainter(new_pixmap)
                painter.drawPixmap(0, 0, old_pixmap)
                painter.end()
            
            self.setPixmap(new_pixmap)
    
    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(ev.pos().x(), ev.pos().y())