
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

        self.setScaledContents(True)


        # Initialise the pixmap in resizeEvent
        # resizeEvent is called when initialised so it will run
        self.canvas = None

        # For debugging purposes - shouldn't be visible
        self.setStyleSheet("background-color: green;")

    # I forgot the proper name but this is a feature of QLabel inherited I believe
    def resizeEvent(self, event):
        super().resizeEvent(event)

         # Get the exact size of this widget
        size = self.size()
    
        # Create a pixmap that's EXACTLY the widget size
        self.canvas = QPixmap(size.width(), size.height())
        self.canvas.setDevicePixelRatio(self.devicePixelRatio())
        self.canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(self.canvas)


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

        # Set initial size
        self.resize(800, 600)
        
        # Set minimum size so it can't be made too small
        self.setMinimumSize(400, 300)

def main(): 
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()