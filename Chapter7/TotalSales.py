# Chapter 1 Programming Exercises 1 - Total Sales
# Author: Steve Schroeder
# Prompts the user for a sales amount for each day of week, then returns the sum
#


def main():
    try:
        daily_sales = program_input()
        total_sales = program_processing(daily_sales)
        program_output(total_sales)
    except ValueError:
        print("There was a problem with one of the values you entered. Please try again.")


def program_input():
    days = 7
    daily_sales = []
    for day in range(days):
        daily_sales.append(float(input("Total sales for day " + str(day + 1) + ": ")))
    return daily_sales


def program_processing(daily_sales):
    total_sales = float(0)
    for sale in daily_sales: # Why use a loop when sum works?
        total_sales = total_sales + sale
    return total_sales


def program_output(total_sales):
    print("Total Sales are $" + format(total_sales, ".2f"))


main()