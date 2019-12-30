"""
Parker Jackman
Assignment 15
Task 2
"""

import time
from deck import Deck

def blackJack():
    done = False
    while not done:
        numPlayers = int(input("# of Players (1 to 5): "))
        if numPlayers < 1:
            print("You have to have at least 1 player.")
        elif numPlayers > 5:
            print("You can only have up to 5 players")
        else:
            done = True

    deck = Deck()

    accounts = [0] * numPlayers
    for i in range(numPlayers):
        accounts[i] = 100

    playAgain = True
    count = 0

    while playAgain:
        bets = [0] * numPlayers

# Player 1 bet
        if accounts[0] > 0:
            if accounts[0] > 5:
                minBet = 5
            else:
                minBet = accounts[0]
            done = False
            while not done:
                print("Player 1, your account has $" + str(accounts[0]))
                bets[0] = int(input("Enter your bet: "))
                if bets[0] < minBet:
                    print("You have to bet at least $" + str(minBet))
                elif bets[0] > accounts[0]:
                    print("You don't have that much money")
                else:
                    done = True

# Player 2 bet
        if numPlayers >= 2 and accounts[1] > 0:
            if accounts[1] > 5:
                minBet = 5
            else:
                minBet = accounts[1]
            done = False
            while not done:
                print("Player 2, your account has $" + str(accounts[1]))
                bets[1] = int(input("Enter your bet: "))
                if bets[1] < minBet:
                    print("You have to bet at least $" + str(minBet))
                elif bets[1] > accounts[1]:
                    print("You don't have that much money")
                else:
                    done = True

# Player 3 bet
        if numPlayers >= 3 and accounts[2] > 0:
            if accounts[2] > 5:
                minBet = 5
            else:
                minBet = accounts[2]
            done = False
            while not done:
                print("Player 3, your account has $" + str(accounts[2]))
                bets[2] = int(input("Enter your bet: "))
                if bets[2] < minBet:
                    print("You have to bet at least $" + str(minBet))
                elif bets[2] > accounts[2]:
                    print("You don't have that much money")
                else:
                    done = True
# Player 4 bet
        if numPlayers >= 4 and accounts[3] > 0:
            if accounts[3] > 5:
                minBet = 5
            else:
                minBet = accounts[3]
            done = False
            while not done:
                print("Player 4, your account has $" + str(accounts[3]))
                bets[3] = int(input("Enter your bet: "))
                if bets[3] < minBet:
                    print("You have to bet at least $" + str(minBet))
                elif bets[3] > accounts[3]:
                    print("You don't have that much money")
                else:
                    done = True

# Player 5 bet
        if numPlayers >= 5 and accounts[4] > 0:
            if accounts[4] > 5:
                minBet = 5
            else:
                minBet = accounts[4]
            done = False
            while not done:
                print("Player 5, your account has $" + str(accounts[4]))
                bets[4] = int(input("Enter your bet: "))
                if bets[4] < minBet:
                    print("You have to bet at least $" + str(minBet))
                elif bets[4] > accounts[4]:
                    print("You don't have that much money")
                else:
                    done = True

        deck.shuffle()
        hands = []
        count += 1
        print("Round " + str(count))
        for i in range(numPlayers + 1):
            hands.append([])
            for j in range(2):
                hands[i].append(deck.draw())

# Player 1 Turn (handValue1, hands[0] and accounts[0])
        if accounts[0] > 0:
            print("Player 1's turn")
            print("Dealer's second card: [" + str(hands[numPlayers][1]) + "]")
            print("Your hand: " + str(hands[0]))
            card1 = hands[0][0].getCardValue() if hands[0][0].getCardValue() <= 10 else 10
            if card1 == 1:
                card1 += 10
            card2 = hands[0][1].getCardValue() if hands[0][1].getCardValue() <= 10 else 10
            if card2 == 1 and card1 < 11:
                card2 += 10
            handValue1 = card1 + card2
            done = False
            while not done:
                choice = int(input("(1) Hit or (2) Hold? "))

                if choice == 1:
                    newCard = deck.draw()
                    if newCard.getRank() == "Ace":
                        newCardVal = 11 if handValue1 <= 10 else 1
                    else:
                        newCardVal = newCard.getCardValue() if newCard.getCardValue() <= 10 else 10
                    hands[0].append(newCard)
                    handValue1 += newCardVal
                    print(hands[0])
                    if handValue1 > 21:
                        print("You busted")
                        break
                else:
                    done = True

