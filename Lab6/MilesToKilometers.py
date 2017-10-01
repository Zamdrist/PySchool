# Lab 6 Miles to Kilometers
# Author: Steve Schroeder
# For a given number of miles, return the kilometers
KILOMETER_CONVERSION = 1.62


def main():
    miles = getmiles()  # Ask user for miles
    kilometers = getkilometers(miles)  # Process and return kilomters
    returnkilometers(miles, kilometers)  # Print kilometers for given miles


def getmiles():  # Input
    miles = input("Enter number of miles to convert to kilometers. ")
    return miles


def getkilometers(miles):  # Processing
    kilometers = float(miles) * KILOMETER_CONVERSION
    return kilometers


def returnkilometers(miles, kilometers):  # Output
    print(miles, "miles converts", round(kilometers, 3), "kilometers.")


main()
