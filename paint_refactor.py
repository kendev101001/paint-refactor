import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QLabel,
    QSizePolicy
)
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt

class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        # Make the canvas expand to fill available space
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumSize(100, 100)

        # Initialize with a pixmap
        dpr = self.devicePixelRatio()
        pixmap = QPixmap(int(600 * dpr), int(300 * dpr))
        pixmap.setDevicePixelRatio(dpr)
        pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(pixmap)

    def resizeEvent(self, event):
        new_size = event.size()
        
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
        
        super().resizeEvent(event)


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Expand right")

        self._setup_ui()

    def _setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

        self.canvas = Canvas()
        main_layout.addWidget(self.canvas, stretch=1)

        # Create right panel with fixed width and purple background
        right_panel = QWidget()
        right_panel.setFixedWidth(200)
        right_panel.setStyleSheet("background-color: purple;")
        main_layout.addWidget(right_panel)

        self.setCentralWidget(central_widget)
        self.resize(800, 400)


def main(): 
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()