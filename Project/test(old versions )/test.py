
from PyQt5 import QtCore,QtGui,QtWidgets
def Ui_Hello(object):
    def setupUi(self,w):
        pass
    pass
 
if __name__ == '__main__':
     import sys
     app = QtWidgets.QApplication(sys.argv)
     w = QtWidgets.QMainWindow()
     w.setGeometry(0,0,1350,690)
     
     def Labeltest():
         l.setText("Button pushed")
     def exiting():
         w.exit()
     def background():
         w.setStyleSheet("background:orange;")
     def clear():
         l.setText("")
     def revert1():
         w.setStyleSheet("")
     

     l=QtWidgets.QLabel(w)
     l.setText("")
     l.setGeometry(0,650,500,30)
     font=QtGui.QFont()
     font.setPointSize(20)
     font.setFamily("MV Boli")
     l.setFont(font)
     l.setStyleSheet("color:blue;")

     d=QtWidgets.QPushButton(w)
     d.setText("Push")
     d.clicked.connect(Labeltest)
     d.setGeometry(0,600,101,41)

     s=QtWidgets.QPushButton(w)
     s.setText("Clear")
     s.clicked.connect(clear)
     s.setGeometry(670,600,101,41)


     changeBackground=QtWidgets.QPushButton(w)
     changeBackground.setGeometry(0,500,350,30)
     changeBackground.setText("Change background")
     font=QtGui.QFont()
     font.setFamily("Consolas")
     font.setPointSize(16)
     changeBackground.setFont(font)
     changeBackground.setStyleSheet("color:blue;\n""background:red;")
     changeBackground.clicked.connect(background)
     
     revert=QtWidgets.QPushButton(w)
     revert.setGeometry(370,500,350,30)
     revert.setText("Revert to original")
     font=QtGui.QFont()
     font.setFamily("Consolas")
     font.setPointSize(16)
     revert.setStyleSheet("color:blue;\n""background:red;")
     revert.setFont(font)
     revert.clicked.connect(revert1)

     exitwindow=QtWidgets.QPushButton(w)
     exitwindow.clicked.connect(exiting)
     exitwindow.setText("Exit")
     exitwindow.setGeometry(1250,650,101,41)

     
     

     w.setWindowTitle("Hello")
     w.show()
     sys.exit(app.exec_())
