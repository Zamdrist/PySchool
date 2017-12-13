# Chapter 10 Programming Exercises 4 - Employee
# Author: Steve Schroeder
# Create three employee objects and print their data
#

import employee


def main():
    try:
        employees = program_input()
        employees_output = program_processing(employees)
        program_output(employees_output)
    except:
        print("An error occurred. Program ending.")
        # Pycharm says this is too broad of an exception


def program_input():
    employees = [employee.Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
                 employee.Employee("Mark Jones", 39119, "IT", "Programmer"),
                 employee.Employee("Joy Rogers", 81744, "Manufacturing", "Engineer")]
    return employees


def program_processing(employees):
    employee_output = ""
    for employee_named in employees:
        employee_output += str(employee_named) + "\n"
    return employee_output


def program_output(employee_output):
    print(employee_output)


main()