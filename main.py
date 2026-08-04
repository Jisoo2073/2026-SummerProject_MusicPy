import sys
import os
import vlc

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget)


# New Window
class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Py Music Player (v0.1)")
        self.resize(500,500)

# How does the window works
if __name__ == "__main__":
    app = QApplication(sys.argv)
    music_app = MusicPlayer()
    music_app.show()
    # If you press the x button, you exit the window.
    sys.exit(app.exec_())