import time
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QColor
from random import randint
from PyQt5.uic.properties import QtGui
from PyQt5.uic.properties import QtCore

__author__ = 'Pawel'

from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QGridLayout, QPushButton, QTextEdit)
"""
Class that represents main widget in MainWindow. Includes every widget that You will see on screen, excluding menubars.
"""
class MainWidget(QWidget):
    def __init__(self, user):
        super().__init__()

        self.user = user
        self.messageLineEdit = QLineEdit(self)
        self.conversationTextEdit = QTextEdit(self)
        self.sendButton = QPushButton("Send", self)

        self.setConversationTextEdit()

        self.setConnections()

        self.initLayout()

    def setConversationTextEdit(self):
        self.conversationTextEdit.setReadOnly(True)
        self.conversationTextEdit.setLineWrapMode(QTextEdit.NoWrap)

        font = self.conversationTextEdit.font()
        font.setFamily("Courier")
        font.setPointSize(10)

    def setConnections(self):
        self.sendButton.clicked.connect(self.sendButtonClicked)
        self.messageLineEdit.returnPressed.connect(self.sendButtonClicked)

    def initLayout(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.messageLineEdit, 3, 1)
        self.grid.addWidget(self.conversationTextEdit, 1, 1, 2, 2)
        self.grid.addWidget(self.sendButton, 3, 2)

        self.setLayout(self.grid)

    def sendButtonClicked(self):
        text = self.user.name + "(" + time.strftime("%H:%M:%S") + ")" + "\n" + self.messageLineEdit.text()
        self.conversationTextEdit.append(text)

        self.messageLineEdit.setText("")