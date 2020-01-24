from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def reset(self):
        self.label1.clear()
        self.label.clear()
    def wishme(self):
        self.label1.setText("Happy Birthday Shreyam.")
        pixmap = QPixmap('birthday.png')
        self.label.setPixmap(pixmap)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 390, 541, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)                
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:blue;\n""border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.wishme)
                
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 80, 180, 200))
        self.label.setStyleSheet("")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label"
                                 )
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(300, 80, 450, 200))
        self.label1.setStyleSheet("")
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")


        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(350, 540, 100, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24) 
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("background:blue;\n""border-radius:20px;")
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.clicked.connect(self.reset)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Happy Birthday"))
        self.pushButton.setText(_translate("MainWindow", "Wish me Happy Birthday!"))
        self.pushButton1.setText(_translate("MainWindow", "Reset"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
