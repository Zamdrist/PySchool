# Chapter 6 Programming Exercises 6 - Average of numbers
# Author: Steve Schroeder
# Sum and return average of numbers in file. Add exception handling.
#


def main():
    try:
        user_file = program_input()
        average = program_processing(user_file)
        program_output(average)
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
    count = 0
    average = 0
    for lines in user_file:
        count = count + 1
        sum_lines += int(lines.rstrip())
        average = sum_lines / count
    return average


def program_output(average):
    print("The average of the numbers contained in the file is: " + str(average))


main()