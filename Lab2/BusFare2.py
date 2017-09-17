# Lab 2
# Author: Steve Schroeder
# Bus Fare Program 2
#
# Input
regularFare = 1.75
regularRides = 7
rushFare = 3
rushRides = 12

# Processing
regularTotal = regularRides * regularFare
rushTotal = rushRides * rushFare
totalSpent = (regularFare * regularRides) + (rushFare * rushRides)

# Output
print("Type\t\t"
      "Rides\t\t"
      "Price\t\t"
      "Total Spent"
      "\n"

      "Regular\t" +
      str(regularRides) + "\t\t\t" +
      "$" + str(regularFare) + "\t\t" +
      "$" + str(regularTotal) + "\t\t" +
      "\n"

      "Rush\t\t" +
      str(rushRides) + "\t\t\t" +
      "$" + str(rushFare) + "\t\t\t" +
      "$" + str(rushTotal) +
      "\n\n"

      "Total spent on bus rides: $" +
      str(totalSpent)
      )
