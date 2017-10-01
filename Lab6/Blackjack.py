# Lab 6 Blackjack
# Author: Steve Schroeder
# Deal two random cards with face values, names and suits to a given number of Blackjack players.
import random


def main():
    players = int(blackjack_players())
    blackjack_output(players)


def blackjack_players(): # Input
    players = input("Let's play Blackjack! How many players are playing? ")
    return players


def blackjack_deal(): # Processing
    # Constants for function, scope need not be global
    suit_diamonds = "Diamonds"
    suit_clubs = "Clubs"
    suit_spades = "Spades"
    suit_hearts = "Hearts"
    facecard_jack = "Jack"
    facecard_queen = "Queen"
    facecard_king = "King"

    random_card = random.randint(1, 13)
    random_suit = random.randint(1, 4)

    if random_suit == 1: # determine suit
        suit = suit_diamonds
    elif random_suit == 2:
        suit = suit_clubs
    elif random_suit == 3:
        suit = suit_spades
    elif random_suit == 4:
        suit = suit_hearts
    else:
        suit = ""

    if random_card == 11: # determine face card
        face = facecard_jack
    elif random_card == 12:
        face = facecard_queen
    elif random_card == 13:
        face = facecard_king
    else:
        face = ""

    if random_card >= 11:
        return [face, suit] # return a card having a face and suit
    else:
        return [random_card, suit] # return a card with a number and suit


def blackjack_output(players): # Output
    for player in range(1, players + 1): # loop through number of players
        deal_one = blackjack_deal()
        deal_two = blackjack_deal()
        print("Player", player, "was dealt the", deal_one[0], "of", deal_one[1], "and the", deal_two[0], "of", deal_two[1])

main()
