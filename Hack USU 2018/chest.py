import random


class Chest:
    def __init__(self):
        self.__possibleItems = ["fish", "fishing pole", "gold", "gold", "hat"]
        self.__visitedChests = []

    def getItem(self):
        spotNumber = random.randint(0, len(self.__possibleItems) - 1)
        chestItem = self.__possibleItems[spotNumber]
        self.__possibleItems.remove(chestItem)
        return chestItem

    def addToVisitedChests(self, location):
        self.__visitedChests.append(location)

    def visitedChests(self):
        return self.__visitedChests


def chest(character, x, y, item):
    while True:
        if (x, y) in item.visitedChests():
            break
        else:
            print("You have found a chest.")
            whatYouFound = item.getItem()
            print("You found a " + whatYouFound + ". It has been added to your inventory.")
            character.addToInventory(whatYouFound)
            item.addToVisitedChests((x, y))
            print(character.returnInventory())
            break

