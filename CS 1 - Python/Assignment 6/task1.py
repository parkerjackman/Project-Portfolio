"""
Parker Jackman
Assignment 6
task 1
"""

import math
from math import pi
from math import tan

numSides = eval(input("Enter the number of sides: "))
sideLength = eval(input("Enter the side length: "))

area = (numSides * math.pow(sideLength, 2)) / (4 * tan(pi / numSides))

print("The area of the polygon is " + str(round(area, 5)))
