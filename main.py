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

        # Widgets
        self.resume_button = QPushButton("Resume",self) #self set the parent class
        self.pause_button = QPushButton("Pause",self)
        self.next_button = QPushButton("Next", self)
        self.previous_button = QPushButton("Previous", self)
        self.add_music_button = QPushButton("Add music", self)

        self.positionSlider = QSlider(Qt.Horizontal, self) #Slider is horizontal

        self.playlist = QListWidget(self) # Playlist list

        self.album_cover = QLabel(self)
        self.album_cover.setFixedSize(250,250)

        # VLC init
        self.instance = vlc.Instance() # Factory
        self.music_player = self.instance.media_player_new() # Create a player from VLC factory
        
        self.init_ui()

    

    def init_ui(self):
        self.setWindowTitle("Py Music Player (v0.1)")
        self.resize(700,500)

        main_layout = QHBoxLayout()  # playlist left / control pad right

        # Playlist & Add Music Part
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.add_music_button)
        left_layout.addWidget(self.playlist)

        # ControlPad Part
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.album_cover)
        right_layout.addWidget(self.positionSlider)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.resume_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.next_button)

        right_layout.addLayout(button_layout)

        # Merge two sections into Main Layout
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)


        # Styles

        # Set Text
        self.album_cover.setText("Album Cover")

        # Alignment
        self.album_cover.setAlignment(Qt.AlignCenter)
        self.album_cover.setStyleSheet("""
            border: 2px solid gray;
        """)
        

        self.setLayout(main_layout)

    def add_music(self):
        pass
    def play_music(self):
        pass
    def pause_music(self):
        pass
    def next_music(self):
        pass
    def previous_music(self):
        pass


# How does the window works
if __name__ == "__main__":
    app = QApplication(sys.argv)
    music_app = MusicPlayer()
    music_app.show()
    # If you press the x button, you exit the window.
    sys.exit(app.exec_())