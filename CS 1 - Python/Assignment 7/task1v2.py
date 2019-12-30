"""
Parker Jackman
Assignment 7
This program plays rock, paper, scissors with user (version 2)
"""

import random

person = eval(input("Choose rock (1), paper (2) or scissors (3): "))

computer = random.randint(1, 3)

if person == 1 and computer == 1:
    message = "You and the computer chose rock. It's a draw."
elif person == 1 and computer == 2:
    message = "You chose rock. The computer chose paper. You lost."
elif person == 1 and computer == 3:
    message = "You chose rock. The computer chose scissors. You won."

elif person == 2 and computer == 1:
    message = "You chose paper. The computer chose rock. You won."
elif person == 2 and computer == 2:
    message = "You and the computer chose paper. It's a draw."
elif person == 2 and computer == 3:
    message = "You chose paper. The computer chose scissors. You lost."

elif person == 3 and computer == 1:
    message = "You chose scissors. The computer chose rock. You lost."
elif person == 3 and computer == 2:
    message = "You chose scissors. The computer chose paper. You won."
else:
    message = "You and the computer chose scissors. It's a draw."

print(message)