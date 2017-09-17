# Chapter 2 Programming exercise 6
# Author: Steve Schroeder
# Calculate the total purchase including state and county sales tax
#
# Input
stateTax = .05
countyTax = .025
purchase = float(input("What is the amount of your purchase? "))

# Processing
stateTaxOnPurchase = purchase * stateTax
countyTaxOnPurchase = purchase * countyTax
totalTaxOnPurchase = stateTaxOnPurchase + countyTaxOnPurchase
totalPurchaseWithTax = purchase + totalTaxOnPurchase

# Output
print("The original amount of your purchase is $" + str(format(purchase, ".2f")))
print("The state sales tax of", format(stateTax, ".0%"), "is $" + str(format(stateTaxOnPurchase, ".2f")))
print("The county sales tax of", format(countyTax, ".1%"), "is $" + str(format(countyTaxOnPurchase, ".2f")))
print("The total sales tax on your purchase is $" + str(format(totalTaxOnPurchase, ".2f")))
print("Your purchase including state and county sales tax is $" + str(format(totalPurchaseWithTax, ".2f")))