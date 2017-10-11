# Week 8 Lab: Distance Traveled
# Author: Steve Schroeder
#
#


def main():
    speed, hours = distance_input()
    table = distance_processing(speed, hours)
    distance_ouput(table)


def distance_input():
    speed = int(input("What is the speed of the vehicle in mph? "))
    hours = int(input("For how many hours did the vehicle travel? "))
    return speed, hours


def distance_processing(speed, hours):
    table = ""
    header = "Hour\t\tDistance\n----\t\t------\n"
    for hour in range(1, hours + 1):
        table = table + str(hour) + "\t\t\t" + str((hour) * speed) + "\n"
    return header + table


def distance_ouput(table):
    print(table)


main()
