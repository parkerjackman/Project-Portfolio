
class Character:
    def __init__(self, name, ClassType, maxLife, level):
        self.__name = name
        self.__life = maxLife
        self.__maxLife = maxLife
        self.__inventory = {'potion': 0, 'gold': 0, 'fish': 0, 'fishing pole': 0, "hat": 0,}
        self.__special = []
        self.__weapons = {'sword': 0, 'dagger': 1, 'axe': 0, 'bow': 0, 'arrow': 0, "shield": 0, 'fists':0}
        self.__level = level
        self.__baseAttack = 0
        self.__exPoints = 0
        self.increaseLevel(level)

    def displayCharacterInfo(self):
        return "Name: " + self.__name + "\n" + "Class: " + self.__type + "\n" + str(self.__life) + " Lives" + "\n" + \
               str(len(self.__inventory)) + " Items in inventory"
    
    def getName(self):
        return self.__name

    def getWeapons(self):
        return self.__weapons

    def getWeaponsAmount(self, item):
        return self.__weapons[item]

    def addWeapons(self, weapon):
        self.__weapons[weapon] += 1

    def removeWeapons(self, weapon):
        self.__weapons[weapon] -= 1

    def returnMaxLife(self):
        return self.__maxLife

    def increaseMaxLife(self, num):
        self.__maxLife += num

    def returnLife(self):
        return self.__life

    def changeLife(self, num):
        self.__life += num
        if self.__life > self.__maxLife:
            self.__life = self.__maxLife
    
    def subLife(self, num):
        self.__life -= num

    def returnInventory(self):
        return self.__inventory 

    def returnInventoryAmount(self, item):
        return self.__inventory[item]

    def addToInventory(self, item):
        self.__inventory[item] += 1

    def removeFromInventory(self, item):
        self.__inventory[item] -= 1

    def specialInventory(self):
        self.__special.sort()
        return self.__special

    def getLevel(self):
        return self.__level

    def increaseLevel(self, lvUp):
        for i in range(int(lvUp)):
            self.__level += 1
            self.__baseAttack += 1
            self.__maxLife += 1
            self.__life = self.__maxLife
            self.__exPoints = 0

    def getBaseAttack(self):
        return self.__baseAttack

    def getExPoints(self):
        return self.__exPoints

    def increaseExPoints(self,num):
        self.__exPoints += num
        if self.__exPoints == 1000:
            self.increaseLevel(self.getLevel()+1)
