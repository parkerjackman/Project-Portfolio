"""
Parker Jackman
Assignment 13
Task 2
"""

import random

def main():

    count = [0] * 10

    for i in range(1000):
        num = random.randint(0, 9)
        count[num] += 1

    for i in range(10):
        print(str(i) + "'s: " + str(count[i]))


main()