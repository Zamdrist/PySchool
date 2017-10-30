# Chapter 6 Programming Exercises 10 - Springfork Amateur Golf Club
# Author: Steve Schroeder
# Springfork Amateur Golf Club - Adds records. Add exception handling.
#


def main():
    try:
        players = springfork_input()
        golf_file = springfork_processing(players)
        springfork_output(golf_file)
    except ValueError:
        print("Invalid selection. Program ending")
    except IOError:
        print("An error occurred writing the file. Program ending.")


def springfork_input():
    players = int(input("How many golfers would you like to add? "))
    return players


def springfork_processing(players):
    golf_file = open("golf.txt", "w")
    for player in range(1, players + 1):
        player_name = str(input("What is the name of player " + str(player) + "? "))
        player_score = str(input("What is their golf score? "))
        golf_file.write("Name=" + player_name + "\n" + "Score=" + player_score + "\n")
    return golf_file


def springfork_output(golf_file):
    print("File written as " + golf_file.name)
    golf_file.close()


main()