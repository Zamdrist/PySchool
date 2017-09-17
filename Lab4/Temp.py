# Lab 4
# Author: Steve Schroeder
# For a given temperature, return if above, at or below zero
#
# Input
temp = float(input("Enter the temperature: "))

# Processing and Output
if temp > 0:
    print("The temperature is greater than 0")
elif temp == 0:
    print("The temperature is exactly 0")
elif temp < 0:
    print("The temperature is less than 0")

print("End of program")
