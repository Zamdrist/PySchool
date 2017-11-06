# Chapter 7 Programming Exercises 5 - Charge Account Validation
# Author: Steve Schroeder
# Read charge_accounts.txt into list and validate a user supplied number against the list
#


def main():
    try:
        accounts, user_account = program_input()
        is_valid = program_processing(accounts, user_account)
        program_output(is_valid)
    except IOError:
        print("There was a problem reading the validation file.")
    except ValueError:
        print("Validation file, or the number entered to validate, is not of the expected value.")


def program_input():
    file = open("charge_accounts.txt" ,"r")
    accounts = []
    for line in file.readlines():
        accounts.append(int(line.rstrip()))
    file.close()
    user_account = int(input("Account number to validate: "))
    return tuple(accounts), user_account


def program_processing(accounts, user_account):
    is_valid = False
    if user_account in accounts:
        is_valid = True
    return is_valid


def program_output(is_valid):
    if is_valid:
        print("The account number entered is valid.")
    else:
        print("Invalid account number.")


main()