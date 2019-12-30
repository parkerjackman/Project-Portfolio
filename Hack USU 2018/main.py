import turtle
from map import BackEndMovement
from character import Character
from characterType import Type
from movement import userMovement
from map import SettingMovement
from chest import chest
from chest import Chest
from quicksand import quicksand
from quicksand import Quicksand
from river import river
from lake import lake
from merchant import merchant
from forest import forest
from monster import Monster
from monster import monster
from boss import Boss
import Battle

def main():
    print("back story")
    name = input("Enter your character name: ")
    type = input("Choose a character type (Fighter, Mage, Archer): ").lower()
    character = Character(name, type, 5, 1)
    setUpType = Type(type)
    if type == "mage":
        character.addToInventory(setUpType.startingClass())
    if type == "archer":
        character.addToInventory(setUpType.startingClass())
    if type == "fighter":
        character.addWeapons(setUpType.startingClass())
    setUpMovement = SettingMovement()
    setUpMovement.gettingLst2()
    setUpMovement.gettingLst()
    setUpMovement.gettingQuickSandList()
    setUpMovement.gettingChestList()
    setUpMovement.gettingMonsterList()
    setUpMovement.runTurtle()
    movement = BackEndMovement(setUpMovement.gettingLst())
    chestInfo = Chest()
    quicksand1 = Quicksand()
    monsterInfo = Monster()
    while True:
        choice = input("Action: ")
        userMovement(movement, choice)
        turtle.update()
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) in setUpMovement.correctChestList():
            chest(character, movement.locationX(), movement.locationY(), chestInfo)
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) in setUpMovement.correctMonsterList():
            monster(character, movement.locationX(), movement.locationY(), monsterInfo)
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) in setUpMovement.correctQuicksandList():
            quicksand(character, movement.locationX(), movement.locationY(), quicksand1)
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) == (-6 * 15, 15):
            movement.goTo(river(character))
            turtle.update()
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) == (-9 * 15, -2 * 15):
            lake(character)
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) == (1 * 15, -6 * 15):
            merchant(character)
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) == (5 * 15, -4 * 15):
            movement.goTo(forest(character))
        if (movement.locationX() - 7.5, movement.locationY() - 7.5) == (5 * 15, 8 * 15):
            dragon = Boss("Smaug", "fire", 5, "axe", "fire", 1)
            Battle.Battle(character, dragon)
            turtle.update()

        if choice == "inventory":
            print(character.getWeapons())
            print(character.returnInventory())

        if character.returnLife() <= 0:
            print("You lose")
            break

        if choice == "potion" and choice in character.returnInventory():
            character.removeFromInventory("potion")
            character.changeLife(5)

        if choice == "life":
            print(character.returnLife())

        if choice == "exit":
            break
    turtle.exitonclick()


main()

