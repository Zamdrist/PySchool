# Lab 4
# Author: Steve Schroeder
# when did Apollo 11 land on the moon? Print correct or wrong answer
#
# Input
APOLLO11_LANDING = 1969
year = int(input("When did Apollo 11 land on the moon? "))

# Processing and Output
if year != APOLLO11_LANDING:
    print("Sorry, wrong answer")
else:
    print("Correct!")