# Chapter 3 Programming Exercises - #13 Shipping Charges
# Author: Steve Schroeder
# For a given weight of package and for a known sets of rates, display the cost of shipping
#
# Input
MINIMUM_WEIGHT = 1
LOWER_WEIGHT = 2
MIDDLE_WEIGHT = 6
UPPER_WEIGHT = 10

LOWER_WEIGHT_RATE = float(1.50)
MIDDLE_WEIGHT_RATE = float(3.00)
UPPER_WEIGHT_RATE = float(4.00)
OVER_WEIGHT_RATE = float(4.75)
OUTPUT_RATE = float(0)

# Processing
weightOfPackage = float(input("What is the weight of the package you want to ship? "))
shippingCost = float(0)

if weightOfPackage < MINIMUM_WEIGHT:
    shippingCost = MINIMUM_WEIGHT * LOWER_WEIGHT_RATE # Cost not lover than minimum rate
elif weightOfPackage <= LOWER_WEIGHT:
    shippingCost = weightOfPackage * LOWER_WEIGHT_RATE
elif weightOfPackage > LOWER_WEIGHT and weightOfPackage <= MIDDLE_WEIGHT:
    shippingCost = weightOfPackage * MIDDLE_WEIGHT_RATE
elif weightOfPackage > MIDDLE_WEIGHT and weightOfPackage <= UPPER_WEIGHT:
    shippingCost = weightOfPackage * UPPER_WEIGHT_RATE
else:
    shippingCost = weightOfPackage * OVER_WEIGHT_RATE

if weightOfPackage < MINIMUM_WEIGHT:
    OUTPUT_RATE = LOWER_WEIGHT_RATE # Rate not lover than minimum rate
else:
    OUTPUT_RATE = shippingCost / weightOfPackage

# Output
print("Your package will cost $" +
      format(shippingCost,".2f"),"to ship at a rate of $" +
      str(format(OUTPUT_RATE, ".2f")), "per pound.")