"""
Parker Jackman
Assignment 13
Polygon Class
"""

class Polygon:
    def __init__(self, sides):
        self.__sides = sides

    def getNumSides(self):
        return self.__sides

    def __add__(self, other):
        return self.__sides + other.getNumSides()

    def __sub__(self, other):
        return self.__sides - other.getNumSides()

    def __lt__(self, other):
        return self.__sides < other.getNumSides()

    def __gt__(self, other):
        return self.__sides > other.getNumSides()

    def __eq__(self, other):
        return self.__sides == other.getNumSides()

    def __len__(self):
        return self.__sides * 5

    def __str__(self):
        return "I'm a polygon with " + str(self.__sides) + " sides"