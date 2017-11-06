# Chapter 7 Lab 8 - Checkpoints
# Author: Steve Schroeder
# Checkpoints 7.1 - 7.25
#

# 7.1
# numbers = [1, 2, 3, 4, 5]
# numbers[2] = 99
# print(numbers)

# 7.2
# numbers = list(range(3))
# print(numbers)

# 7.3
# numbers = [10] * 5
# print(numbers)

# 7.4
# numbers = list(range(1, 10, 2))
# for n in numbers:
#     print(n)

# 7.5
# numbers = [1, 2, 3, 4, 5]
# print(numbers[-2])

# 7.6
# How do you find the number of elements in a list?
# You use the len() function, i.e. print(len(my_list))

# 7.7
# numbers1 = [1, 2, 3]
# numbers2 = [10, 20 , 30]
# numbers3 = numbers1 + numbers2
# print(numbers1)
# print(numbers2)
# print(numbers3)

# 7.8
# numbers1 = [1, 2, 3]
# numbers2 = [10, 20, 30]
# numbers2 += numbers1
# print(numbers1)
# print(numbers2)

# 7.9
# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[1:3]
# print(my_list)

# 7.10
# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[1:]
# print(my_list)

# 7.11
# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[:1]
# print(my_list)

# # 7.12
# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[:]
# print(my_list)

# 7.13
# numbers = [1, 2, 3, 4, 5]
# my_list = numbers[-3:]
# print(my_list)

# 7.14
# names = ["Jim", "Jill", "John", "Jasmine"]
# if "Jasmine" not in names:
#     print("Cannot find Jasmine.")
# else:
#     print("Jasmine's family:")
#     print(names)

# 7.15
# What is the difference between calling a list's remove method
# and using the del statement to remove and element?
# You use the remove method to remove and item from the list by it's value.
# You use the del method to remove an item from the list by index.

# 7.16
# How do you find the lowest and highest value in a list?
# You use the min and max functions.

# 7.17
# names = []
# names.append("Wendy")
# print(names)

# 7.18
# a. index - Index references the position of an item in a list beginning with zero.
# b. insert - Insert inserts a list item at after a given index value
# c. sort - The sort method reorders items in a list from lowest to highest value
# d. reverse - The reverse method reverses the whatever the current order of list items are.

# 7.19
# numbers = [[1,2], [10, 20], [100, 200], [1000, 2000]]
# There are two columns, four rows

# 7.20
# 3 rows, 4 columns
# numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 7.21
# numbers = [[1,2], [10, 20], [100, 200], [1000, 2000]]
# rows = len(numbers)
# columns = len(numbers[0])
# for row in range(rows):
#     for column in range(columns):
#         print(numbers[row][column])

# 7.22
# What is the primary different between a list and a tuple?
# You cannot change the contents of a tuple.

# 7.23
# Give two reasons why tuples exist:
# 1. Performance: A list which cannot change is faster and requires less memory
# 2. Integrity: A read-only list cannot be inadvertently changed.

# 7.24
# my_list = ["list_item"]
# new_tuple = tuple(my_list)

# 7.25
# my_tuple = ("things",)
# my_list = list(my_tuple)
