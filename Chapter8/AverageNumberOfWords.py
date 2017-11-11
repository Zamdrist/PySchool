# Chapter 8 Programming Exercise 6 - Average number of words
# Author: Steve Schroeder
# Read text.txt and return average number of words per sentence
#

FILE = "text.txt"


def main():
    try:
        lines = program_input()
        average_words = program_processing(lines)
        program_output(average_words)
    except IOError:
        print("There was an issue reading the file: " + FILE + ". Program ending.")


def program_input():
    file = open(FILE, "r")
    lines = file.readlines()
    file.close()
    return lines


def program_processing(lines):
    words = 0
    for line in lines:
        words += len(line.rstrip("\n").split()) # here we count the words per line
    average_words = words / len(lines) # here we tally the average number of words for the total lines
    return average_words


def program_output(average_words):
    print("There is an average of " + str(format(average_words, ".1f") + " words per sentence."))


main()