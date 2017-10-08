# Chapter 5 Programming Exercises - Paint Job estimator
# Author: Steve Schroeder
# Paint Job Estimator - Ask the user how many square feet they need painted, and how much each gallon of paint costs.
#
# Answer these questions:
#
# Number of gallons of paint required
# Hours of labour
# Cost of paint
# Labour charges
# Total Cost

# Base units of work
BASE_SQUARE_FEET = int(112)
BASE_RATE = float(35.00)
BASE_HOURS = int(8)
BASE_PAINT_GALLONS = int(1)
BASE_ESTIMATE = float(BASE_RATE * BASE_HOURS)


def main():
    sqrft, paint_gallon_cost = paintjob_input()
    gallons, labour_hours, paint_cost, labour_cost, total = paintjob_process(sqrft, paint_gallon_cost)
    paint_cost, labour_cost, total = paintjob_format(paint_cost, labour_cost, total)
    paintjob_output(gallons, labour_hours, paint_cost, labour_cost, total)


def paintjob_input():  # Input
    sqrft = input("How many square feet are to be painted? ")
    paint_gallon_cost = input("How much does each gallon of paint cost? ")
    return int(sqrft), float(paint_gallon_cost)


def paintjob_process(sqrft, paint_gallon_cost):  # Processing
    multiplier = sqrft / BASE_SQUARE_FEET # Use multiplier to derive from base values
    gallons = round(BASE_PAINT_GALLONS * multiplier, 2)
    if gallons % 1 > 0:
        gallons = gallons + 1  # Presumption is you can only buy whole gallons of paint
    labour_hours = round(BASE_HOURS * multiplier, 1)
    paint_cost = round(int(gallons) * paint_gallon_cost, 2)
    labour_cost = round(BASE_HOURS * BASE_RATE * multiplier, 2)
    total = round((BASE_ESTIMATE * multiplier) + paint_cost, 2)
    return int(gallons), labour_hours, paint_cost, labour_cost, total


def paintjob_format(paint_cost, labour_cost, total):  # Formatting
    paint_cost = "$" + str(format(paint_cost, ".2f"))
    labour_cost = "$" + str(format(labour_cost, ".2f"))
    total = "$" + str(format(total, ".2f"))
    return paint_cost, labour_cost, total


def paintjob_output(gallons, labour_hours, paint_cost, labour_cost, total):  # Output
    print("Gallons:", gallons,
          "\nHours:", labour_hours,
          "\nPaint Cost:", paint_cost,
          "\nLabour Cost:", labour_cost,
          "\nTotal:", total)


main()