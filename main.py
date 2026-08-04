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
        self.play_button = QPushButton("Play",self)
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
        
        self.init_ui() # apply the layout

        # Connect Signals
        self.add_music_button.clicked.connect(self.add_music)
        self.play_button.clicked.connect(self.play_music)
        self.pause_button.clicked.connect(self.pause_music)
        self.next_button.clicked.connect(self.next_music)
        self.previous_button.clicked.connect(self.previous_music)

        # State variables
        self.music_files = []
        self.current_index = -1
        self.is_paused = False


    

    def init_ui(self):
        self.setWindowTitle("Py Music Player (v0.2)")
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
        button_layout.addWidget(self.play_button)
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

        
    # Each function for the widget
    def add_music(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Music",
            "",
            "AudioFiles (*.mp3 *.wav *.flac)"
        )

        if not files:
            return
        for file in files:
            self.music_files.append(file)
            self.playlist.addItem(os.path.basename(file)) # Add song in the playlist widget

        

    def play_music(self):
            # if the song was paused state, resume the song we play.
        if self.is_paused:
            self.music_player.play()
            self.is_paused = False
        else:

            if not self.music_files:
                return

            # set the first song to play
            if self.current_index == -1:
                self.current_index = 0


            # Load the song to play
            song = self.music_files[self.current_index]

            # Insert the song in the player
            media = self.instance.media_new(song)
            self.music_player.set_media(media)

            self.music_player.play()
            print(f"Now playing : {os.path.basename(song)}")
        
        
    def pause_music(self):
        self.music_player.pause()
        self.is_paused = True

    def next_music(self):
        if not self.music_files:
            return
        self.current_index += 1
        
        if self.current_index >= len(self.music_files):
            self.current_index = 0 # Return to the first song

        self.playlist.setCurrentRow(self.current_index) # Show the next song
        self.is_paused = False
        self.play_music()
        
    def previous_music(self):
        if not self.music_files:
            return
        self.current_index -= 1

        if self.current_index < 0:
            self.current_index = 0
        self.playlist.setCurrentRow(self.current_index) # Show the next song
        self.is_paused = False
        self.play_music()


# How does the window works
if __name__ == "__main__":
    app = QApplication(sys.argv)
    music_app = MusicPlayer()
    music_app.show()
    # If you press the x button, you exit the window.
    sys.exit(app.exec_())