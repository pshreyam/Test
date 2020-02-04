import json
from PyQt5 import QtWidgets,QtGui,QtCore
from search import *

class Ui_MainWindow(object):
    def setCompleter(self):
        try:
            fileobj=open('search_history.json','r')
            self.read=json.load(fileobj)
        except Exception:
            pass

        completer=QtWidgets.QCompleter(self.read)
        self.search_box.setCompleter(completer)

    def search_google(self):
        gs=GoogleSearch()
        item=self.search_box.text()
        try:
            fileobj=open('search_history.json','r')
            self.read=json.load(fileobj)            
            fileobj=open('search_history.json','w')
            self.read.append(item)
            json.dump(self.read,fileobj)
        except Exception:
            self.read=[]
            fileobj=open('search_history.json','w')
            self.read.append(item)
            json.dump(self.read,fileobj)
        self.setCompleter()
        gs.browse_item(item)

    def search_url(self):
        us=UrlBrowse()
        url=self.search_box.text()
        try:
            fileobj=open('search_history.json','r')
            self.read=json.load(fileobj)
            fileobj=open('search_history.json','w')
            self.read.append(url)
            json.dump(read,fileobj)
        except Exception:
            self.read=[]
            fileobj=open('search_history.json','w')
            self.read.append(url)
            json.dump(self.read,fileobj)
        self.setCompleter()
        us.browse_url(url)

    def setupUi(self,MainWindow):
        self.read=[]
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("QLineEdit{border-radius:6px;}""QPushButton:hover{background-color:gray;}")
        MainWindow.setFixedSize(400,200)
        self.centralwidget=QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.search_box=QtWidgets.QLineEdit(self.centralwidget)
        self.search_box.setGeometry(QtCore.QRect(10,10,290,35))
        self.search_box.setObjectName("search_box")
        self.search_box.returnPressed.connect(self.search_google) 
        self.setCompleter()                  

        self.search_button=QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(310,10,70,35))
        self.search_button.setObjectName("search_button")
        self.search_button.setAutoDefault(True)
        menu=QtWidgets.QMenu()
        menu.addAction("Search Url",self.search_url)
        menu.addAction("Google Search",self.search_google)
        self.search_button.setMenu(menu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
    def retranslateUi(self,MainWindow):
        _translate=QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Assistant-Search"))
        self.search_box.setPlaceholderText(_translate("MainWindow","Enter the url or text to search "))
        self.search_button.setText(_translate("MainWindow","Search"))

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())