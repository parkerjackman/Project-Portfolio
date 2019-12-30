"""
Parker Jackman
Assignment 13
Rectangle Class
"""

import turtle

class Rectangle:
    def __init__(self, positionX, positionY, width, height, color):
        self.__positionX = positionX
        self.__positiony = positionY
        self.__width = width
        self.__height = height
        self.__color = color
        self.__colorOptions = ["red", "yellow", "blue", "green"]


    def draw(self):
        turtle.setheading(0)
        turtle.fillcolor(self.__getColor())
        turtle.penup()
        turtle.goto(self.__positionX, self.__positiony)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.end_fill()


    def __getColor(self):
        return self.__colorOptions[self.__color]



list = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

num = 3

list[num] += 1