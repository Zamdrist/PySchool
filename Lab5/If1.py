# Lab 5
# Author: Steve Schroeder
# The If-1 Program
#
# Input
DOLLAR_CENTS = 100

cents = int(input("How many cents do you have? "))
# Processing, Output
while cents < 0:
  print("Not a valid number of cents, please enter a whole positive number")
  cents = int(input("How many cents do you have? "))
if cents > DOLLAR_CENTS:
    print(cents,"cents is more than one dollar")
elif cents == DOLLAR_CENTS:
    print("You have exactly one dollar in cents.")
elif cents > 0 and cents < DOLLAR_CENTS:
    print(cents, "is less than one dollar in cents")

