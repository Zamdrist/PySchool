# Lab 3
# Author: Steve Schroeder
# For a give length and width, print the area of a rectangle
#
# Input
rectangleLength = int(input("What is the length of your rectangle? "))
rectangleWidth = int(input("What is the width of your rectangle? "))

# Processing
rectangleArea = rectangleLength * rectangleWidth

# Output
print("\nThe area of a rectangle is its length multiplied by width.\n"
      "The length of your rectangle is",
      str(rectangleLength) +
      " and the width is",
      str(rectangleWidth) + "\n"
      "The area of your rectangle is",rectangleArea)