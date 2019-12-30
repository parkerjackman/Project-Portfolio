"""
Parker Jackman
Assignment 14
Task 3
"""

from deck import Deck
import gubbinsutil
mano = ["Rock", "Paper", "Scissors"]
coin = ["Heads", "Tails"]

def sortByValue(list):
    for i in range(1, len(list)):
        currentCard = list[i]
        j = i - 1
        while j >= 0 and list[j].getValue() > currentCard.getValue():
            list[j + 1] = list[j]
            list[j] = currentCard
            j -= 1

def sortById(list):
    for i in range(1, len(list)):
        currentCard = list[i]
        j = i - 1
        while j >= 0 and gubbinsutil.convertCardToValue(list[j].getValue(), list[j].getMano(), list[j].getCoin()) >\
                        gubbinsutil.convertCardToValue(currentCard.getValue(), currentCard.getMano(), currentCard.getCoin()):
            list[j + 1] = list[j]
            list[j] = currentCard
            j -= 1

def displayHand(list):
    for i in range(len(list)):
        print(str(list[i]))


def main():
    deck = Deck()
    hand = []
    for i in range(30):
        hand.append(deck.draw())

    displayHand(hand)

    done = False

    while not done:
        print("(1) Sort by value")
        print("(2) Sort by ID")
        print("(3) Find card")
        print("(4) New Hand")
        print("(5) Quit")
        choice = int(input("What do you want to do? "))

        if choice == 1:
            sortByValue(hand)
            displayHand(hand)

        elif choice == 2:
            sortById(hand)
            displayHand(hand)

        elif choice == 3:
            wantedValue = int(input("Enter a Value to search for: "))
            print("(0) Rock")
            print("(1) Paper")
            print("(2) Scissors")
            choice1 = int(input("Choose Mano: "))
            if choice1 == 0:
                wantedMano = "Rock"
            if choice1 == 1:
                wantedMano = "Paper"
            if choice1 == 2:
                wantedMano = "Scissors"

            print("(0) Heads")
            print("(1) Tails")
            choice2 = int(input("Choose Coin: "))
            if choice2 == 0:
                wantedCoin = "Heads"
            if choice2 == 1:
                wantedCoin = "Tails"

            wantedCardId = gubbinsutil.convertCardToValue(wantedValue, wantedMano, wantedCoin)

            found = False
            for i in range(len(hand)):
                currentCardId = gubbinsutil.convertCardToValue(hand[i].getValue(), hand[i].getMano(), hand[i].getCoin())
                found = False
                if currentCardId == wantedCardId:
                    found = True
                    break

            if found:
                print("That card is in your hand!")
            else:
                print("That card is not in your hand.")

        elif choice == 4:
            deck.shuffle()
            hand = []
            for i in range(30):
                hand.append(deck.draw())

            displayHand(hand)

        elif choice == 5:
            break

        else:
            print("Invalid Input")

    print("Thanks for playing!")


main()