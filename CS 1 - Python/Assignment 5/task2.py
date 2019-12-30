"""
Parker Jackman
Assn 5
Task 2
"""

import turtle

bullseye_x, bullseye_y = eval(input("Enter the location of the bull's eye center, (eg 5, 10): "))
radius = eval(input("Enter the radius of the bull's eye: "))

radius += 75

turtle.penup()
turtle.goto(bullseye_x, bullseye_y - radius)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

radius -= 25
turtle.penup()
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

radius -= 25
turtle.penup()
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

radius -= 25
turtle.penup()
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.pendown()

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(radius)
turtle.end_fill()

turtle.done()