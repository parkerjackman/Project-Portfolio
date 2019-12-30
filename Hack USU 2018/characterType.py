
class Type:
    def __init__(self, characterType):
        self.__type = characterType

    def startingClass(self):
        if self.__type == "fighter":
            return "sword"
        if self.__type == "mage":
            return "potion"
        if self.__type == "archer":
            return "fishing pole"


