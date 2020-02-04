from PyQt5 import QtWidgets,QtGui,QtCore

class Ui_MainWindow(QtWidgets.QWidget):
    def on_homebutton_clicked(self):
        message=self.lineEdit.text()
        #self.label.setText(message)
        self.label.setText(self.family.currentText())
        QtWidgets.QMessageBox.information(self,"Message",message)

    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800,600)
        self.centralwidget=QtWidgets.QWidget()

        self.lineEdit=QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10,10,300,40))
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)        
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText("Enter the message")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.on_homebutton_clicked)

        self.label=QtWidgets.QLabel(self.centralwidget)
        self.setStyleSheet("color:blue;""")
        self.label.setGeometry(QtCore.QRect(350,0,300,150))
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.home_button=QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(100,100,100,40))
        self.home_button.setStyleSheet("QPushButton:hover{background-color:red;border-radius:10px;font-size:20px;}""QPushButton{background-color:blue;}")
        self.home_button.setObjectName("home_button")
        self.home_button.setAutoDefault(True)
        self.home_button.clicked.connect(self.on_homebutton_clicked)

        self.family=QtWidgets.QComboBox(self.centralwidget)
        self.family.setGeometry(QtCore.QRect(100,500,150,30))
        self.family.addItem("Father")
        self.family.addItem("Mother")
        self.family.addItem("Brother")
        self.family.addItem("Sister")
        self.family.setObjectName("family")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
    
    def retranslateUi(self,MainWindow):
        _translate=QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Hello"))
        self.home_button.setText(_translate("MainWindow","Home"))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())