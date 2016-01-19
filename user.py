__author__ = 'Pawel'
"""
Class that represents user. It stores basic information about user of chat
"""
class User:
    def __init__(self, name = "DefaultUser"):
        self.name = name

    def setName(self, name):
        self.name = name
