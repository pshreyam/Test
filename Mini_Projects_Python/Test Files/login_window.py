from PyQt5 import QtWidgets,QtGui,QtCore
from user_window import *
class Ui_LoginWindow(QtWidgets.QWidget):
    
    def login(self):
        uname=self.username_edit.text().strip().lower()
        pword=self.password_edit.text().strip()
        self.username_edit.clear()
        self.password_edit.clear()
        if (uname=='admin' and pword=='admin'):
            self.hide_show_button.setIcon(QtGui.QIcon('hide.png'))
            self.statusbar.showMessage("Logged in as {}.".format(uname))
            LoginWindow.hide()
            self.UserWindow=QtWidgets.QMainWindow()
            self.ui=Ui_UserWindow()
            self.ui.setupUi(self.UserWindow)
            self.UserWindow.show()
        else:
            QtWidgets.QMessageBox.warning(self,"Not valid","Enter a valid username and password.")

        
    def setupUi(self,LoginWindow):
        LoginWindow.setFixedSize(300,200)
        LoginWindow.setStyleSheet("QPushButton#hide_show_button{background-color:white;font-size:16;border-radius:6px;}""QPushButton{background-color:lightblue;font-size:16;border-radius:10px;}""QPushButton:hover{background-color:blue;color:white;}")
        self.centralwidget=QtWidgets.QWidget()

        self.info_label=QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(110,10,80,30))
        font=QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Consolas")
        self.info_label.setFont(font)
        self.info_label.setObjectName("info_label")
        
        self.username_label=QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(10,60,90,30))
        self.username_label.setObjectName("username_label")

        self.password_label=QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(10,100,90,30))
        self.password_label.setObjectName("password_label")

        self.username_edit=QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setGeometry(QtCore.QRect(100,60,180,30))
        self.username_edit.setObjectName("username_edit")

        self.password_edit=QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(100,100,180,30))
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")

        self.login_button=QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(200,135,80,35))
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.login)

        self.hide_show_button=QtWidgets.QPushButton(self.centralwidget)
        self.hide_show_button.setGeometry(QtCore.QRect(245,103,30,25))
        self.hide_show_button.setIcon(QtGui.QIcon('show.png'))
        self.hide_show_button.setObjectName("hide_show_button")
        password_status=["hidden"]
        def set_password_opacity():
            try:
                password_status.pop()
                self.password_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.hide_show_button.setIcon(QtGui.QIcon('hide.png'))
            except Exception:
                password_status.append("hidden")
                self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
                self.hide_show_button.setIcon(QtGui.QIcon('show.png'))
        self.hide_show_button.clicked.connect(set_password_opacity)

        self.statusbar=QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginWindow)
    
    def retranslateUi(self,LoginWindow):
        _translate=QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow","Login"))
        self.username_label.setText(_translate("LoginWindow","Username"))
        self.password_label.setText(_translate("LoginWindow","Password")) 
        self.info_label.setText(_translate("LoginWindow","Login"))   
        self.login_button.setText(_translate("LoginWindow","Login"))            


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    LoginWindow=QtWidgets.QMainWindow()
    ui=Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())