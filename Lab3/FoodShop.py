# Lab 3
# Author: Steve Schroeder
# For a given food item price, show the discounted price
#
# Input
loyaltyCardDiscount = float(0.05)
fullPrice = float(input("What is the full price of your food item? "))

# Processing
discountedPrice = float(fullPrice - (fullPrice * loyaltyCardDiscount))
amountSaved = float(fullPrice - discountedPrice)

# Output
print("The full price of your item was: $" +
      format(fullPrice,".2f") +
      "\n"
      "The discounted price of your item is: $" +
      format(discountedPrice, ".2f") +
      "\n"
      "You saved: $" +
      format(amountSaved, ".2f") +
      "\n"
      "Thank you for shopping with us!"
      )
