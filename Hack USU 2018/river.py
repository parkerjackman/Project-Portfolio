a = (-6 * 16, 1 * 15)


def river(character):
    while True:
        message1 = "Ahead there is a river. What are you gonna do?"
        message1 += "\n""1. Try to cross"
        message1 += "\n""2. Turn around"

        choice1 = input(message1)
        if choice1 == "1":
            choice2 = input("You can't swim across. What are you going to use?")

            if choice2 in character.returnInventory() and choice2 == "fishing pole":
                character.removeFromInventory(choice2)
                print("You made it across using the fishing pole's string but lost the pole in the process.")
                return -7 * 15, 1 * 15
            elif choice2 in character.getWeapons() and choice2 == "shield":
                print("You were able to swim across on your shield.")
                return -7 * 15, 1 * 15
            elif choice2 in character.returnInventory():
                character.removeFromInventory(choice2)
                print("Using " + choice2 + " didn't help you cross and you dropped it in the river.")
            else:
                print("You don't have " + choice2)

        if choice1 == "2":
            return -5 * 15, 15


