# Learnt from online tutorial

import sys
from os import environ

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (
		QApplication, QFileDialog, QPushButton, 
		QHBoxLayout, QSlider, QVBoxLayout, QWidget, QStatusBar
)
        
def suppress_qt_warnings():
    """
    Suppresses Qt Warnings
    """
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    

class VideoPlayer(QWidget):

    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()
        videoWidget.setStyleSheet("background-color: black;")

        openButton = QPushButton(" Open Video")   
        openButton.setToolTip("Choose Video")
        openButton.setStatusTip("Choose Video")
        openButton.setFixedHeight(30)
        openButton.setStyleSheet("border: 2px solid black; border-radius: 6px; padding: 2px;")
        openButton.setIconSize(btnSize)
        openButton.setFont(QFont("Sans Serif", 10))
        openButton.setIcon(QIcon('icon.png'))
        openButton.clicked.connect(self.open_file)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(30)
        self.playButton.setStyleSheet("border-radius: 50%;")
        self.playButton.setIconSize(btnSize)
        self.playButton.setIcon(QIcon('play.png'))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setStyleSheet("color: #E69A8DFF;")
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Sans Serif", 10))
        self.statusBar.setFixedHeight(16)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.statusBar.showMessage("Player is ready...")

    def open_file(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Video",
                ".", "Video Files (*.mp4 *.flv *.avi *.wmv)")

        if fileName:
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName.split('/')[-1])
            self.play()

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
               QIcon('pause.png')
            )
        else:
            self.playButton.setIcon(
                QIcon('play.png')
            )

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())

if __name__ == '__main__':
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.setWindowIcon(QIcon('icon.png'))
    player.setStyleSheet("background-color: #FC766AFF;")
    player.setMouseTracking(True)
    player.setWindowTitle("Video Player")
    player.resize(800, 700)
    player.show()
    sys.exit(app.exec())
