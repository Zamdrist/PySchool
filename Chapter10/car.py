# Chapter 10 Programming Exercises 2 - Car Class
# Author: Steve Schroeder
# Define a car class with methods: accelerate, brake and get_speed
#


class Car:
    _accelerate = 5
    _brake = 5

    def __init__(self, year_model, make, speed):
        self._year_model = year_model
        self._make = make
        self._speed = speed

    def accelerate(self):
        self._speed = self._speed + self._accelerate

    def brake(self):
        if self._speed != 0:
            self._speed = self._speed - self._brake

    def get_speed(self):
        return self._speed

    def __str__(self):
        return str(self._year_model) + " " + self._make + "...vroom!"
