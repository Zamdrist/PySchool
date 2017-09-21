# Lab 5
# Author: Steve Schroeder
# Dice rolling program
#
# Input, Processing & Output
import  random

while True:
    first_roll = random.randint(1,6)
    second_roll = random.randint(1,6)
    print("You rolled a", first_roll,"and",second_roll)
    roll_again = input("Enter [N]o to quit or [Y]es to roll the dice again. ")

    if roll_again == "n" or roll_again == "N":
        break
    elif roll_again == "y" or roll_again == "Y":
       continue
    else:
        break
print("Thanks for using the program")