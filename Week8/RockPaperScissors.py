# Week 8 Lab: Rock, Paper, Scissors
# Author: Steve Schroeder
#
#
import random


def main():
    selected = rps_input()
    computer = rps_processing()
    outcome = rps_outcome(selected, computer)
    rps_output(selected, computer, outcome)


def rps_input():
    user_choice = input("(r)ock, (p)aper, (s)cissors? ")
    if user_choice == "r":
        return "rock"
    if user_choice == "p":
        return "paper"
    if user_choice == "s":
        return "scissors"
    else:
        exit(1)


def rps_processing():
    rps = random.randint(1, 3)
    if rps == 1:
        return "rock"
    if rps == 2:
        return "paper"
    if rps == 3:
        return "scissors"


def rps_outcome(selected, computer):

    if selected == "rock" and computer == "paper":
        return "Computer wins!"
    if selected == "paper" and computer == "rock":
        return "You win!"
    if selected == "scissors" and computer == "rock":
        return "Computer wins!"
    if selected == "rock" and computer == "scissors":
        return "You win!"
    if selected == "paper" and computer == "scissors":
        return "Computer Wins!"
    if selected == "scissors" and computer == "paper":
        return "You win!"
    else:
        return "We tied!"


def rps_output(selected, computer, outcome):
    print("You: " + selected + "\nComputer: " + computer + "\n" + outcome)

main()



