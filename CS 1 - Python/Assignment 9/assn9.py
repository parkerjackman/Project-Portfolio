'''
Parker Jackman
Assignment 9
This program draws a chessboard based on input from user
'''

#### Add Import Statement(s) as needed ####
import chessboard
from chessboard import drawChessboard

#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startX, startY = eval(input("Enter starting coordinates (x, y): "))
    height = input("Enter height of chessboard: ")
    width = input("Enter width of chessboard: ")

    #### End Add Code to get input from user ####
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))

    chessboard.done()


main()
