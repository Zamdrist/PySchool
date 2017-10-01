# Lab 6 Lemonade and Cookie Stand Profit
# Author: Steve Schroeder
# For lemonades and cookies, ask what the cost and sale prices were,
# as well as the number sold. Return profits for each.
#


def main():
    for word in {"lemonade", "cookie"}:  # Loop for each item, lemonades and cookies.
        def item_input():  # Inputs
            cost_item = input("What is the cost per " + word + "? ")
            sale_item = input(f"What is the sale price per {word}? ")
            number_items = input("How many " + word + "s were sold? ")
            return cost_item, sale_item, number_items

        # Processing
        def item_processing(cost_item, sale_item, number_items):
            total_cost = float(cost_item) * float(number_items)
            total_sale = float(sale_item) * float(number_items)
            profit = total_sale - total_cost
            return total_cost, total_sale, profit

        # Outputs
        def item_output(totalCost, totalSale, profit):
            print("The total cost of", word, "was $" +
                  format(totalCost, ".2f") + ", the total sales were $" +
                  format(totalSale, ".2f") + " and your proft was $" + format(profit, ".2f"))

        # Call inputs, processing and outputs
        cost_item, sale_item, number_items = item_input()
        total_cost, total_sale, profilt = item_processing(cost_item, sale_item, number_items)
        item_output(total_cost, total_sale, profilt)


main()
