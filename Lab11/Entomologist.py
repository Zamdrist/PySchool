# Labb 11 - Entomologist
# Author: Steve Schroeder
# Expand on the insect class to include wing count and color. Print insect info.
#
import insect


def main():
    try:
        ladybug, butterfly, ant = program_input()
        ladybug, butterfly, ant = program_processing(ladybug, butterfly, ant)
        program_output(ladybug, butterfly, ant)
    except:
        print("An exception occurred, program ending.")
        # Pycharm says this is too broad of an exception


def program_input():
    ladybug = insect.Insect("ladybug","red")
    butterfly = insect.Insect("butterfly", "orange")
    ant = insect.Insect("ant", "black")
    return ladybug, butterfly, ant


def program_processing(ladybug, butterfly, ant):
    return str(ladybug), str(butterfly), str(ant)


def program_output(ladybug, butterfly, ant):
    print(ladybug, butterfly, ant, sep="\n")

main()