"""
Parker Jackman
Assignment 14
gubbinsutil code
"""

mano = ["Rock", "Paper", "Scissors"]
coin = ["Heads", "Tails"]
maxCardValue = 20

# Make sure you understand this to do the opposite conversion!!!
def convertCardToValue(cardValue, cardMano, cardCoin):
    return 2 * ((cardValue - 1) + (maxCardValue * mano.index(cardMano))) + coin.index(cardCoin)