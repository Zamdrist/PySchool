# Lab 11 - Coffee_Drink class
# Author: Steve Schroeder
# Define Coffee_Drink class
#


class Coffee_Drink: # PyCharm says class names should be CamelCase. Using lab name.

    def __init__(self):
        self._name = ""
        self._price = 0.00

    def setPrice(self, price):
        self._price = price

    def setName(self, name):
        self._name = name

    def getPrice(self):
        return self._price

    def getName(self):
        return self._name

    def __str__(self):
        return "Your " + self._name + " costs " + format(self._price, ".2f")
