from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def login(self):
        username=self.lineEdit1.text()
        password=self.lineEdit2.text()
        print(username)
        print(password)
    def show(self):
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Normal)
    def hide(self):
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background:orange;")

        self.labellogin=QtWidgets.QLabel(self.centralwidget)
        self.labellogin.setText("Login Window")
        self.labellogin.setStyleSheet("color:blue;\n""font-size:20px;\n""font-family:Consolas;\n")
        self.labellogin.setGeometry(340,100,200,30)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 360, 101, 31))
        self.pushButton.setStyleSheet("font-size:20px;\n""font-family:\"Consolas\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(340, 209, 181, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1.setStyleSheet("background:white;\n""font-family:Consolas;\n""font-size:16px;")
        self.lineEdit1.returnPressed.connect(self.login)

        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(340, 260, 181, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setStyleSheet("background:white;\n""font-family:Consolas;\n""font-size:16px;")
        self.lineEdit2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit2.returnPressed.connect(self.login)

        self.pushButton2=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(522,260,101,31))
        self.pushButton2.setText("Show")
        self.pushButton2.clicked.connect(self.show)        
        self.pushButton2.setStyleSheet("font-size:20px;\n""font-family:Consolas;")
       

        self.pushButton3=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(624,260,101,31))
        self.pushButton3.setText("Hide")
        self.pushButton3.clicked.connect(self.hide)       
        self.pushButton3.setStyleSheet("font-size:20px;\n""font-family:Consolas;")
        


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
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    a=QtWidgets
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