# Player 2 Turn (handValue2, hands[1] and accounts[1])
        if numPlayers >= 2 and accounts[1] > 0:
            print("Player 2's turn")
            print("Dealer's second card: [" + str(hands[numPlayers][1]) + "]")
            print("Your hand: " + str(hands[1]))
            card1 = hands[1][0].getCardValue() if hands[1][0].getCardValue() <= 10 else 10
            if card1 == 1:
                card1 += 10
            card2 = hands[1][1].getCardValue() if hands[1][1].getCardValue() <= 10 else 10
            if card2 == 1 and card1 < 11:
                card2 += 10
            handValue2 = card1 + card2
            done = False
            while not done:
                choice = int(input("(1) Hit or (2) Hold? "))

                if choice == 1:
                    newCard = deck.draw()
                    if newCard.getRank() == "Ace":
                        newCardVal = 11 if handValue2 <= 10 else 1
                    else:
                        newCardVal = newCard.getCardValue() if newCard.getCardValue() <= 10 else 10
                    hands[1].append(newCard)
                    handValue2 += newCardVal
                    print(hands[1])
                    if handValue2 > 21:
                        print("You busted")
                        break
                else:
                    done = True

# Player 3 Turn (handValue3, hands[2] and accounts[2])
        if numPlayers >= 3 and accounts[2] > 0:
            print("Player 3's turn")
            print("Dealer's second card: [" + str(hands[numPlayers][1]) + "]")
            print("Your hand: " + str(hands[2]))
            card1 = hands[2][0].getCardValue() if hands[2][0].getCardValue() <= 10 else 10
            if card1 == 1:
                card1 += 10
            card2 = hands[2][1].getCardValue() if hands[2][1].getCardValue() <= 10 else 10
            if card2 == 1 and card1 < 11:
                card2 += 10
            handValue3 = card1 + card2
            done = False
            while not done:
                choice = int(input("(1) Hit or (2) Hold? "))

                if choice == 1:
                    newCard = deck.draw()
                    if newCard.getRank() == "Ace":
                        newCardVal = 11 if handValue3 <= 10 else 1
                    else:
                        newCardVal = newCard.getCardValue() if newCard.getCardValue() <= 10 else 10
                    hands[2].append(newCard)
                    handValue3 += newCardVal
                    print(hands[2])
                    if handValue3 > 21:
                        print("You busted")
                        break
                else:
                    done = True

# Player 4 Turn (handValue4, hands[3] and accounts[3])
        if numPlayers >= 4 and accounts[3] > 0:
            print("Player 4's turn")
            print("Dealer's second card: [" + str(hands[numPlayers][1]) + "]")
            print("Your hand: " + str(hands[3]))
            card1 = hands[3][0].getCardValue() if hands[3][0].getCardValue() <= 10 else 10
            if card1 == 1:
                card1 += 10
            card2 = hands[3][1].getCardValue() if hands[3][1].getCardValue() <= 10 else 10
            if card2 == 1 and card1 < 11:
                card2 += 10
            handValue4 = card1 + card2
            done = False
            while not done:
                choice = int(input("(1) Hit or (2) Hold? "))

                if choice == 1:
                    newCard = deck.draw()
                    if newCard.getRank() == "Ace":
                        newCardVal = 11 if handValue4 <= 10 else 1
                    else:
                        newCardVal = newCard.getCardValue() if newCard.getCardValue() <= 10 else 10
                    hands[3].append(newCard)
                    handValue4 += newCardVal
                    print(hands[3])
                    if handValue4 > 21:
                        print("You busted")
                        break
                else:
                    done = True

