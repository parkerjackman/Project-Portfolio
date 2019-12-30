class Boss:
    def __init__(self, name, classType, life, inventory, weapon, level):
        self.__name = name
        self.__type = classType
        self.__life = life
        self.__inventory = []
        self.__weapons = {'claws': 0, 'dagger': 0, 'sword': 0, 'fire': 0}
        self.addWeapons(weapon)
        self.__level = level
        self.__baseAttack = 0
        self.increaseLevel(level)

    def displayBossInfo(self):
        return ("Name: " + self.__name + "\n" + "Class: " + self.__type + "\n" + str(self.__life) + " Lives" + "\n" + \
               str(len(self.__inventory)) + " Items in inventory")
    
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def returnLife(self):
        return self.__life
    
    def getWeapons(self):
        for x,y in self.__weapons.items():
            if y == True:
                return x
    
    def addWeapons(self, weapon):
        if weapon == 'claws':
            self.__weapons['claws'] += 1
        if weapon == 'sword':
            self.__weapons['sword'] += 1
        if weapon == 'fire':
            self.__weapons['fire'] += 1
        if weapon == 'dagger':
            self.__weapons['dagger'] += 1
        if weapon == 'fists':
            self.__weapons['fists'] +=1
            
    def subLife(self, num):
        self.__life -= num

    def addLife(self, num):
        self.__life += num

    def returnInventory(self):
        self.__inventory.sort()
        return self.__inventory

    def addToInventory(self, item):
        self.__inventory.append(item)

    def removeFromInventory(self, item):
        self.__inventory.remove(item)

    def getLevel(self):
        return self.__level 

    def increaseLevel(self, lvUp):
        for i in range(int(lvUp)):
            self.__level += 1
            self.__baseAttack += 1
            self.__life += 5

    def getBaseAttack(self):
        return self.__baseAttack
