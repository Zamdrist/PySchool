# Bus Fare Program 2
#
regularFare = 1.75
regularRides = 7
rushFare = 3
rushRides = 12

print("Type\t\t"
      "Rides\t\t"
      "Price\t\t"
      "Total Spent"
      "\n" # header

      "Regular\t\t" +
      str(regularRides) + "\t\t\t" +
      "$" + str(regularFare) + "\t\t" +
      "$" + str(regularRides * regularFare) + "\t\t" +
      "\n" # regular
      
      "Rush\t\t" +
      str(rushRides) + "\t\t\t" +
      "$" + str(rushFare) + "\t\t\t" +
      "$" + str(rushRides * rushFare) +
      "\n\n" # rush

      "Total spent on bus rides: $" +
      str((regularFare * regularRides) +
          (rushFare * rushRides)) # total
      )
