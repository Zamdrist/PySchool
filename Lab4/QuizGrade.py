# Lab 4
# Author: Steve Schroeder
# For a given quiz score, return the letter grade
#
# Input
score = float(input("Enter quiz score: "))

# Processing and Output
if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("F grade")