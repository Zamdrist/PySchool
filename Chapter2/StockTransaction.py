# Chapter 2 Programming exercise 12
# Author: Steve Schroeder
# Calculate Joe's profit/loss for his stock purchase and sale
#
# Input
sharesPurchased = 2000
sharesSold = 2000
purchasePriceShare = 40.00
salePriceShare = 42.75
brokerCommission = 0.03

# Processing
purchasePrice = sharesPurchased * purchasePriceShare
purchasePriceCommission = purchasePrice * brokerCommission
purchasePriceTotal = purchasePrice + purchasePriceCommission

salePrice = sharesSold * salePriceShare
salePriceCommission = salePrice * brokerCommission
salePriceTotal = salePrice + salePriceCommission

profit = salePriceTotal - purchasePriceTotal

# Output
print("Joe purchased", format(sharesPurchased,","), "shares of stock at $" +
      str(format(purchasePriceShare,".2f")),
      "per share, and at a commission of", format(brokerCommission, ".0%"))

print("Joe paid his broker $" +str(format(purchasePriceCommission, ",.2f")), "in commission")
print("Joe's total purchase with commission was $" + str(format(purchasePriceTotal, ",.2f")))

print("Two weeks later Joe sold", format(sharesSold,","), "shares of stock at $" +
      str(format(salePriceShare,".2f")),
      "per share, and at a commission of", format(brokerCommission, ".0%"))

print("Joe paid his broker $" + str(format(salePriceCommission, ",.2f")), "in commission")
print("Joe's total sale with commission was $" + str(format(salePriceTotal, ",.2f")))

print("Joe's profit after the sale was $" + str(format(profit, ",.2f")))