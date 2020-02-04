from PyQt5 import QtWidgets,QtGui,QtCore

class Ui_SecondWindow(QtWidgets.QWidget):
    def change(self):
        self.Window.hide()
                
    def setupUi(self,SecondWindow):
        self.Window=SecondWindow
        SecondWindow.setFixedSize(400,400)
        SecondWindow.setObjectName("SecondWindow")
        self.centralwidget=QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.change_window=QtWidgets.QPushButton(self.centralwidget)
        self.change_window.setGeometry(QtCore.QRect(0,0,100,40))
        self.change_window.clicked.connect(self.change)
        SecondWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(SecondWindow)

    def retranslateUi(self,SecondWindow):
        _translate=QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow","Second Window"))
        self.change_window.setText(_translate("SecondWindow","goto first"))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    SecondWindow=QtWidgets.QMainWindow()
    ui=Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())