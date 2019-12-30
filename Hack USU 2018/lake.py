import time
from character import Character

class Lake:
    def __init__(self):
        self.__gold = 2

    def returnGold(self):
        return self.__gold

    def foundGold(self):
        self.__gold -= 1


def lake(character):
    lake = Lake()
    while True:
        menu = "What would you like to do at the lake?"
        menu += "\n""1. Fish"
        menu += "\n""2. Take a walk"
        menu += "\n""3. Leave"

        choice = input(menu)

        if choice == "1":
            if character.returnInventoryAmount("fishing pole") > 0:
                time1 = time.time()
                print("You are now fishing.")
                timeCount = 8
                while timeCount > 0:
                    print("\r" + str(timeCount - 1) + " seconds left", end=" ")
                    timeCount -= 1
                    time.sleep(1)
                input("\n""Enter anything to stop fishing.")
                time2 = time.time()
                timeFishing = time2 - time1
                numFish = int(timeFishing // 8)
                for n in range(0, int(numFish)):
                    character.addToInventory("fish")
                print("You caught " + str(numFish) + " fish.")

            else:
                print("You don't have a fishing pole.")

        if choice == "2":
            time1 = time.time()
            print("You are now walking around the lake.")
            input("Enter anything to stop walking.")
            time2 = time.time()
            timeWalking = time2 - time1
            if timeWalking > 10:
                if lake.returnGold() > 0:
                    lake.foundGold()
                    character.addToInventory("gold")
                    print("You found a gold while walking.")

        if choice == "3":
            break






