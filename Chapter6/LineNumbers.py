# Chapter 6 Programming Exercises 3 - Line Numbers
# Author: Steve Schroeder
# Read file and return the line numbers followed by a colon. Add exception handling.
#


def main():
    try:
        selected_file = program_input()
        return_lines = program_processing(selected_file)
        program_output(return_lines)
    except IOError:
        print("That file does not exist.")


def program_input():
        user_file = input("Name of file to read? ")
        selected_file = open(user_file, "r")
        return selected_file


def program_processing(selected_file):
    line_number = 0
    return_lines = ""
    for lines in selected_file:
        line_number = line_number + 1
        return_lines += str(line_number) + ":" + lines.rstrip() + "\n"
    selected_file.close()
    return return_lines


def program_output(return_lines):
    print(return_lines)


main()
