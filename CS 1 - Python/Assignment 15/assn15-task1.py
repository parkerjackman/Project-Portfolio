"""
Parker Jackman
Assignment 15
Task 1
"""

from deck import Deck

def bubbleSort(list):
    count = 0
    swap = True

    while swap:
        swap = False

        for i in range(len(list) - 1):
            if list[i].getCardValue() > list[i + 1].getCardValue():
                list[i], list[i + 1] = list[i + 1], list[i]
                swap = True
                count += 1
                message = str(count) + " ["
                for i in range(len(list)):
                    message += list[i].getNickName() + " "
                message += "]"

                print(message)


def insertionSort(list):
    count = 0
    for i in range(1, len(list)):
        currentCard = list[i]
        j = i - 1
        while j >= 0 and list[j].getCardValue() > currentCard.getCardValue():
            list[j + 1] = list[j]
            list[j] = currentCard
            j -= 1
            count += 1
            message = str(count) + " ["
            for i in range(len(list)):
                message += list[i].getNickName() + " "
            message += "]"

            print(message)


def main():
    deck = Deck()
    deck.shuffle()
    hand = []
    for i in range(20):
        hand.append(deck.draw())

    print("(1) Bubble sort")
    print("(2) Insertion sort")
    sortType = int(input("Sort Type: "))

    if sortType == 1:
        bubbleSort(hand)

    if sortType == 2:
        insertionSort(hand)


main()