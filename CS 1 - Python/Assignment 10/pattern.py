"""
Parker Jackman
Assignment 10
pattern module
"""

import random
import turtle

# define reset()
def reset():
    turtle.reset()

# define setup()
def setup():
    turtle.speed(0)
    turtle.screensize(1000, 800)

# define define drawRectanglePattern()
def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    heading = 0
    for i in range (count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(heading)
        turtle.forward(offset)
        turtle.left(rotation)
        turtle.pendown()

        setRandomColor()
        drawRectangle(height, width)
        heading += 360 / count



# define drawRectangle()
def drawRectangle(height, width):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)


# define drawCirclePattern()
def drawCirclePattern(centerX, centerY, offset, radius, count):
    heading = 0
    for i in range(count):
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(heading)
        turtle.forward(offset)
        turtle.setheading(heading - 90)
        turtle.pendown()

        setRandomColor()
        turtle.circle(radius)
        heading += 360 / count


# define drawSuperPattern()
def drawSuperPattern(num = random.randint(5, 10)):
     for n in range(num):
        shape = random.randint(0,1)
        if shape == 0:
            drawRectanglePattern(centerX = random.randint(-470, 470), centerY = random.randint(-370, 370),
                         offset = random.randint(-100, 100), width = random.randint(5, 100),
                         height = random.randint(5, 100), count = random.randint(5, 50),
                         rotation = random.randint(0, 360))
        else:
            drawCirclePattern(centerX = random.randint(-470, 470), centerY = random.randint(-370, 370),
                      offset = random.randint(-100, 100), radius = random.randint(5, 100),
                      count = random.randint(5, 50))


# setRandomColor()
def setRandomColor():
    color = random.randint(0, 2)
    if color == 0:
        color = "red"
    elif color == 1:
        color = "green"
    else:
        color = "blue"
    turtle.color(color)

# done()
def done():
    turtle.done()