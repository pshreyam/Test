from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
import MySQLdb as mdb 
 
class Window(QDialog):
    def __init__(self):
        super().__init__()
 
        self.title = "PyQt5 Insert Data"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 100
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
 
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
 
        vbox = QVBoxLayout()
 
        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Please Enter Your Name')
        self.name.setStyleSheet('background:yellow')
        self.name.setFont(QtGui.QFont("Sanserif", 15))
 
        vbox.addWidget(self.name)
 
        self.email = QLineEdit(self)
        self.email.setPlaceholderText('Please Enter Your Email')
        self.email.setFont(QtGui.QFont("Sanserif", 15))
        self.email.setStyleSheet('background:yellow')
 
        vbox.addWidget(self.email)
 
        self.button = QPushButton("Insert Data", self)
        self.button.setStyleSheet('background:green')
 
        self.button.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.InsertData)
 
        self.setLayout(vbox)
 
        self.show()
 
 
    def InsertData(self):        
        conn = mdb.connect(host="localhost",user= "root", passwd="",db= "pyqt5")
        print("hi")        
        cur = conn.cursor()
        name_su=self.name.text()
        email_su=self.email.text()
        print(name_su,email_su)              
        sql=cur.execute("INSERT INTO data(name, email)" "VALUES('%s', '%s')" % ((name_su).toUtf8(),(email_su).toUtf8()))
        QMessageBox.about(self,'Connected','Successfully inserted')
        cur.execute(sql)
        conn.writeValues(sql)
        QMessageBox.about(self,'Connected','Successfully inserted')
        cur.fetchone()
        conn.commit()        
        conn.close()

 
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
