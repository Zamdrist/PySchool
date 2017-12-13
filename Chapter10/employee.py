# Chapter 10 Programming Exercises 4 - Employee class
# Author: Steve Schroeder
# Define an employee class with name, id number, department and job title
#


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self._name = name
        self._id_number = id_number
        self._department = department
        self._job_title = job_title

    def __str__(self):
        return self._name + ", " + \
               str(self._id_number) + ", " + \
               self._department + ", " + \
               self._job_title
