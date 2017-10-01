# Chapter 4 Programming Exercises - #5 Average Rainfall
# Author: Steve Schroeder
# Calculate average rainfall for number of years
#
# Input
MONTHS = 12
years = int(input("For how many years do you wish to calculate the average rainfall? "))
yearTotal = 0 # Running total of inches for number of years
totalMonths = 0 # Running total of months for number of years

# Processing
for year in range(1, years + 1):
    for month in range(1, MONTHS + 1):
        averageForMonth = int(input("What was the average inches of rainfall for month " +
                                    str(month) + " in year " +
                                    str(year) + "? "))
        yearTotal = yearTotal + averageForMonth
        totalMonths += 1
averageTotal = round(yearTotal / totalMonths,3)

# Output
print("The average inches of rainfall for",totalMonths,
      "months was", str(averageTotal) +
      ". The total inches of rainfall was", yearTotal)