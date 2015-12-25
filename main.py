import sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QInputDialog
from PyQt5.QtGui import QIcon

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

    def createMenus(self):
        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.exitAction)
        self.userMenu = self.menubar.addMenu('&User')
        self.userMenu.addAction(self.editUserAction)

    def editUserName(self):
        text, ok = QInputDialog.getText(self, 'Name change dialog', 'Please, enter your name:', text=self.user.name)
        self.user.setName(text)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())  