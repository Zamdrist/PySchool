# Chapter 6 Programming Exercises 10 - Springfork Amateur Golf Club
# Author: Steve Schroeder
# Springfork Amateur Golf Club -Reads records. Add exception handling.
#

GOLF_FILE = "golf.txt"


def main():
    try:
        golf_file = springfork_input(GOLF_FILE)
        golf_file_contents = springfork_processing(golf_file)
        springfork_output(golf_file_contents)
    except IOError:
        print("File " + GOLF_FILE + " could not be read or found. Program ending.")

def springfork_input(golf_file):
    golf_file = open(golf_file, "r")
    return golf_file


def springfork_processing(golf_file):
    golf_file_contents = golf_file.read()
    golf_file.close()
    return golf_file_contents


def springfork_output(golf_file_contents):
    print(golf_file_contents)



main()