# Lab 11 - insect class
# Author: Steve Schroeder
# Define an insect class
#


class Insect:
    _legs = 6
    _butterflywings = 4
    _ladybugwings = 2
    _wings = 0

    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._wings = self.get_wings()

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_wings(self):
        if self._name.upper() == "butterfly".upper():
            self._wings = self._butterflywings
            return self._wings
        elif self._name.upper() == "ladybug".upper():
            self._wings = self._ladybugwings
            return self._wings
        else:
            return self._wings

    def get_legs(self):
        return self._legs

    def __str__(self):
        return "The " + self.get_name() + \
               " is " + self.get_color() + \
               ", has " + str(self.get_wings()) + " wings" + \
               " and " + str(self.get_legs()) + \
               " legs."
