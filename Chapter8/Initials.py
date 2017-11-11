# Chapter 8 Programming Exercises 1 - Initials
# Author: Steve Schroeder
# Print the initials of a first, middle and last name entered
#


def main():
    try:
        fullname = program_input()
        splitname = program_processing(fullname)
        program_output(splitname)
    except IndexError:
        print("There was a problem with your entry. Please try again.")


def program_input():
    fullname = input("Enter your first, middle and last name. ")
    return fullname


def program_processing(fullname):
    splitname = fullname.split()
    return splitname


def program_output(splitname):
    print(splitname[0][0].upper(),
          splitname[1][0].upper(),
          splitname[2][0].upper(), sep=".")


main()
