# Chapter 8 Lab 9 - Checkpoints
# Author: Steve Schroeder
# Checkpoints 8.1 - 8.19
#

#8.1
# name = "Steve"
# for char in name:
#     print(char)

# 8.2
# What is the index of the first character of the string?
# 0

# 8.3
# If a string has 10 characters what is the index of the last character?
# 9

# 8.4
# what happens if you try to use an invalid index to access a character in a string?
# An IndexError exception is raised

# 8.5
# How do you find the lenth of a string?
# Use the len() function.

# 8.6
# What is wring with the following code?
# animal = "Tiger"
# animal[0] = "L"
# String are immutable

# 8.7
# What will the following code display?
# mystring = "abcdefg"
# print(mystring[2:5])
# cde

# 8.8
# What will the following code display?
# mystring = "abcdefg"
# print(mystring[3:])
# defg

# 8.9
# What will the following code display?
# mystring = "abcdefg"
# print(mystring[:3])
# abc

# 8.10
# What will the following code display?
# mystring = "abcdefg"
# print(mystring[:])
# abcdefg

# 8.11
# Write code using the in operator to determine whether 'd' is in mystring
# mystring = "Whatever"
# if "d" in mystring:
#     print("'d' is found in mystring")
# else:
#     print("'d' is not found in mystring")

# 8.12
# big = "BIG"
# little = big.lower()
# print(little)

# 8.13
# my_variable = "Zipper5"
# for ch in my_variable:
#     if ch.isdigit():
#         print("Digit")
#     else:
#         print("No Digit")

# 8.14
# what is the output of the following code?4
# ch = "a"
# ch2 = ch.upper()
# print(ch, ch2)
# a A

# 8.15
# answer = "R"
# while (answer.upper() != "R" or answer.upper() != "Q"):
#     answer = input("Do you want to repeat the program or quit? (R/Q)? ")
#     if answer.upper() == "Q":
#         exit()

# 8.16
# var = "$"
# print(var.upper())
# $

# 8.17
# upper_count = 0
# myString  = "Steve"
# for char in myString:
#     if char.isupper():
#         upper_count += 1
# print(upper_count)

# 8.18
# days = "Monday Tuesday Wednesday"
# threedays = days.split()
# print(threedays)

# 8.19
values = "one$two$three$four"
value_list = values.split("$")
print(value_list)





