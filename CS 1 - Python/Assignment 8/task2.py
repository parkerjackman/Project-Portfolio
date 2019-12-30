"""
Parker Jackman
Assignment 8
task 2
"""

import random

def play_game():
    decision = input("Do you want to stay with your door or switch? ")
    decision = decision.lower()
    if decision == "stay":
        chosen_door = 1
    else:
        chosen_door = 2
    times_won = 0
    for i in range(1, 100001):
        car_door = random.randint(1, 2)
        if chosen_door == car_door:
            times_won += 1
        else:
            continue
    win_percent = round((times_won / 100000) * 100, 2)
    print("You won", times_won, "times!")
    print("You won " + str(win_percent) + "% of the time")

again = "y"

while again == "y":
    play_game()
    again = input("Do you want to play again (y or n)? ")
    again = again.lower()

print("Thanks for playing!")
