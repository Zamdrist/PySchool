# Lab 11 - room class
# Author: Steve Schroeder
# Define a room class
#


class Room():
    _coverage = 350

    def __init__(self, l, w, h, name):
        self._length = l
        self._width = w
        self._height = h
        self._room_name = name
        self._paint_gallons = 0
        self._color = ""

    def setColor(self, color):
        self._color = color

    def getColor(self):
        return self._color

    def setPaint_needed(self, coats = 1):
        area = (self._length * self._height * 2) + (self._width * self._height * 2)
        paint_gallons = (area / self._coverage) * coats
        self._paint_gallons = int(paint_gallons * 100) / 100.0

    def __str__(self):
        return "The " + self._room_name + \
               " required " + str(self._paint_gallons) + \
               " gallons of " + self.getColor() + " paint."
