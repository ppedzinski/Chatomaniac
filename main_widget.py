import time
import socket
import shelve
import sys
import _thread
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QColor
from random import randint
from PyQt5.uic.properties import QtGui
from PyQt5.uic.properties import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QObject, pyqtSignal

__author__ = 'Pawel'

from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QGridLayout, QPushButton, QTextEdit)
"""
Class that represents main widget in MainWindow. Includes every widget that You will see on screen, excluding menubars.
"""
class MainWidget(QWidget):
    def __init__(self, user):
        super().__init__()

        self.serverRole = False
        self.tcp_ip = '192.168.1.1'
        #self.tcp_ip = '127.0.0.1'
        self.tcp_port = 5005
        self.buffer_size = 1024
        self.message = ""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if sys.argv[1] != "test":
            self.db = shelve.open('database5', 'c')


        self.serverThread = ServerWaitThread(self.s, self.buffer_size)
        self.clientThread = ClientWaitThread(self.s, self.buffer_size)
        self.clientThread.receivedMessage.connect(self.handleReceivedMessage)
        self.serverThread.receivedMessage.connect(self.handleReceivedMessage)

        self.user = user
        self.messageLineEdit = QLineEdit("enter text here", self)
        self.conversationTextEdit = QTextEdit(self)
        self.sendButton = QPushButton("Send", self)

        self.setConversationTextEdit()

        self.setConnections()

        self.initLayout()

        self.initialize_socket()

    def metoda(self, text):
        print(text)

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
        text +="\n"
        if sys.argv[1] != "test":
            if self.user.name in self.db:
                self.db[self.user.name] += text
            else:
                self.db[self.user.name] = ""
                self.db[self.user.name] += text
        self.messageLineEdit.setText("")

        if self.serverRole:
            self.serverThread.sendMessageToClient(bytes(text, 'UTF-8'))
        else:
            self.clientThread.sendMessageToServer(bytes(text, 'UTF-8'))

    def handleReceivedMessage(self, data):
        self.conversationTextEdit.append(data.rstrip())
        if sys.argv[1] != "test":
            self.db[self.user.name].append(data)

    def initialize_socket(self):
        try:
            self.create_server()
            self.serverThread.begin()
            self.serverRole = True
        except:
            self.s.connect((self.tcp_ip, self.tcp_port))
            #self.s.send(bytes(self.message, 'UTF-8'))
            self.clientThread.begin()

    def create_server(self):
        print("create server")
        i = self.s.bind((self.tcp_ip, self.tcp_port))
        print(i)
        self.s.listen(2)

"""
Class that represents server. It is made as thread
"""
class ServerWaitThread(QThread):
    receivedMessage = pyqtSignal(str)
    def __init__(self, s, buffer_size):
        QThread.__init__(self)
        self.s = s
        self.buffer_size = buffer_size
        self.conn = None

    def __del__(self):
        self.wait()

    def begin(self):
        self.start()

    def run(self):
        self.conn, addr = self.s.accept()
        print ('Connection address:', addr)
        while 1:
            data = self.conn.recv(self.buffer_size)
            if data:
                try:
                    self.receivedMessage.emit(data.decode("utf-8"))
                except:
                    print("something goes wrong with receiving data")
        self.conn.close()

    def sendMessageToClient(self, message):
        print("sending message to client")
        try:
            self.conn.send(message)
        except:
            print("Client is not yet there")
"""
Class that represents client. It is made as thread
"""
class ClientWaitThread(QThread):
    receivedMessage = pyqtSignal(str)
    def __init__(self, s, buffer_size):
        QThread.__init__(self)
        self.s = s
        self.buffer_size = buffer_size

    def __del__(self):
        self.wait()

    def begin(self):
        self.start()

    def run(self):
        while 1:
            data = self.s.recv(self.buffer_size)
            if data:
                try:
                    self.receivedMessage.emit(data.decode("utf-8"))
                except:
                    print("something goes wrong with receiving message")
        self.s.close()

    def sendMessageToServer(self, message):
        print("sending message to server")
        try:
            self.s.send(message)
        except:
            print("something goes wrong with sending message to server")