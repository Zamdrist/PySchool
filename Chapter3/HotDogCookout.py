# Chapter 3 Programming Exercises - #8 Hot Dog Cookout Calculator
# Author: Steve Schroeder
# Calculates the number of hot dog packages and buns needed for a cookout party
#
# Input
HOTDOGSPERPKG = 10 # Number of hot dogs per package
BUNSPERPKG = 8 # Number of buns per package
REMAINDER = 1 # used to round up to next package

peopleAttending = int(input("How many people are attending your hot dog cook out? "))
hotdogsPerPerson = int(input("How many hot dogs will each person be allotted? "))

# Processing
totalHotDogs = peopleAttending * hotdogsPerPerson
totalBuns = totalHotDogs

hotDogPackagesNeeded = totalHotDogs / HOTDOGSPERPKG
if hotDogPackagesNeeded % REMAINDER > 0:
    hotDogPackagesNeeded = hotDogPackagesNeeded + REMAINDER # Extra package needed

bunPackagesNeeded = totalBuns / BUNSPERPKG
if bunPackagesNeeded % REMAINDER > 0:
    bunPackagesNeeded = bunPackagesNeeded + REMAINDER # Extra package needed

leftOverHotDogs = (int(hotDogPackagesNeeded) * HOTDOGSPERPKG) - totalHotDogs
leftOverBuns = (int(bunPackagesNeeded) * BUNSPERPKG) - totalBuns

# Output
print("You need", int(hotDogPackagesNeeded),"hot dog packages and",int(bunPackagesNeeded),"bun packages")
print("You will have",leftOverHotDogs,"left over hot dogs and",leftOverBuns,"left over buns.")