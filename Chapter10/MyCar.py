# Chapter 10 Programming Exercises 2 - Car program
# Author: Steve Schroeder
# Create a car class. Accelerate 5 times, brake five times and display the speed
#
import car

ACCELERATE_TIMES = 5
DECELERATE_TIMES = 5


def main():
    try:
        my_car = program_input()
        program_processing(my_car)
    except:
        print("An error occurred. Program ending")
        # Pycharm says this is too broad of an exception


def program_input():
    my_car = car.Car(2018, "Corvette", 0)
    return my_car


def program_processing(my_car):
    print(my_car)
    for accelerate in range(ACCELERATE_TIMES):
        my_car.accelerate()
        program_output("Accelerating..." + str(my_car.get_speed()) + " mph")
    for decelerate in range(DECELERATE_TIMES):
        my_car.brake()
        program_output("Braking..." + str(my_car.get_speed()) + " mph")


def program_output(car_output):
    print(car_output)


main()