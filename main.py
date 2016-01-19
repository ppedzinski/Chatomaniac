import sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QInputDialog
from PyQt5.QtGui import QIcon
from archieve_dialog import ArchieveDialog

from user import User
from main_widget import MainWidget

"""
Class that represent main window of Chatomaniac. Include menubar and set main widget.
"""
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.user = User()
        self.initUI()

    def initUI(self):

        self.createActions()
        self.createMenus()
        self.mainWidget = MainWidget(self.user)
        self.setCentralWidget(self.mainWidget)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Chatomaniac')
        self.show()


    def createActions(self):
        self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(qApp.quit)

        self.editUserAction = QAction(QIcon('user.png'), '&User', self)
        self.editUserAction.setShortcut('Ctrl+U')
        self.editUserAction.setStatusTip('Edit user data')
        self.editUserAction.triggered.connect(self.editUserName)

        self.archieveAction = QAction( '&Archieve', self)
        self.archieveAction.setShortcut('Ctrl+A')
        self.archieveAction.setStatusTip('Show archieve')
        self.archieveAction.triggered.connect(self.showArchieve)

    def createMenus(self):
        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.exitAction)
        self.userMenu = self.menubar.addMenu('&User')
        self.userMenu.addAction(self.editUserAction)
        self.archieveMenu = self.menubar.addMenu('Archieve')
        self.archieveMenu.addAction(self.archieveAction)

    def editUserName(self):
        text, ok = QInputDialog.getText(self, 'Name change dialog', 'Please, enter your name:', text=self.user.name)
        self.user.setName(text)

    def showArchieve(self):
        archieveDialog = ArchieveDialog(self, self.mainWidget.db)
        archieveDialog.exec_()
    def closeEvent(self,event):
        print("zamykamy")
        if sys.argv[1] != "test":
            self.mainWidget.db.close()
        event.accept()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())  