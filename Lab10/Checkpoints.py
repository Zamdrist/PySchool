# Chapter 9 Lab 10 - Checkpoints
# Author: Steve Schroeder
# Checkpoints 9.1 - 9.38
#

# 9.1 An element in a dictionary has two parts. What are they called?
# Key, Value

# 9.2 Which part of the dictionary element must be immutable?
# Key

# 9.3 Suppose 'start' : 1472 is an element in a dictionary. What is the key, what is the value?
# Key: 'start', Value: 1472

# 9.4
# Suppose a dictionary named employee has been created. What does the following statement do?
# employee['id'] = 54321
# Assigns the key 'id' to the value of 54321

# 9.5
# What will the following code display?
# stuff = {1 : "aaa", 2: "bbb", 3 : "ccc"}
# print(stuff[3])
# Prints the third element, "ccc"

# 9.6
# How can you determine whether a key-value pair exist in a dictionary?
# Use the In statement to return a boolean.

# 9.7
# Suppose a dictionary named inventory exists. What does the following statement do?
# del inventory[654]
# Deletes the item with a key of 654

# 9.8
# What will the following code display?
# stuff = {1 : "aaa", 2: "bbb", 3 : "ccc"}
# print(len(stuff))
# Prints the number of elements in the dictionary named 'stuff'

# 9.9
# What will the following code display?
# stuff = {1 : "aaa", 2: "bbb", 3 : "ccc"}
# for k in stuff:
#     print(k)
# Prints the names of the keys in the dictionary.

# 9.10
# What is the difference between the dictionary methods pop and popitem?
# The method pop returns and removes a specified key-value pair. The method
# popitem returns and removes a random key-value pair.

# 9.11
# What does the items moth return?
# Returns the dictionary's key-value pairs.

# 9.12
# What does the keys method rewturn?
# Returns the dictionary's keys

# 9.13
# What does the values method return?
# Returns the dictionary's values

# 9.14
# Are the elements of a set ordered or unordered?
# They are unordered

# 9.15
# Does a set allow you to store duplicate elements?
# No

# 9.16
# How do you create an empty set?
# myset = set()

# 9.17
# After the following statement executes, what elements will be stored in the myset set?
# myset = set("Jupiter")
# {'J', 'i', 't', 'u', 'e', 'p', 'r'}

# 9.18
# After the following statement executes, what elements will be stored in the myset set?
# myset = set(25)
# Nothing, produces TypeError

# 9.19
# After the following statement executes, what elements will be stored in the myset set?
# myset = set("www xxx yyy zzz")
# {'x', 'w', ' ', 'y', 'z'}

# 9.20
# After the following statement executes, what elements will be stored in the myset set?
# myset = set([1, 2, 2, 3, 4, 4, 4])
# {1, 2, 3, 4}

# 9.21
# After the following statement executes, what elements will be stored in the myset set?
# myset = set(["www", "xxx", "yyy", "zzz"])
# {'xxx', 'yyy', 'zzz', 'www'}

# 9.22
# How do you dtermine the number of elements in a set?
# Use the len function.

# 9.23
# After the following statement executes, what elements will be stored in the myset set?
# myset = set([10, 9, 8])
# myset.update([1, 2, 3])
# {1, 2, 3, 8, 9, 10}

# 9.24
# After the following statement executes, what elements will be stored in the myset set?
# myset = set([10, 9, 8])
# myset.update("abc")
# {'c', 8, 9, 10, 'a', 'b'}

# 9.25
# What is the different between remove and discard?
# The remove method will raise a KeyError if the element specified does not exist. Discard will not raise an error.

# 9.26
# How can you dtermine whether a specified element exists in a set?
# Use the In and Not In operators

# 9.27
# After the following code executes, what elements will be members of set3?
# set1 = set([10, 20, 20])
# set2 = set([100, 200, 300])
# set3 = set1.union(set2)
# {20, 100, 200, 10, 300}

# 9.28
# After the following code executes, what elements will be members of set3?
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.intersection(set2)
# {3, 4}

# 9.29
# After the following code executes, what elements will be members of set3?
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set1.difference(set2)
# {1, 2}

# 9.30
# set1 = set([1, 2, 3, 4])
# set2 = set([3, 4, 5, 6])
# set3 = set2.difference(set1)
# {5, 6}

# 9.31
# After the following code executes, what elements will be members of set3?
# set1 = set(['a', 'b', 'c'])
# set2 = set(['b', 'c', 'd'])
# set3 = set1.symmetric_difference(set2)
# {'a', 'd'}

# 9.32
# Look at the following code:
# set1 = set([1, 2, 3, 4])
# set2 = set([2, 3])
# set2 is a subset of set1
# set1 is a superset of set2

# 9.33
# What is object serialization?
# The process of converting an object of bytes to a file

# 9.34
# When you open a file for the purpose of saving a pickled object to it, what
# file access mode do you use?
# wb, binary writing

# 9.35
# When you open a file for the purposes of retrieving a pickled object from it, what
# file access do you use?
# rb, binary read

# 9.36
# What module do you import if you want to pickle objects?
# import pickle

# 9.37
# What function do you call to pickl an object?
# pickle

# 9.38
# What function do you call to retrieve and unpickle an object?
# open, and pickle.load
