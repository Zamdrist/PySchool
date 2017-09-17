# Lab 3
# Author: Steve Schroeder
# Prompts, calculates and displays the number of and costs of coffee, tea and cappuccino sold
#
# Input
cupsOfCoffeSold = int(input("How many cups of coffee sold? "))
costOfEachCoffee = float(input("What is the cost of each cup of cofee? "))
cupsOfTeaSold = int(input("How many cups of tea sold? "))
costOfEachTea = float(input("What is the cost of each cup of tea? "))
cupsOfCappuccinoSold = int(input("How many cups of cappuccino sold? "))
costOfeachCappuccino = float(input("What is the cost of each cup of cappuccino? "))

# Processing
totalCostOfCoffee = cupsOfCappuccinoSold * costOfEachCoffee
totalCostOfTea = cupsOfTeaSold * costOfEachTea
totalCostOfCappuccino = cupsOfCappuccinoSold * costOfeachCappuccino
total = totalCostOfCoffee + totalCostOfTea + totalCostOfCappuccino

# Output
print(
        "\n"
        "Product\t\t"
        "Price\t\t"
        "Cups Sold\t\t"
        "Total Price\t\t"
        "\n"
        "-------\t\t"
        "-----\t\t"
        "---------\t\t"
        "-----------\t\t"
        "\n"
        "Coffee\t\t$" + format(costOfEachCoffee, ".2f") +
        "\t\t" + str(cupsOfCoffeSold) +
        "\t\t\t\t$" + format(totalCostOfCoffee, ".2f") +
        "\n"
        "Tea\t\t\t$" + format(costOfEachTea, ".2f") +
        "\t\t" + str(cupsOfTeaSold) +
        "\t\t\t\t$" + format(totalCostOfTea, ".2f") +
        "\n"
        "Cappuccino\t$" + format(costOfeachCappuccino, ".2f") +
        "\t\t" + str(cupsOfCappuccinoSold) +
        "\t\t\t\t$" + format(totalCostOfCappuccino, ".2f") +
        "\n\n"
        "Total: $" + format(total, ".2f")
)