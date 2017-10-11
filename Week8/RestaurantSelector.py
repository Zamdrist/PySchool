# Week 8 Lab: Restaurant Selector
# Author: Steve Schroeder
#
#

JOES = "Joe's Gourmet Hamburgers"
MAINST = "Main Street Pizza Company"
CORNER_CAFE = "Corner Cafe"
MAMAS = "Mama's Fine Italian"
CHEF_KITCHEN = "The Chef's Kitchen"


# Input
vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
glutenFree = input("Is anyone in your [party gluten-free? ")

# Processing
restaurant_choices = ""

if (vegetarian == "yes" or glutenFree == "yes") and vegan == "no": # MAIN ST
    restaurant_choices = MAINST + "\n"
if vegetarian == "yes" or vegan == "yes" or glutenFree == "yes":   # CORNER
    restaurant_choices = restaurant_choices + CORNER_CAFE + "\n"
if vegetarian == "yes" and vegan == "no" and glutenFree == "no":   # MAMAS
    restaurant_choices = restaurant_choices + MAMAS + "\n"
if vegetarian == "yes" or vegan == "yes" and glutenFree == "yes": # CHEFS
    restaurant_choices = restaurant_choices + CHEF_KITCHEN + "\n"
else:                                                              # JOES
    restaurant_choices = JOES + "\n" + CORNER_CAFE + "\n" + CHEF_KITCHEN

# Output
print("Here are your restaurant choices:\n" + restaurant_choices)