"""
Parker Jackman
Assignment 7
Task 2
"""

from math import sqrt

x1, y1 = eval(input("Enter coordinates of center of first circle, (x, y): "))
radius1 = eval(input("Enter radius of first circle: "))

x2, y2 = eval(input("Enter coordinates of center of second circle, (x, y): "))
radius2 = eval(input("Enter radius of second circle: "))

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distance > (radius1 + radius2):
    message = "The circles are not touching."
elif distance < (radius1 + radius2) and distance > abs(radius1 - radius2):
    message = "The circles are overlapping."
elif distance < (radius1 + radius2) and distance < abs(radius1 - radius2):
    if radius1 > radius2:
        message = "Circle 2 is inside circle 1."
    else:
        message = "Circle 1 is inside circle 2."
elif distance == (radius1 + radius2):
    message = "The circles aren't overlapping, but they are touching at one point"
else:
    if radius1 > radius2:
        message = "Circle 2 is inside circle 1 with the edges touching at one point"
    else:
        message = "Circle 1 is inside circle 2 with the edges touching at one point"

print(message)