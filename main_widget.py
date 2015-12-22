__author__ = 'Pawel'

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QGridLayout)
"""
Class that represents main widget in MainWindow. Includes every widget that You will see on screen, excluding menubars.
"""
class MainWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.messageLineEdit = QLineEdit()
        self.conversationLabel = QLabel("wiadomosci")

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.messageLineEdit, 3, 1)
        self.grid.addWidget(self.conversationLabel, 1, 1)

        self.setLayout(self.grid)


