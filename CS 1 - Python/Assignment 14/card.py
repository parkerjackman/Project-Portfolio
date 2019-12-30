"""
Parker Jackman
Assignment 14
Card Class
"""

class Card:
    def __init__(self, id):
        self.__id = id
        self.__value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.__coin = ["Heads", "Tails"]
        self.__mano = ["Rock", "Paper", "Scissors"]

    def getValue(self):
        return self.__value[self.__id % 20]

    def getCoin(self):
        return self.__coin[(self.__id // 20) % 2]

    def getMano(self):
        return self.__mano[self.__id // 40]


    def __str__(self):
        return str(self.getValue()) + " of " + self.getMano() + " " + self.getCoin()