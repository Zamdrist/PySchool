# Lab 5
# Author: Steve Schroeder
# The While-1 Program
#
import random

# Input
SUIT_DIAMONDS = "diamonds"
SUIT_CLUBS = "clubs"
SUIT_SPADES = "spades"
SUIT_HEARTS = "hearts"
FACECARD_JACK = "jack"
FACECARD_QUEEN = "queen"
FACECARD_KING = "king"

answer = input("Would you like to draw a card from the deck? [Y]es or [N]o? ")

# Processing, Output
while True:
    if answer != "Y":
        break
    randomCard = random.randint(1, 13)
    randomSuit = random.randint(1, 4)

    # Determine which suit was drawn
    if randomSuit == 1:
        suit = SUIT_DIAMONDS
    elif randomSuit == 2:
        suit = SUIT_CLUBS
    elif randomSuit == 3:
        suit = SUIT_SPADES
    elif randomSuit == 4:
        suit = SUIT_HEARTS

    # determine if a face card was drawn and which one
    if randomCard == 11:
        face = FACECARD_JACK
    elif randomCard == 12:
        face = FACECARD_QUEEN
    elif randomCard == 13:
        face = FACECARD_KING
    else:
        face = ""

    # Output like this if a face card was drawn, otherwise just say the number and suit
    if randomCard >= 11:
        print("You drew the",face,"of",suit + ".")
    else:
        print("You drew the",randomCard,"of",suit + ".")

    # Continue or not, otherwise break out
    answer = input("Would you like to draw another card? [Y]es or [N]o? ")
    if answer == "N":
        break

print("Thank you for playing.")


