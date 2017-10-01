# Lab 6 Caesar Cipher
# Author: Steve Schroeder
# For a given word and number, shift each letter of word the number of times, return the coded word
#


def main():
    word, shift = cipher_input()
    coded_word = cipher(word, int(shift))
    cipher_output(word, coded_word)


def cipher_output(word, coded_word): # Output
    print(word, "in code is", coded_word)


def cipher(word, shift): # Processing
    coded_word = ""
    for letter in word:
        coded_letter = chr(ord(letter) + shift) # Add the number (shift) to the ASCII value, return new letter
        coded_word = coded_word + coded_letter # Concatenate letters to make new coded word
    return coded_word


def cipher_input(): # Input
    word = input("Which word would you like to encrypt? ")
    shift = input("By how many characters do you wish to encrypt by? ")
    return word, shift


main()