# Player 5 Turn (handValue5 and accounts[4])
        if numPlayers >= 5 and accounts[4] > 0:
            print("Player 5's turn")
            print("Dealer's second card: [" + str(hands[numPlayers][1]) + "]")
            print("Your hand: " + str(hands[4]))
            card1 = hands[4][0].getCardValue() if hands[4][0].getCardValue() <= 10 else 10
            if card1 == 1:
                card1 += 10
            card2 = hands[4][1].getCardValue() if hands[4][1].getCardValue() <= 10 else 10
            if card2 == 1 and card1 < 11:
                card2 += 10
            handValue5 = card1 + card2
            done = False
            while not done:
                choice = int(input("(1) Hit or (2) Hold? "))

                if choice == 1:
                    newCard = deck.draw()
                    if newCard.getRank() == "Ace":
                        newCardVal = 11 if handValue5 <= 10 else 1
                    else:
                        newCardVal = newCard.getCardValue() if newCard.getCardValue() <= 10 else 10
                    hands[4].append(newCard)
                    handValue5 += newCardVal
                    print(hands[4])
                    if handValue5 > 21:
                        print("You busted")
                        break
                else:
                    done = True

# Dealer's turn
        print("Dealer's Turn")
        print("[ " + str(hands[numPlayers][0]) + "]")
        print("[ " + str(hands[numPlayers][1]) + "]")
        card1 = hands[numPlayers][0].getCardValue() if hands[numPlayers][0].getCardValue() <= 10 else 10
        if card1 == 1:
            card1 += 10
        card2 = hands[numPlayers][1].getCardValue() if hands[numPlayers][1].getCardValue() <= 10 else 10
        if card2 == 1 and card1 < 11:
            card2 += 10
        dealerHandValue = card1 + card2
        done = False
        while not done:
            time.sleep(1)
            if dealerHandValue > 21:
                print("The dealer busted")
                done = True
            elif dealerHandValue == 21:
                print("The dealer got a Blackjack")
                done = True
            elif dealerHandValue >= 17:
                print("The dealer Holds")
                done = True
            else:
                print("The dealer hits")
                newCard = deck.draw()
                hands[numPlayers].append(newCard)
                dealerHandValue += newCard.getCardValue() if newCard.getCardValue() <= 10 else 10
                print(hands[numPlayers])

# Pay all players still in when dealer busts
        if dealerHandValue > 21:
            print("Everyone who didn't bust won this round!")
            if accounts[0] > 0 and handValue1 <= 21:
                accounts[0] += bets[0]
                print("Player 1, your current balance is $" + str(accounts[0]))
            if numPlayers >= 2 and accounts[1] > 0 and handValue2 <= 21:
                accounts[1] += bets[1]
                print("Player 2, your current balance is $" + str(accounts[1]))
            if numPlayers >= 3 and accounts[2] > 0 and handValue3 <= 21:
                accounts[2] += bets[2]
                print("Player 3, your current balance is $" + str(accounts[2]))
            if numPlayers >= 4 and accounts[3] > 0 and handValue4 <= 21:
                accounts[3] += bets[3]
                print("Player 4, your current balance is $" + str(accounts[3]))
            if numPlayers >= 5 and accounts[4] > 0 and handValue5 <= 21:
                accounts[4] += bets[4]
                print("Player 5, your current balance is $" + str(accounts[4]))

