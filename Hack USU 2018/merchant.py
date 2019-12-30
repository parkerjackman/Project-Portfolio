

class Merchant:
    def __init__(self):
        self.__inventory = ["potion", "fishing pole"]
        self.__weapons = ["shield", "sword", "dagger", "axe"]
        self.__otb = ["fish", "hat"]

    def returnInventory(self):
        return self.__inventory

    def weapons(self):
        return self.__weapons

    def sell(self, item):
        self.__inventory.remove(item)

    def returnOtb(self):
        return self.__otb


def merchant(character):
    merchant = Merchant()
    print("Welcome to my shop. Choose the number for what you would like to do.")
    merchantMenu = "1. View shop inventory"
    merchantMenu += "\n""2. Buy weapons"
    merchantMenu += "\n""3. Buy items"
    merchantMenu += "\n""4. Sell"
    merchantMenu += "\n""5. Leave"

    while True:
        menuChoice = eval(input(merchantMenu))
        if menuChoice == 1:
            for x in merchant.returnInventory():
                print(x)

        if menuChoice == 2:
            shopping = input("Enter the item you would like to buy: ")
            if shopping in merchant.weapons() and character.returnInventoryAmount("gold") >= 2:
                character.addWeapons(shopping)
                character.removeFromInventory("gold")
                character.removeFromInventory("gold")
                print("You now have " + shopping + " in your inventory.")
            else:
                print("That is not an item you can purchase.")

        if menuChoice == 3:
            shopping = input("Enter the item you would like to buy: ")
            if shopping in merchant.returnInventory() and character.returnInventoryAmount("gold") >= 2:
                character.addToInventory(shopping)
                character.removeFromInventory("gold")
                character.removeFromInventory("gold")
                print("You now have " + shopping + " in your inventory.")
            else:
                print("That is not an item you can purchase.")

        if menuChoice == 4:
            selling = input("Enter the item you would like to sell: ")
            if character.returnInventoryAmount(selling) > 0 and selling in merchant.returnOtb():
                character.addToInventory("gold")
                character.removeFromInventory(selling)
            else:
                print("That is not an item you can sell.")

        if menuChoice == 5:
            break


