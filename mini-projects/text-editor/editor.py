import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


EDITOR_NAME = "TEXT EDITOR"


class Ui_MainWindow(QWidget):
    filename = None
    
    def clear(self):
        self.textEdit.setText("")
        
    def createnewfile(self):
        MainWindow.setWindowTitle(f"{EDITOR_NAME} -*New File")
        self.clear()

    def openfile(self):
        name = QFileDialog.getOpenFileName(self, "Open File", sys.path[0], "*.txt")[0]
        try:
            with open(name, 'r') as file:
                text = file.read()
                self.textEdit.setText(text)
        except Exception as e:
            print(e)
        else:
            self.filename = name
            MainWindow.setWindowTitle(f"{EDITOR_NAME} - {name}")
        
    def savefile(self):
        if self.filename:
            with open(self.filename, 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)
        
    def saveasfile(self):
        name = QFileDialog.getSaveFileName(self, "Save File")[0]
        with open(name, 'w') as file:
            text = self.textEdit.toPlainText()
            file.write(text)
        MainWindow.setWindowTitle(f"{EDITOR_NAME} - {name}")
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1350, 690))
        font=QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.openfile)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.triggered.connect(self.savefile)

        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.saveasfile)
        

        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionClear.setShortcut("Ctrl+f2")
        self.actionClear.triggered.connect(self.clear)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setShortcut("Ctrl+N")
        self.actionNew.triggered.connect(self.createnewfile)

        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.setShortcut("Ctrl+Z")
        
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.setShortcut("Ctrl+Shift+Z")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionView_Help = QtWidgets.QAction(MainWindow)
        self.actionView_Help.setObjectName("actionView_Help")
        self.actionAbout_Text_Editor = QtWidgets.QAction(MainWindow)
        self.actionAbout_Text_Editor.setObjectName("actionAbout_Text_Editor")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuHelp.addAction(self.actionView_Help)
        self.menuHelp.addAction(self.actionAbout_Text_Editor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Editor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionView_Help.setText(_translate("MainWindow", "View Help"))
        self.actionAbout_Text_Editor.setText(_translate("MainWindow", "About Text Editor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
