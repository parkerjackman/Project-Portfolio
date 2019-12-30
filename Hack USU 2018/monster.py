import character
import random
import boss
import Battle

class Monster:
    def __init__(self):
        self.__visitedMonster = []

    def visitedMonster(self):
        return self.__visitedMonster

    def addToVisitedMonster(self, location):
        self.__visitedMonster.append(location)

def monster(character, x, y, location):
    while True:
        if (x, y) in location.visitedMonster():
            break
        else:
            monsterChoice = random.randint(0,3)
            dwarf  = boss.Boss("Gimley", "Waddling Dwarf", 5, "potion", "dagger", 0)
            vermin = boss.Boss("Smeagle", "Fierst little Vermin", 5, "potion", "claws", 0)
            if monsterChoice == 0:
                print("A goblin jumps out to attack you")
                choice = input("\n""What do you hit him with?\nAction: ")
                
                if choice in character.returnInventory() and choice == "axe" or "dagger" or "sword":
                    print("You killed the goblin!")
                    character.addToInventory("gold")
                    character.increaseExPoints(500)
                    print("You get gold!")
                    location.addToVisitedMonster((x, y))
                    break
                else:
                    print("That doesn't work. You lose a life.")
                    character.changeLife(-1)
                    location.addToVisitedMonster((x, y))
                    break
            if monsterChoice == 1:
                Battle.Battle(character, dwarf)
                break
            if monsterChoice == 2:
                Battle.Battle(character, vermin)
                break

