
from PyQt6.QtCore import QObject

class Controller(QObject):
    def __init__(self, model, canvas):
        super().__init__()
        self.model = model
        self.canvas = canvas

        # connect canvas clicks to model
        self.canvas.clicked.connect(self._handle_canvas_click)
    
    def _handle_canvas_click(self, x, y):
        pass