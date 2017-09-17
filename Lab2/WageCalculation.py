# Lab 2
# Author: Steve Schroeder
# Calculate paycheck based on regular hours and rate plus over time hours and rate
#
# Input
regularHours = 40
regularRate = 15.34
overtimeHours = 10

# Processing
overtimeRate = regularRate * 1.5
totalPay = (regularRate * regularHours) + (overtimeRate * overtimeHours)

# Output
print("Your will be paid $" +
      str(totalPay),
      "this week")