# Lab 6 Lemonade Stand Profit
# Author: Steve Schroeder
#


def main():
    # cost_cup = 0
    # sale_cup = 0
    # number_cups = 0
    # totalCost = 0
    # total_sale = 0
    # profit = 0
    cost_cup, sale_cup, number_cups = lemonade_input()
    total_cost, total_sale, profilt = lemonade_processing(cost_cup,sale_cup, number_cups)
    lemondate_output(total_cost,total_sale,profilt)


def lemonade_input():
    cost_cup = input("What is the cost per cup? ")
    sale_cup = input("What is the sale price per cup? ")
    number_cups = input("How many cups of lemonade were sold? ")
    return cost_cup, sale_cup, number_cups


def lemonade_processing(cost_cup, sale_cup, number_cups):
    total_cost = float(cost_cup) * float(number_cups)
    total_sale = float(sale_cup) * float(number_cups)
    profit = total_sale - total_cost
    return total_cost, total_sale, profit


def lemondate_output(totalCost, totalSale, profit):
    print("The total cost of lemonade was $" +
          format(totalCost, ".2f") + ", the total sales were $" +
          format(totalSale, ".2f") + " and your proft was $" + format(profit, ".2f"))

main()