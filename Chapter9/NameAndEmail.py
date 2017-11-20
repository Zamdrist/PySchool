# Chapter 9 Programming Exercises 8 - Name and Email Addresses
# Author: Steve Schroeder
# Write a program that keeps nameas and e-mail addresses in a dictionary as key-value pairs.
#
import pickle

DATAFILE = "names_addresses.dat"


def main():
    try:
        choice = program_input()
        program_processing(choice)
    except IOError:
        print("There was a problem reading from the file. Creating file from scratch.")
        initialize() # create the pickle file if it does not exist
    except KeyError:
        print("There was an error processing the dictionary.")
    except EOFError:
        serialize({}) # initialize pickle with an empty dictionary


def initialize():
    data_file = open(DATAFILE, "wb")
    pickle.dump({}, data_file)
    data_file.close()


def serialize(names_addresses):
    data_file = open(DATAFILE, "wb")
    pickle.dump(names_addresses, data_file)
    data_file.close()
    print(DATAFILE, "written to disk.")


def deserialize():
    data_file = open(DATAFILE, "rb")
    names_address = pickle.load(data_file)
    data_file.close()
    return names_address


def program_input():
    menu, menu_list = menu_options()
    print(menu_list)
    choice = input("Choose an option from the menu: ").upper()
    return choice


def menu_options():
    menu = {"L": "(L)ookup", "A": "(A)dd", "C": "(C)hange", "D": "(D)elete", "S": "(S)how list", "Q": "(Q)uit"}
    menu_list = "\nNames and Email Addresses\n-------------------------\n"
    for menu_item in menu:
        menu_list += menu[menu_item] + "\n"
    return menu, menu_list


def program_processing(choice):

    again = "C"
    names_addresses = deserialize()

    if choice == "Q":
        exit()

    while again == "C":
        if choice == "L":
            lookup(names_addresses)
        elif choice == "A":
            add(names_addresses)
        elif choice == "C":
            change(names_addresses)
        elif choice == "D":
            delete(names_addresses)
        elif choice == "S":
            show(names_addresses)

        again = input("\n(C)ontinue or (Q)uit? ").upper()
        if again == "Q":
            exit()
        else:
            main()

    return


def lookup(names_addresses):
    lookup_value = input("Name to look up: ")
    if lookup_value in names_addresses:
        print(lookup_value, names_addresses[lookup_value])
    else:
        print("Name not found in list")


def add(names_addresses):
    name = input("Name: ")
    address = input("Address: ")
    names_addresses[name] = address
    serialize(names_addresses)


def change(names_addresses):
    change_entry = input("Entry to change: ")
    change_value = input("New address: ")
    if change_entry in names_addresses:
        names_addresses[change_entry] = change_value
        serialize(names_addresses)
    else:
        print("Name not found in list")


def delete(names_addresses):
    delete_entry = input("Name to delete from list: ")
    if delete_entry in names_addresses:
        del names_addresses[delete_entry]
        serialize(names_addresses)
    else:
        print("Entry does not exist in list.")


def show(names_addresses):
    for key in names_addresses:
        print(key, names_addresses[key])

main()