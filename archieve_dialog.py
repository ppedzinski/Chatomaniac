

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QComboBox, QTextEdit

__author__ = 'Pawel'
"""
Class that represents archieve window. It allows you to see every conversation you have
"""
class ArchieveDialog(QtWidgets.QDialog):

    def __init__(self,parent, db):
        super(ArchieveDialog, self).__init__(parent)
        self.conversation = QTextEdit(self)
        self.combo = QComboBox(self)
        self.db = db
        self.initUI()

    def initUI(self):
        self.resize(300,300)
        for key, value in self.db.items():
            self.combo.addItem(key)
        self.conversation.move(0,20)
        self.combo.move(0, 0)
        self.combo.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.conversation.clear()
        self.conversation.append(self.db[text])

