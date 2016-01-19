__author__ = 'Pawel'
import sys
import unittest
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QInputDialog
from PyQt5.QtGui import QIcon
from archieve_dialog import ArchieveDialog

from user import User
from main_widget import MainWidget
from main import MainWindow

class ChatomaniacTestCase(unittest.TestCase):
    def setUp(self):
        app = QApplication(sys.argv)
        self.main = MainWindow()
        self.role = self.main.mainWidget.serverRole
    def test_server(self):
        self.assertEqual(self.role, True)

    def test_messageline_initialize(self):
        self.assertEqual(self.main.mainWidget.messageLineEdit.text(), "enter text here")

    def test_button_initialize(self):
        self.assertEqual(self.main.mainWidget.sendButton.text(), "Send")

    def test_db(self):
        self.main.mainWidget.db["2"] = 2
        self.assertEqual("2" in self.main.mainWidget.db, True)

    def test_user(self):
        self.assertEqual(self.main.user.name, "DefaultUser")


if __name__ == '__main__':
    unittest.main()
