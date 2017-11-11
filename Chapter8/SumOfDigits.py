# Chapter 8 Programming Exercises 2 - Sum of digits in string
# Author: Steve Schroeder
# Return the sum of a string of digits
#


def main():
    try:
        digits = program_input()
        summation = program_processing(digits)
        program_output(summation)
    except ValueError:
        print("Please enter whole integers only. Program ending.")


def program_input():
    digits = input("Please enter a series of whole integers (digits): ")
    return digits


def program_processing(digits):
    if len(digits) == 0:
        exit(0)
    summation = 0
    for digit in digits:
        # cast each character passed as int so that we raise a ValueError if not an int
        summation = summation + int(digit)
    return summation


def program_output(summation):
    print("The sum of your digits is: " + str(summation))


main()