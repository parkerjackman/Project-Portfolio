"""
Parker Jackman
Assignment 12
Chessboard class
"""


import turtle

class Chessboard:
    def __init__(self, startX, startY, width = 250, height = 250):
        self.__startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height


    def draw(self):
        turtle.penup()
        turtle.goto(self.__startX, self.__startY)
        turtle.pendown()
        self.__drawRectangle(self.__width, self.__height)
        self.__drawAllRectangles(self.__startX, self.__startY, self.__width, self.__height)



    def __drawRectangle(self, width, height):
        turtle.setheading(0)
        turtle.speed(0)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)


    def __drawAllRectangles(self, startX, startY, width, height):
        for i in range(1, 9):
            # if i is odd
            if i % 2 != 0:
                # loop 4 times
                for j in range(0, 4):
                    # rectangleCornerX = startX + width / 8 * j
                    rectangleCornerX = startX + (width / 8) * j * 2
                    # rectangleCornerY = startY + height / 8 * (i - 1)
                    rectangleCornerY = startY + (height / 8) * (i - 1)
                    # go to (rectangleCornerX, rectangleCornerY)
                    turtle.penup()
                    turtle.goto(rectangleCornerX, rectangleCornerY)
                    turtle.pendown()
                    # call drawRectangle()
                    turtle.begin_fill()
                    self.__drawRectangle(width / 8, height / 8)
                    turtle.end_fill()

            # if i is even
            else:
                # loop 4 times
                for j in range(0, 4):
                    # rectangleCornerX = startX + width / 8 + width / 8 * j * 2
                    rectangleCornerX = startX + width / 8 + width / 8 * j * 2
                    # rectangleCornerY = startY + height / 8 * (i - 1) * 2
                    rectangleCornerY = startY + height / 8 * (i - 1)
                    # go to (rectangleCornerX, rectangleCornerY)
                    turtle.penup()
                    turtle.goto(rectangleCornerX, rectangleCornerY)
                    turtle.pendown()
                    # call drawRectangle
                    turtle.begin_fill()
                    self.__drawRectangle(width / 8, height / 8)
                    turtle.end_fill()