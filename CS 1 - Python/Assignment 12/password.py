"""
Parker Jackman
Assignment 12
Password Class
"""

class Password:
    __password = ""
    __message = ""
    def setPassword(self, password):
        self.__password = password


    def isValid(self):
        if self.__isLength() and self.__isLettersDigits() and self.__isTwoDigits() and self.__isNotPassword() and self.__isCorrectEnd():
            return True
        else:
            return False



    def __isLength(self):
        if len(self.__password) >= 8:
            return True
        else:
            return False


    def __isLettersDigits(self):
        count = 0
        for i in range(len(self.__password)):
            indexNum = self.__password[i]
            if indexNum.isdigit():
                count += 1
            elif indexNum.isalpha():
                count += 1
            else:
                continue

        if count == len(self.__password):
            return True
        else:
            return False


    def __isTwoDigits(self):
        digit = 0
        for i in range(len(self.__password)):
            indexNum = self.__password[i]
            if indexNum.isdigit():
                digit += 1

        if digit >= 2:
            return True
        else:
            return False


    def __isNotPassword(self):
        if "password" in self.__password:
            return False
        else:
            return True


    def __isCorrectEnd(self):
        if self.__password.endswith("123"):
            return False
        else:
            return True


    def getErrorMessage(self):
        self.__message = ""
        if not self.__isLength():
            self.__message += "Must be at least 8 characters\n"

        if not self.__isLettersDigits():
            self.__message += "Must only consist of letters and numbers\n"

        if not self.__isTwoDigits():
            self.__message += "Must contain at least 2 digits\n"

        if not self.__isNotPassword():
            self.__message += "Cannot contain the word 'password'\n"

        if not self.__isCorrectEnd():
            self.__message += "Cannot end with '123'\n"

        return self.__message
