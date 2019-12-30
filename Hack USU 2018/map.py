import turtle
import random


class BackEndMovement:
    def __init__(self, lst):
        self.__xLocation = 7.5
        self.__yLocation = 7.5
        self.__possibleMoves = lst

    def possibleMoves(self):
        return self.__possibleMoves

    def locationX(self):
        return self.__xLocation

    def locationY(self):
        return self.__yLocation

    def goUp(self):
        self.__yLocation += 15
        turtle.goto(self.__xLocation, self.__yLocation)

    def goRight(self):
        self.__xLocation += 15
        turtle.goto(self.__xLocation, self.__yLocation)

    def goDown(self):
        self.__yLocation -= 15
        turtle.goto(self.__xLocation, self.__yLocation)

    def goLeft(self):
        self.__xLocation -= 15
        turtle.goto(self.__xLocation, self.__yLocation)

    def goTo(self, newPosition):
        self.__xLocation, self.__yLocation = newPosition
        self.__xLocation += 7.5
        self.__yLocation += 7.5
        turtle.goto(self.__xLocation, self.__yLocation)

    def goToStartingPoint(self):
        self.__xLocation = 7.5
        self.__yLocation = 7.5


class SettingMovement:
    def __init__(self):
        self.__lst = []
        self.__lst2 = []
        self.__squareSize = 15
        self.__quicksandList = []
        self.__chestList = []
        self.__monsterList = []
        self.__riverList = [(-6 * 15, 1 * 15)]
        self.__bossList = [(5 * 15, 8 * 15)]
        self.__forestList = [(5 * 15, -4 * 15)]
        self.__lakeList = [(-10 * 15, -2 * 15), (-10 * 15, -1 * 15), (-9 * 15, -1 * 15)]
        self.__merchantList = [(1 * 15, -6 * 15)]

    def gettingLst(self):
        for i in range(-2, 2):
            for k in range(-2, 2):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-5, -2):
            for k in range(-1, 1):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-6, -4):
            for k in range(0, 2):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-9, -5):
            for k in range(1, 3):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-9, -5):
            for k in range(3, 4):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-9, -7):
            for k in range(4, 9):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-6, -4):
            for k in range(3, 5):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-5, -3):
            for k in range(4, 6):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-4, -2):
            for k in range(5, 7):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-3, 1):
            for k in range(6, 8):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(0, 4):
            for k in range(5, 7):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(3, 5):
            for k in range(6, 8):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(4, 7):
            for k in range(6, 9):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(1, 4):
            for k in range(-3, -1):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(3, 6):
            for k in range(-4, -2):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(5, 9):
            for k in range(-7, -3):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(1, 6):
            for k in range(1, 3):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(5, 9):
            for k in range(0, 4):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-3, -1):
            for k in range(-4, -2):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-4, -2):
            for k in range(-5, -3):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-5, -3):
            for k in range(-6, -4):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-6, -4):
            for k in range(-7, -5):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-1, 0):
            for k in range(-3, -2):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-8, -1):
            for k in range(-9, -7):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-2, 1):
            for k in range(-8, -6):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(0, 2):
            for k in range(-7, -5):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-9, -7):
            for k in range(-8, -2):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        for i in range(-9, -6):
            for k in range(-3, -1):
                self.__lst.append((i * self.__squareSize, k * self.__squareSize))

        return self.__lst


    def gettingLst2(self):
        for j in range(-10, 10):
            for k in range(-10, 10):
                self.__lst2.append((j * self.__squareSize, k * self.__squareSize))

        for x in self.__lst:
            while self.__lst2.count(x) > 0:
                self.__lst2.remove(x)
        return self.__lst2

    def gettingQuickSandList(self):
        for i in range(7):
            xOption = yOption = 10
            while ((xOption * 15, yOption * 15) not in self.__lst) and ((xOption * 15, yOption * 15) not in self.__quicksandList) and ((xOption * 15, yOption * 15) not in self.__riverList) and ((xOption * 15, yOption * 15) not in self.__bossList) and ((xOption * 15, yOption * 15) not in self.__merchantList):
                xOption = random.randint(-10, 10)
                yOption = random.randint(-10, 10)
            self.__quicksandList.append((xOption * 15, yOption * 15))
        return self.__quicksandList

    def gettingChestList(self):
        for i in range(5):
            xOption = yOption = 10
            while ((xOption * 15, yOption * 15) not in self.__lst) and ((xOption * 15, yOption * 15) not in self.__quicksandList) and ((xOption * 15, yOption * 15) not in self.__chestList) and ((xOption * 15, yOption * 15) not in self.__riverList) and ((xOption * 15, yOption * 15) not in self.__bossList) and ((xOption * 15, yOption * 15) not in self.__merchantList):
                xOption = random.randint(-10, 10)
                yOption = random.randint(-10, 10)
            self.__chestList.append((xOption * 15, yOption * 15))

    def gettingMonsterList(self):
        for i in range(6):
            xOption = yOption = 10
            while ((xOption * 15, yOption * 15) not in self.__lst) and ((xOption * 15, yOption * 15) not in self.__quicksandList) and ((xOption * 15, yOption * 15) not in self.__chestList) and ((xOption * 15, yOption * 15) not in self.__riverList) and ((xOption * 15, yOption * 15) not in self.__bossList) and ((xOption * 15, yOption * 15) not in self.__merchantList) and ((xOption * 15, yOption * 15) not in self.__forestList):
                xOption = random.randint(-10, 10)
                yOption = random.randint(-10, 10)
            self.__monsterList.append((xOption * 15, yOption * 15))

    def correctChestList(self):
        return self.__chestList

    def correctQuicksandList(self):
        return self.__quicksandList

    def correctMonsterList(self):
        return self.__monsterList


    def runTurtle(self):
        self.gettingLst()
        self.gettingLst2()
        turtle.tracer(0, 0)
        turtle.pencolor("black")
        turtle.speed(0)
        turtle.bgcolor("white")
        for u in self.__lst2:
            turtle.begin_fill()
            turtle.fillcolor("gray")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__quicksandList:
            turtle.begin_fill()
            turtle.fillcolor("brown")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__chestList:
            turtle.begin_fill()
            turtle.fillcolor("brown")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__riverList:
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__forestList:
            turtle.begin_fill()
            turtle.fillcolor("dark green")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__lakeList:
            turtle.begin_fill()
            turtle.fillcolor("blue")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__merchantList:
            turtle.begin_fill()
            turtle.fillcolor("yellow")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__monsterList:
            turtle.begin_fill()
            turtle.fillcolor("red")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        for u in self.__bossList:
            turtle.begin_fill()
            turtle.fillcolor("black")
            turtle.penup()
            turtle.goto(u)
            turtle.pendown()
            turtle.setheading(0)
            for l in range(4):
                turtle.forward(self.__squareSize)
                turtle.left(90)
            turtle.penup()
            turtle.end_fill()
        turtle.update()


