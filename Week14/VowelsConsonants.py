# Chapter 8 Programming Exercises 9 - Vowels and Consonants
# Author: Steve Schroeder
# Week 14
#

VOWELS = ["a", "e", "i", "o", "u"]


def main():

    user_string = program_input()
    vowel_count, consonant_count = program_processing(user_string)
    program_output(vowel_count, consonant_count)


def program_input():
    user_string = input("Enter a string: ")
    return user_string.lower()


def vowels(user_string):
    vowel_hit = 0
    for char in user_string:
        if char in VOWELS:
            vowel_hit = vowel_hit + 1
    return vowel_hit


def consonants(user_string):
    consonant_hit = 0
    for char in user_string:
        if char not in VOWELS and not (ord(char) < ord('a') or ord(char) > ord('z')):
            consonant_hit = consonant_hit + 1
    return consonant_hit


def program_processing(user_string):
    vowel_count = vowels(user_string)
    consonant_count = consonants(user_string)
    return vowel_count, consonant_count


def program_output(vowel_count, consonant_count):
    print(str(vowel_count) + " Vowels", str(consonant_count) + " Consonants")


main()