
# import turtle
import turtle

# define drawChessboard()
    # param -
        # startX
        # startY
        # width - default = 250
        # height - default = 250
def drawChessboard(startX, startY, width=250, height=250):
    # go to starting point
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    # call drawRectangle(width, height)
    drawRectangle(width, height)
    # call drawAllRectangles(width, height)
    drawAllRectangles(startX, startY, width, height)

# define drawAllRectangles()
    # param -
        # width
        # height
def drawAllRectangles(startX, startY, width=250, height=250):
    # loop 8 times
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
                drawRectangle(width / 8, height / 8)
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
                drawRectangle(width / 8, height / 8)
                turtle.end_fill()

# define drawRectangle()
    # param -
        # height
        # width
def drawRectangle(width, height):
    # set heading at 0
    # set speed
    turtle.setheading(0)
    turtle.speed(0)
    # forward width / 8
    turtle.forward(width)
    # left 90
    turtle.left(90)
    # forward height / 8
    turtle.forward(height)
    # left 90
    turtle.left(90)
    # forward width / 8
    turtle.forward(width)
    # left 90
    turtle.left(90)
    # forward height / 8
    turtle.forward(height)


# define done()
def done():
    turtle.done()