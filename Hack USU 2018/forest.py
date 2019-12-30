import random

a = (5 * 15, -4 * 15)

def forest(character):
    while True:
        message1 = "Ahead there is a thick forest. What are you gonna do?"
        message1 += "\n""1. Try to go through it"
        message1 += "\n""2. Turn around"

        choice1 = input(message1)
        if choice1 == "1":
            choice2 = input("It's too thick to go through. What are you going to use?")

            if character.getWeaponsAmount(choice2) and choice2 == "axe":
                print("You got through!")
                if riddleTroll(character):
                    return 6 * 15, -4 * 15
                else:
                    return 4 * 15, -4 * 15
            elif choice2 in character.returnInventory():
                print(choice2 + "won't help you.")
                return 4 * 15, -4 * 15
            elif choice2 not in character.returnInventory():
                print("You don't have a " + choice2)
                return 4 * 15, -4 * 15
            elif choice2 not in character.getWeapons():
                print("You don't have a" + choice2)
                return 4 * 15, -4 * 15
            elif choice2 in character.getWeapons():
                print(choice2 + " wont help you get through the forest")
                return 4 * 15, -4 * 15
            else:
                print("You don't have " + choice2)
                return 4 * 15, -4 * 15

        if choice1 == "2":
            return 4 * 15, -4 * 15

def riddleTroll(character):
    while True:
        message1 = "After you got through the forest you stumbled upon a 30 ft ravenous troll. What are you gonna do?"
        message1 += "\n""1. Try to talk to it"
        message1 += "\n""2. Turn around and RUN!"

        choice1 = input(message1)
        if choice1 == "1":
            print("Instead of talking, he traps you and threatens to smash you with his club unless you answer his riddle.")
            if getRiddle():
                print("Correct! The troll grudgingly lets you go and raises your max health.")
                character.increaseMaxLife(1)
                return True
            else:
                print("Wrong! You lost a life from the troll's club then he let you go.")
                character.changeLife(-1)
                return True
        if choice1 == "2":
            return False


def getRiddle():
    riddleNum = random.randint(1,3)
    if riddleNum == 1:
        answer = input("The more you take the more you leave behind. What am I? ").lower()
        if answer == "footsteps":
            return True
        else:
            return False
    elif riddleNum == 2:
        answer = input("What is black when you buy it, red when you use it, and gray when you throw it away? ").lower()
        if answer == "charcoal":
            return True
        else:
            return False
    else:
        answer = input("Re-arrange the letters, O O U S W T D N E J R, to spell just one word. ").lower()
        if answer == "just one word":
            return True
        else:
            return False