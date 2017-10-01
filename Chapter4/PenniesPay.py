# Chapter 4 Programming Exercises - #7 Pennies for Pay
# Author: Steve Schroeder
# Show pay for number of days per penny, doubled each day
#
# Input
days = int(input("For how many days were you paid? "))
pay = 0
totalPennies = 0
payString = ""
# Processing

for day in range(days):
    pay = day ** 2
    totalPennies += pay
    payString = payString + "\n" + "Your pay for day " + str(day + 1) + " was $" + str(float(format(pay * .01, ".2f")))
totalPay = totalPennies * .01
# Output
print(payString)
print("Your total pay was $" + str(float(format(totalPay, ".2f"))))