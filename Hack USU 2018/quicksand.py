

class Quicksand:
    def __init__(self):
        self.__visitedQuicksand = []

    def visitedQuicksand(self):
        return self.__visitedQuicksand

    def addToVisitedQuicksand(self, location):
        self.__visitedQuicksand.append(location)


def quicksand(character, x, y, location):
    while True:
        if (x, y) in location.visitedQuicksand():
            break
        else:
            print("You fell in quicksand")
            choice = input("\n""What are you going to use to stop from sinking?")

            if choice in character.getWeapons() and choice == "shield":
                print("You got out")
                location.addToVisitedQuicksand((x, y))
            else:
                character.changeLife(-1)
                print("You lost a life while getting out.")
                location.addToVisitedQuicksand((x, y))

