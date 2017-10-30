# Chapter 6 Programming Exercises 5 - Sum of numbers
# Author: Steve Schroeder
# Read the contents of a file and return the sum of these numbers in the file.
# Add exception handling.
#


def main():
    try:
        user_file = program_input()
        sum_lines = program_processing(user_file)
        program_output(sum_lines)
    except IOError:
        print("That file does not exist. Program ending")
    except ValueError:
        print("One or more of the values in this file are not valid. Program ending.")
    except:
        print("An unknown error occurred. Program ending.")


def program_input():
    user_file = input("What file to read? ")
    return user_file


def program_processing(user_file):
    user_file = open(user_file, "r")
    sum_lines = 0
    for lines in user_file:
        sum_lines += int(lines.rstrip())
    return sum_lines


def program_output(sum_lines):
    print("The sum of the numbers in file is: " + str(sum_lines))


main()