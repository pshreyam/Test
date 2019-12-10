from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def resetfx(self):
        self.lcdNumber=0
        self.lcdNumber_3=0
        self.lcdNumber.display
        self.lcdNumber_3.display
        print (self.lcdNumber.text())
        print (self.lcdNumber_3.text())
        
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setWindowOpacity(200.0)
        mainWindow.setStyleSheet("background:magneta;\n"
"color:yellow;")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(260, 250, 131, 121))
        self.dial.setStyleSheet("background:magneta;\n"
"color:yellow;")
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(190, 160, 141, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 60, 121, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(24)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(450, 160, 131, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 160, 47, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 160, 47, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(490, 250, 131, 121))
        self.dial_2.setStyleSheet("background:magneta;\n"
"color:yellow;")
        self.dial_2.setObjectName("dial_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 125, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 126, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 440, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:red;\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 440, 161, 51))
        self.pushButton_2.clicked.connect(self.resetfx)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:red;\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")        
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.dial.sliderMoved['int'].connect(self.lcdNumber.display)
        self.dial_2.sliderMoved['int'].connect(self.lcdNumber_3.display)
        self.pushButton.clicked.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Volume regulator"))
        self.label.setText(_translate("mainWindow", "Volume"))
        self.label_2.setText(_translate("mainWindow", "%"))
        self.label_3.setText(_translate("mainWindow", "%"))
        self.label_4.setText(_translate("mainWindow", " Media"))
        self.label_5.setText(_translate("mainWindow", "System"))
        self.pushButton.setText(_translate("mainWindow", "Exit"))
        self.pushButton_2.setText(_translate("mainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
