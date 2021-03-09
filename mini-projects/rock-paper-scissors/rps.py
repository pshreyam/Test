from os import environ

from PyQt5 import QtCore, QtGui, QtWidgets
# not a good idea to import all the components fron modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from engine import play
import random

ASSETS_FOLDER = "assets"
HOLD_SLOGAN = ["Let's Get Going!", "Let's Play!", "Let's Start Now!"]

def suppress_qt_warnings():
    """
    Suppresses Qt Warnings
    """
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


class Ui_MainWindow(object):
    def set_user_computer(self, choice, user):
        rock = QPixmap(f'{ASSETS_FOLDER}/rock.png')
        paper = QPixmap(f'{ASSETS_FOLDER}/paper.png')
        scissors = QPixmap(f'{ASSETS_FOLDER}/scissors.png')
        self.label_user.setStyleSheet("background:rgb(50, 173, 81);\n""border-radius:10px;")
        self.label_computer.setStyleSheet("background:rgb(95, 66, 212);\n""border-radius:10px;")
        
        # for computer
        if choice == "paper":
            self.label_computer.setPixmap(paper.transformed(QTransform().scale(-1, 1)))
        elif choice == "scissors":
            self.label_computer.setPixmap(scissors.transformed(QTransform().scale(-1, 1)))
        else:
            self.label_computer.setPixmap(rock.transformed(QTransform().scale(-1, 1)))
        
        # for user
        if user == "paper":
            self.label_user.setPixmap(paper)
        elif user == "scissors":
            self.label_user.setPixmap(scissors)
        else:
            self.label_user.setPixmap(rock)
             
    def view_help(self):
        """ Implement help functionalities using this function
        Pop up a help dialog box.
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("<h2>Help for Rock Paper Scissors</h2>")
        with open("docs/help.txt", "r") as file:
            text = file.read()
        msg.setInformativeText(text)
        msg.setWindowTitle("Help - Rock Paper Scissors")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
      
    def view_about(self):
        """ Implement about functionalities using this function
        Pop up an about dialog box.
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("<h2>Welcome to Rock Paper Scissors!</h2>")
        with open("docs/about.txt", "r") as file:
            text = file.read()
        msg.setInformativeText(text)
        msg.setWindowTitle("About - Rock Paper Scissors")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def reset(self):
        self.label.setText("")
        computer = QPixmap(f"{ASSETS_FOLDER}/computer.png")
        user = QPixmap(f"{ASSETS_FOLDER}/user.png")
        self.label.move(30,60)
        self.label.setText(f"{random.choice(HOLD_SLOGAN)}")
        self.label_user.setStyleSheet("background:rgb(50, 173, 81);\n""border-radius:10px;")
        self.label_user.setPixmap(user)
        self.label_computer.setStyleSheet("background:rgb(95, 66, 212);\n""border-radius:10px;")
        self.label_computer.setPixmap(computer)
        user = ""
        self.statusbar.showMessage("Reseting...", 200)

    def user_rock(self):
        self.statusbar.showMessage("Playing...")
        user = "rock"
        result, choice = play(user)
        self.label.move(90, 250)
        self.label.setText(result)
        self.set_user_computer(choice, user)
        self.statusbar.showMessage(f"Computer chose: {choice} \t\t You chose: {user}")
        user = ""

    def user_paper(self):
        self.statusbar.showMessage("Playing...")
        user = "paper"
        result, choice = play(user)
        self.label.move(90, 250)
        self.label.setText(result)
        self.set_user_computer(choice, user)
        self.statusbar.showMessage(f"Computer chose: {choice} \t\t You chose: {user}")
        user = ""
        
    def user_scissors(self):
        self.statusbar.showMessage("Playing...")
        user = "scissors"
        result,choice = play(user)
        self.label.move(90, 250)
        self.label.setText(result)
        self.set_user_computer(choice, user)
        self.statusbar.showMessage(f"Computer chose: {choice} \t\t You chose: {user}")
        user = ""
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{ASSETS_FOLDER}/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.rock_pushButton.setStyleSheet("border-radius:8px;\n""background:rgb(184, 68, 110);\n""color:'white';\n")
        self.rock_pushButton.setIcon(QIcon(f"{ASSETS_FOLDER}/rock.png"))
        self.rock_pushButton.setIconSize(QSize(191,51))
        self.rock_pushButton.clicked.connect(self.user_rock)
        self.rock_pushButton.setAutoDefault(True)


        self.scissors_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.scissors_pushButton.setGeometry(QtCore.QRect(290, 480, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.scissors_pushButton.setFont(font)
        self.scissors_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scissors_pushButton.setObjectName("scissors_pushButton")
        self.scissors_pushButton.setStyleSheet("border-radius:8px;\n""background:rgb(112, 189, 53);\n""color:'white';\n")
        self.scissors_pushButton.setIcon(QIcon(f"{ASSETS_FOLDER}/scissors.png"))
        self.scissors_pushButton.setIconSize(QSize(191,51))
        self.scissors_pushButton.clicked.connect(self.user_scissors)
        self.scissors_pushButton.setAutoDefault(True)
        
        
        self.paper_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.paper_pushButton.setGeometry(QtCore.QRect(530, 480, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.paper_pushButton.setFont(font)
        self.paper_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.paper_pushButton.setObjectName("paper_pushButton")
        self.paper_pushButton.setStyleSheet("border-radius:8px;\n""background:rgb(217, 48, 67);\n""color:'white';\n")
        self.paper_pushButton.setIcon(QIcon(f"{ASSETS_FOLDER}/paper.png"))
        self.paper_pushButton.setIconSize(QSize(191,51))
        self.paper_pushButton.clicked.connect(self.user_paper)
        self.paper_pushButton.setAutoDefault(True)

        
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(0, 0, 800, 42))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("background: rgb(76, 122, 161);\n")
        self.info_label.setObjectName("info_label")
        self.info_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;\nbackground: None;\n")
        self.label.setObjectName("label")
        self.label.setText(f"{random.choice(HOLD_SLOGAN)}")

        self.userlabel = QtWidgets.QLabel(self.centralwidget)
        self.userlabel.setGeometry(QtCore.QRect(300, 90, 200, 30))
        self.userlabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.userlabel.setFont(font)
        self.userlabel.setStyleSheet("color: black;\nbackground: None;\n")
        self.userlabel.setObjectName("userlabel")
        self.userlabel.setText("User")

        self.computerlabel = QtWidgets.QLabel(self.centralwidget)
        self.computerlabel.setGeometry(QtCore.QRect(530, 90, 200, 30))
        self.computerlabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.computerlabel.setFont(font)
        self.computerlabel.setStyleSheet("color: black;\nbackground: None;\n")
        self.computerlabel.setObjectName("computerlabel")
        self.computerlabel.setText("Computer") 

        computer = QPixmap(f"{ASSETS_FOLDER}/computer.png")
        user = QPixmap(f"{ASSETS_FOLDER}/user.png")
        
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(300, 130, 200, 200))
        self.label_user.setStyleSheet("background:rgb(50, 173, 81);\n""border-radius:10px;")
        self.label_user.setPixmap(user)
        self.label_user.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        
        self.label_computer = QtWidgets.QLabel(self.centralwidget)
        self.label_computer.setGeometry(QtCore.QRect(530, 130, 200, 200))
        self.label_computer.setStyleSheet("background:rgb(95, 66, 212);\n""border-radius:10px;")
        self.label_computer.setPixmap(computer)
        self.label_computer.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        self.label_computer.setFont(font)
        self.label_computer.setObjectName("label_computer")
        
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
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(MainWindow.close)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionReset)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())
        
        self.actionViewHelp = QtWidgets.QAction(MainWindow)
        self.actionViewHelp.setObjectName("actionViewHelp")
        self.actionViewHelp.setShortcut("Ctrl+H")
        self.actionViewHelp.triggered.connect(self.view_help)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setShortcut("Ctrl+A")
        self.actionAbout.triggered.connect(self.view_about)
        
        self.menuMisc=QtWidgets.QMenu(self.menubar)
        self.menuMisc.setObjectName("menuMisc")
        self.menuMisc.addAction(self.actionViewHelp)
        self.menuMisc.addSeparator()
        self.menuMisc.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMisc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.rock_pushButton.setText(_translate("MainWindow", "Rock"))
        self.paper_pushButton.setText(_translate("MainWindow", "Paper"))
        self.scissors_pushButton.setText(_translate("MainWindow", "Scissors"))
        self.info_label.setText(_translate("MainWindow", "Let us play Rock/Paper/Scissors:"))
        self.menuOptions.setTitle(_translate("MainWindow", "&Game"))
        self.menuMisc.setTitle(_translate("MainWindow", "&..."))
        self.actionReset.setText(_translate("MainWindow", "&Reset"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionViewHelp.setText(_translate("MainWindow", "&Help"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))


if __name__ == "__main__":
    import sys
    suppress_qt_warnings()
    try: 
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print('--- Closing the interface 🚀️ ---')
        sys.exit(0)
