from PyQt5 import QtWidgets,QtGui,QtCore
from secondwindow import *

class Ui_FirstWindow(QtWidgets.QWidget):
    def setupUi(self,FirstWindow,SecondWindow):
        self.window=FirstWindow
        self.next_window=SecondWindow
        FirstWindow.setFixedSize(400,400)
        self.centralwidget=QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.change_window=QtWidgets.QPushButton(self.centralwidget)
        self.change_window.setGeometry(QtCore.QRect(0,0,100,40))
        self.change_window.clicked.connect(self.change)
        FirstWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(FirstWindow)
    
    def change(self):
        self.window.close()
        self.next_window.show()

    def retranslateUi(self,FirstWindow):
        _translate=QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow","First Window"))
        self.change_window.setText(_translate("FirstWindow","goto second"))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)

    SecondWindow=QtWidgets.QMainWindow()
    ui_second=Ui_SecondWindow()
    ui_second.setupUi(SecondWindow)

    FirstWindow=QtWidgets.QMainWindow()
    ui=Ui_FirstWindow()
    ui.setupUi(FirstWindow,SecondWindow)
    FirstWindow.show()
    

    sys.exit(app.exec_())