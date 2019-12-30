

def userMovement(movement, choice):
    if choice == "w":
        if (movement.locationX() - 7.5, movement.locationY() - 7.5 + 15) in movement.possibleMoves():
            movement.goUp()
        else:
            print("You hit a wall")

    if choice == "s":
        if (movement.locationX() - 7.5, movement.locationY() - 7.5 - 15) in movement.possibleMoves():
            movement.goDown()
        else:
            print("You hit a wall")

    if choice == "d":
        if (movement.locationX() - 7.5 + 15, movement.locationY() - 7.5) in movement.possibleMoves():
            movement.goRight()
        else:
            print("You hit a wall")

    if choice == "a":
        if (movement.locationX() - 15 - 7.5, movement.locationY() - 7.5) in movement.possibleMoves():
            movement.goLeft()
        else:
            print("You hit a wall")