# Pay or deduct from player 1
        if dealerHandValue <= 21 and handValue1 > dealerHandValue and handValue1 <= 21:
            print("Player 1 beat the dealer")
            accounts[0] += bets[0]
        if dealerHandValue <= 21 and handValue1 == dealerHandValue and handValue1 <= 21:
            print("Player 1 tied with the dealer")
        if dealerHandValue <= 21 and handValue1 < dealerHandValue and handValue1 <= 21:
            print("The dealer beat player 1")
            accounts[0] -= bets[0]
        if handValue1 > 21:
            accounts[0] -= bets[0]
        print("Player 1's current balance is $" + str(accounts[0]))

# Pay or deduct from player 2
        if numPlayers >= 2:
            if dealerHandValue <= 21 and handValue2 > dealerHandValue and handValue2 <= 21:
                print("Player 2 beat the dealer")
                accounts[1] += bets[1]
            if dealerHandValue <= 21 and handValue2 == dealerHandValue and handValue2 <= 21:
                print("Player 2 tied with the dealer")
            if dealerHandValue <= 21 and handValue2 < dealerHandValue and handValue2 <= 21:
                print("The dealer beat player 2")
                accounts[1] -= bets[1]
            if handValue2 > 21:
                accounts[1] -= bets[1]
            print("Player 2's current balance is $" + str(accounts[1]))

# Pay or deduct from player 3
        if numPlayers >= 3:
            if dealerHandValue <= 21 and handValue3 > dealerHandValue and handValue3 <= 21:
                print("Player 3 beat the dealer")
                accounts[2] += bets[2]
            if dealerHandValue <= 21 and handValue3 == dealerHandValue and handValue3 <= 21:
                print("Player 3 tied with the dealer")
            if dealerHandValue <= 21 and handValue3 < dealerHandValue and handValue3 <= 21:
                print("The dealer beat player 3")
                accounts[2] -= bets[2]
            if handValue3 > 21:
                accounts[2] -= bets[2]
            print("Player 3's current balance is $" + str(accounts[2]))

# Pay or deduct from player 4
        if numPlayers >= 4:
            if dealerHandValue <= 21 and handValue4 > dealerHandValue and handValue4 <= 21:
                print("Player 4 beat the dealer")
                accounts[3] += bets[3]
            if dealerHandValue <= 21 and handValue4 == dealerHandValue and handValue4 <= 21:
                print("Player 4 tied with the dealer")
            if dealerHandValue <= 21 and handValue4 < dealerHandValue and handValue4 <= 21:
                print("The dealer beat player 4")
                accounts[3] -= bets[3]
            if handValue4 > 21:
                accounts[3] -= bets[3]
            print("Player 4's current balance is $" + str(accounts[3]))

# Pay or deduct from player 5
        if numPlayers == 5:
            if dealerHandValue <= 21 and handValue5 > dealerHandValue and handValue5 <= 21:
                print("Player 5 beat the dealer")
                accounts[4] += bets[4]
            if dealerHandValue <= 21 and handValue5 == dealerHandValue and handValue5 <= 21:
                print("Player 5 tied with the dealer")
            if dealerHandValue <= 21 and handValue5 < dealerHandValue and handValue5 <= 21:
                print("The dealer beat player 5")
                accounts[4] -= bets[4]
            if handValue5 > 21:
                accounts[4] -= bets[4]
            print("Player 5's current balance is $" + str(accounts[4]))

# Play again?
        keepPlaying = input("Do you want to keep playing (y or n)? ").lower()
        if keepPlaying == "y":
            continue
        else:
            playAgain = False

    print("Thanks for playing! Here are the results:")

    players = []
    for i in range(numPlayers):
        players.append(i + 1)

    for i in range(1, numPlayers):
        currentAccount = accounts[i]
        currentPlayer = players[i]
        j = i - 1
        while j >= 0 and accounts[j] < currentAccount:
            accounts[j + 1] = accounts[j]
            accounts[j] = currentAccount
            players[j + 1] = players[j]
            players[j] = currentPlayer
            j -= 1

    for i in range(numPlayers):
        print("Player " + str(players[i]) + " ended with $" + str(accounts[i]))


blackJack()