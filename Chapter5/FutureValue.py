# Chapter 5 Programming Exercises - Future Value
# Author: Steve Schroeder
# Future Value: F = P * ((1 + i) ** t)
#
# F = Future value
# P = Present value
# i = Interest rate
# t = Months
#
# Return future value of account for a given interest rate, time and starting value


def main():
    present_value, interest_rate, months = futurevalue_input()
    future_value = futurevalue_process(present_value, interest_rate, months)
    futurevalue_output(future_value)


def futurevalue_input():  # Input
    present_value = float(input("What is the present value of your savings account? "))
    interest_rate = float(input("What is the interest rate? "))
    months = int(input("For how many months shall we calculate future value? "))
    return present_value, interest_rate, months


def futurevalue_process(present_value, interest_rate, months):  # Processing
    future_value = present_value * ((1 + interest_rate) ** months)  # Here we calculate future value based
                                                                    # on the formula provided
    return future_value


def futurevalue_output(future_value):  # Output
    print("The Future Value of your account will be: $" + str(format(future_value, ".2f")))


main()
