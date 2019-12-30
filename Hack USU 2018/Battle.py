import character
import boss
import monster
import time
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.status(0)
        self.theBattle()

    def theBattle(self):
        self.battleSequence = True
        whosTurn = random.randint(0,2)
        if whosTurn == 0:
            while self.battleSequence == True:
                self.yourAttack()
                self.defeat()
                if self.battleSequence == False:
                    break
                self.enemyAttack()
                self.defeat()
        else:
            while self.battleSequence == True:
                self.enemyAttack()
                self.defeat()
                if self.battleSequence == False:
                    break
                self.yourAttack()
                self.defeat()
    
    def yourAttack(self):
        self.availableActions()
        print("Action: ", end='')
        action = input()
        print()

        if action in self.player.getWeapons():
            self.attack(action, self.player, self.enemy)

        if (action == 'potion') and self.player.returnInventoryAmount('potion') > 0:
            self.player.changeLife(5)
            self.player.removeFromInventory('potion')
            self.status(2)

        if (action == 'potion') and self.player.returnInventoryAmount('potion') == 0:
                print('you have no more potions')
        
        if action == 'chimichanga':
            self.attack('chimichanga', self.player, self.enemy)
        if action == "run":
            chance = random.randint(0,5)
            if chance == 0:
                print("{0} prevented {1} from escaping").format(self.enemy.getName(), self.player.getName()) 
            if chance == 1:
                print("{1} escaped from {0}").format(self.enemy.getName(), self.player.getName()) 
                self.battleSequence = False
        
    def enemyAttack(self):
        self.attack(self.enemy.getWeapons(),self.enemy, self.player)            

    def defeat(self):
            if self.player.returnLife() < 1:
                print("{0} defeated {1}.\nYOU LOSE!".format(self.enemy.getName(), self.player.getName()))
                self.battleSequence = False
                return False
            if self.enemy.returnLife() < 1:
                self.player.increaseExPoints(1000)
                print("{0} defeated {1}! You increased your exp to {2}".format(self.player.getName(), self.enemy.getName(), self.player.getExPoints()))
                self.battleSequence = False
                return False

    def enemyAvalailableActions(self):
        weapons=[]
        for x, y in self.enemy.getWeapons().items():
            if y == True:
                weapons.append(x)
        weaponOfChoice = random.randint(0, len(weapons))
        return self.enemy.getWeapons[weapons[weaponOfChoice]]

    def availableActions(self): 
        print("\n","==="*10,"\nAvailable Actions: ")
 
        if (self.player.returnInventoryAmount('potion') == 0):
            print("** You have no Potions **")

        print("* Use Weapon: ")
        for x, y in self.player.getWeapons().items():
            if y == True:
                print("\t",x)
               
        if (self.player.returnInventoryAmount('potion') != 0):
            print("* Use item\n\tpotion ({0})".format((self.player.returnInventoryAmount('potion'))))

    def status(self, num):
        if num == 0:
            print("{0} finds {1} the {2}. \nYou currently have {3} health and {1} has {4} health.".format(self.player.getName(), self.enemy.getName(), self.enemy.getType(), self.player.returnLife(), self.enemy.returnLife()))
        if num == 1:
            print("{0} currently has {1} health.\n{2} currenly has {3} health.".format(self.player.getName(), self.player.returnLife(), self.enemy.getName(), self.enemy.returnLife()))
        if num == 2:
            print("{0} used a {1} to increase health to {2}.".format(self.player.getName(), 'potion', self.player.returnLife()))

    def useWeapon(self, weapon):
        weaponDamage = {'bow': 3, "sword": 5, "axe": 3, "dagger": 2, 'fists': 1, 'claws': 2, 'fire': 5, 'chimichanga':9000}
        return weaponDamage[weapon]

    def attack(self, weapon, attacker, defender):
        print("{0} used {1} on {2}. ".format(attacker.getName(), weapon, defender.getName()))
        defender.subLife(self.useWeapon(weapon) + defender.getBaseAttack())
        print("{0} health is now {1}.".format(defender.getName(), defender.returnLife()))

# def __init__(self, name, classType, life, inventory):
'''
player = character.Character("Jim", "dagger", 5, 0)


dwarf  = boss.Boss("Gimley", "Waddling Dwarf", 5, "potion", "dagger", 0)
vermin = boss.Boss("Smeagle", "Fierst little Vermin", 5, "potion", "claws", 0)
vermin = boss.Boss("Smeagle", "Fierst little Vermin", 5, "potion", "claws", 0)

dragon = boss.Boss("Smoag", "Firebreathing Dragon", 5, "Axe", "fire", 3)

player.addWeapons("sword")
player.addWeapons("dagger")
player.removeWeapons("dagger")
player.addToInventory("potion")
player.addToInventory("potion")
player.addToInventory("potion")
player.removeFromInventory("potion")
player.returnInventory()
Battle(player, dwarf)
Battle(player, vermin)
Battle(player, dragon)
'''
'''
player = character.Character("Jim", "dagger", 5, 0)
dragon = boss.Boss("Smoag", "Firebreathing Dragon", 5, "Axe", "fire", 3)
Battle(player, dragon)
'''
