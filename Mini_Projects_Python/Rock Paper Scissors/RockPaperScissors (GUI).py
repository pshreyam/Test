from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from python_rps import *

class Ui_MainWindow(object):
    def set_user_computer(self,choice,user):
        rock = QPixmap('rock.png')
        paper= QPixmap('paper.png')
        scissors=QPixmap('scissors.png')
        self.label_user.setStyleSheet("background:blue;\n""border-radius:30px;")
        self.label_computer.setStyleSheet("background:blue;\n""border-radius:30px;")
        ####for computer##########
        if (choice=="paper"):
            self.label_computer.setPixmap(paper)
        elif (choice=="scissors"):
            self.label_computer.setPixmap(scissors)
        else:
            self.label_computer.setPixmap(rock)
        #########################
        ####for user##################
        if (user=="paper"):
            self.label_user.setPixmap(paper)
        elif (user=="scissors"):
            self.label_user.setPixmap(scissors)
        else:
            self.label_user.setPixmap(rock)
        #############################
            
    def ViewHelp(self):
        pass
    def About(self):
        pass
    def save(self):
        pass

    def reset(self):
        self.label.setText("")
        computer=QPixmap('computer.png')
        user=QPixmap('user.png')
        self.label.move(30,60)
        self.label.setText("Let's Play!!!")
        self.label_user.setStyleSheet("background:blue;\n""border-radius:30px;")
        self.label_user.setPixmap(user)
        self.label_computer.setStyleSheet("background:blue;\n""border-radius:30px;")
        self.label_computer.setPixmap(computer)
        user=""
        self.statusbar.showMessage("Reseting....",1000)

    def userRock(self):
        user="rock"
        result,choice=play(user)
        self.label.move(90,250)
        self.label.setText(result)
        self.set_user_computer(choice,user)
        self.statusbar.showMessage("Computer chose: "+choice+"    "+"You chose: "+user)
        user=""

    def userPaper(self):
        user="paper"
        result,choice=play(user)
        self.label.move(90,250)
        self.label.setText(result)
        self.set_user_computer(choice,user)
        self.statusbar.showMessage("Computer chose: "+choice+"    "+"You chose: "+user)
        user=""
        

    def userScissors(self):
        user="scissors"
        result,choice=play(user)
        self.label.move(90,250)
        self.label.setText(result)
        self.set_user_computer(choice,user)
        self.statusbar.showMessage("Computer chose: "+choice+"    "+"You chose: "+user)
        user=""
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        #MainWindow.setStyleSheet("background-image:url(rps_background.png);")        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.rock_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rock_pushButton.setGeometry(QtCore.QRect(40, 480, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.rock_pushButton.setFont(font)
        self.rock_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rock_pushButton.setObjectName("rock_pushButton")
        self.rock_pushButton.setStyleSheet("border-radius:25px;\n""background:'blue';\n""color:'white';\n")
        self.rock_pushButton.setIcon(QIcon('rock.png'))
        self.rock_pushButton.setIconSize(QSize(191,51))
        self.rock_pushButton.clicked.connect(self.userRock)
        self.rock_pushButton.setAutoDefault(True)


        self.scissors_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.scissors_pushButton.setGeometry(QtCore.QRect(290, 480, 191, 51))        
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.scissors_pushButton.setFont(font)
        self.scissors_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scissors_pushButton.setObjectName("scissors_pushButton")
        self.scissors_pushButton.setStyleSheet("border-radius:25px;\n""background:'blue';\n""color:'white';\n")
        self.scissors_pushButton.setIcon(QIcon('scissors.png'))
        self.scissors_pushButton.setIconSize(QSize(191,51))
        self.scissors_pushButton.clicked.connect(self.userScissors)
        self.scissors_pushButton.setAutoDefault(True)
        
        
        self.paper_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.paper_pushButton.setGeometry(QtCore.QRect(530, 480, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.paper_pushButton.setFont(font)
        self.paper_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paper_pushButton.setObjectName("paper_pushButton")
        self.paper_pushButton.setStyleSheet("border-radius:25px;\n""background:'blue';\n""color:'white';\n")
        self.paper_pushButton.setIcon(QIcon('paper.png'))
        self.paper_pushButton.setIconSize(QSize(191,51))
        self.paper_pushButton.clicked.connect(self.userPaper)
        self.paper_pushButton.setAutoDefault(True)

        
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(0, 0, 800, 42))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("background: rgb(7, 11, 255);\n")
        self.info_label.setObjectName("info_label")
        self.info_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Let's Play!!!")

        self.userlabel= QtWidgets.QLabel(self.centralwidget)
        self.userlabel.setGeometry(QtCore.QRect(300, 90, 200, 30))
        self.userlabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.userlabel.setFont(font)
        self.userlabel.setObjectName("userlabel")
        self.userlabel.setText("User")

        self.computerlabel= QtWidgets.QLabel(self.centralwidget)
        self.computerlabel.setGeometry(QtCore.QRect(530, 90, 200, 30))
        self.computerlabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.computerlabel.setFont(font)
        self.computerlabel.setObjectName("computerlabel")
        self.computerlabel.setText("Computer") 

        computer=QPixmap('computer.png')
        user=QPixmap('user.png')
        
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(300, 130, 200, 200))
        self.label_user.setStyleSheet("background:blue;\n""border-radius:30px;")
        self.label_user.setPixmap(user)
        self.label_user.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        #self.label_user.setText("User")       
               
        self.label_computer = QtWidgets.QLabel(self.centralwidget)
        self.label_computer.setGeometry(QtCore.QRect(530, 130, 200, 200))
        self.label_computer.setStyleSheet("background:blue;\n""border-radius:30px;")
        self.label_computer.setPixmap(computer)
        self.label_computer.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_computer.setFont(font)
        self.label_computer.setObjectName("label_computer")
        #self.label_computer.setText("Computer")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.setShortcut("Ctrl+R")
        self.actionReset.triggered.connect(self.reset)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.save)       
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+E")
        self.actionExit.triggered.connect(MainWindow.close)
        self.menuOptions.addAction(self.actionSave)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionReset)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())
        
        self.actionViewHelp = QtWidgets.QAction(MainWindow)
        self.actionViewHelp.setObjectName("actionViewHelp")
        self.actionViewHelp.setShortcut("Ctrl+H")
        self.actionViewHelp.triggered.connect(self.ViewHelp)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setShortcut("Ctrl+A")
        self.actionAbout.triggered.connect(self.About)
        
        self.menuHelp=QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.addAction(self.actionViewHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.rock_pushButton.setText(_translate("MainWindow", "Rock"))
        self.paper_pushButton.setText(_translate("MainWindow", "Paper"))
        self.scissors_pushButton.setText(_translate("MainWindow", "Scissors"))
        self.info_label.setText(_translate("MainWindow", "Let us play Rock/ Paper/ Scissors:"))
        self.menuOptions.setTitle(_translate("MainWindow", "Game"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionViewHelp.setText(_translate("MainWindow", "View Help"))
        self.actionAbout.setText(_translate("MainWindow", "About Rock Paper Scissors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
