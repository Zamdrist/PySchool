# Chapter 7 Programming Exercises 3 - Rainfall Statistics
# Author: Steve Schroeder
# Prompt the user for 12 months of rainfall statistics. Return the total, average, min, max
#
MONTHS = 12


def main():
    try:
        monthly_rainfall = program_input()
        rainfall_stats = program_processing(monthly_rainfall)
        program_output(rainfall_stats)
    except ValueError:
        print("There was a problem with one or more values entered. Please try again.")


def program_input():
    monthly_rainfall = []
    for month in range(MONTHS):
        monthly_rainfall.append(float(input("Rainfall for month " + str(month + 1) + ": ")))
    return monthly_rainfall


def program_processing(monthly_rainfall):
    rainfall_stats = [sum(monthly_rainfall),            # total rainfall
                      sum(monthly_rainfall) / MONTHS,   # average rainfall
                      max(monthly_rainfall),            # maximum rainfall
                      min(monthly_rainfall)]
    return rainfall_stats


def program_output(rainfall_statistics):
    print("Total: " + str(rainfall_statistics[0]))
    print("Average: " + format(rainfall_statistics[1], ".2f"))
    print("Maximum: " + str(rainfall_statistics[2]))
    print("Minimum: " + str(rainfall_statistics[3]))


main()