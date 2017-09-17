# Lab 3
# Author: Steve Schroeder
# Use various math functions
#
from math import sqrt, pi, sin

# Input
firstNumberToRound = 7.89
secondNumberToRound = 54.345395
numberToSquareRoot = 2
valueToSin = 7

# Processing
firstNumberRounded = int(firstNumberToRound // 1)
secondNumberRounded = round(secondNumberToRound,3)
squareRootOfNumber = sqrt(numberToSquareRoot)
roundedPI = round(pi,3)
sinValue = sin(valueToSin)

# Output
print(firstNumberToRound, "rounded to",firstNumberRounded)
print(secondNumberToRound, "rounded to", secondNumberRounded)
print("The square root of", numberToSquareRoot, "is", squareRootOfNumber)
print("The value of pi is:", pi)
print("The sin value of", valueToSin,"is", sinValue)
print("pi rounded to 3 decimal places is",roundedPI)

