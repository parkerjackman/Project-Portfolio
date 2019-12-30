"""
Parker Jackman
Assignment 13
Task 3
"""

import turtle
from circle import Circle
from rectangle import Rectangle

def main():

    shapes = []

    done = False

    while not done:
        print("Pick an option:")
        print(" (1) Enter Circle")
        print(" (2) Enter Rectangle")
        print(" (3) Remove Shape")
        print(" (4) Draw Shapes")
        print(" (5) Exit")
        choice = eval(input("What do you want to do? "))

        if choice == 1:
            positionX, positionY = eval(input("Enter center coordinates of the circle: "))
            radius = eval(input("Enter radius of the circle: "))
            print("(0) red")
            print("(1) yellow")
            print("(2) blue")
            print("(3) green")
            color = eval(input("Choose a color: "))

            cir = Circle(positionX, positionY, radius, color)
            shapes.append(cir)

        elif choice == 2:
            positionX, positionY = eval(input("Enter center coordinates of the rectangle: "))
            width = eval(input("Enter width of the rectangle: "))
            height = eval(input("Enter height of the rectangle: "))
            print("(0) red")
            print("(1) yellow")
            print("(2) blue")
            print("(3) green")
            color = eval(input("Choose a color: "))

            rec = Rectangle(positionX, positionY, width, height, color)
            shapes.append(rec)

        elif choice == 3:
            print(len(shapes))
            choice = int(input("Which one do you want to remove? "))
            shapes.pop(choice)

        elif choice == 4:
            turtle.clear()
            for shape in shapes:

                shape.draw()

        else:
            break

        print("Thanks for playing!")


main()