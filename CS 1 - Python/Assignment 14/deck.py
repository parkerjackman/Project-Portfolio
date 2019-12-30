"""
Parker Jackman
Assignment 14
Deck Class
"""

import random
from card import Card

class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        for i in range(120):
            self.__deck.append(Card(i))
            random.shuffle(self.__deck)


    def draw(self):
        return self.__deck.pop()
