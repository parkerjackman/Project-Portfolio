"""
Parker Jackman
Assignment 13
Circle Class
"""
import turtle

class Circle:
    def __init__(self, positionX, positionY, radius, color):
        self.__positionX = positionX
        self.__positionY = positionY
        self.__radius = radius
        self.__color = color
        self.__colorOptions = ["red", "yellow", "blue", "green"]


    def draw(self):
        turtle.setheading(0)
        turtle.fillcolor(self.__getColor())
        turtle.penup()
        turtle.goto(self.__positionX, self.__positionY - self.__radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.__radius)
        turtle.end_fill()


    def __getColor(self):
        return self.__colorOptions[self.__color]