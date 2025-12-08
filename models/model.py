
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColor


class Model(QObject):
    def __init__(self):
        super().__init__()

        self._line_colour = QColor(255, 255, 255, 255)

    @property
    def line_colour(self):
        return self._line_colour