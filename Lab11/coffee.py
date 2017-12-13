# Lab 11 - Coffee
# Author: Steve Schroeder
# Expand on the coffee_drink class to include a name property and a function to change price.
#
import coffee_drink


def main():
    try:
        newPrice = 3.50  # as per lab instructions
        coffeeName = "latte" # as per lab instructions
        coffee = program_input()
        coffee = program_processing(coffee, coffeeName, newPrice)
        program_output(coffee)
    except:
        print("An exception occurred, program ending.")
        # PyCharm says this is too broad of an exception


def program_input():
    coffee = coffee_drink.Coffee_Drink() # Initialize coffee class here
    return coffee


def program_processing(coffee, coffeeName, newPrice):
    coffee.setName(coffeeName) # set name
    coffee.setPrice(newPrice) # set price
    return coffee


def program_output(coffee):
    print(coffee)


main()