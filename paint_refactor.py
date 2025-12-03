
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QLabel
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        canvas = QPixmap(600, 300)
        canvas.setDevicePixelRatio(self.devicePixelRatio())
        canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(canvas)
        # self.setMouseTracking(True)


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

        # Add stretch to push right panel to the right
        # main_layout.addStretch()

        canvas = Canvas()
        main_layout.addWidget(canvas, stretch=1)

        # Create right panel with fixed width and purple background
        right_panel = QWidget()
        right_panel.setFixedWidth(200)
        right_panel.setStyleSheet("background-color: purple;")
        main_layout.addWidget(right_panel)

        self.setCentralWidget(central_widget)

        self.adjustSize()
        # self.setFixedSize(self.size())

def main(): 
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()