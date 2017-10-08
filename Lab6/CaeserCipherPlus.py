# Lab 6 Caesar Cipher Plus
# Author: Steve Schroeder
# Ask the user to decrypt/encrypt a word
#

WORD = "Minneapolis"
SHIFT = 6

def main():
    choice = cipher_input()
    if choice == 1:
        word = encrypt()
        cipher_output(word)
    elif choice == 2:
        word = decrypt()
        cipher_output(word)
    elif choice == 3:
        print("Thanks")

def encrypt():
    coded_word = ""
    for letter in WORD:
        coded_letter = chr(ord(letter) + SHIFT) # Add the number (shift) to the ASCII value, return new letter
        coded_word = coded_word + coded_letter # Concatenate letters to make new coded word
    return coded_word


def decrypt():
    coded_word = ""
    for letter in WORD:
        coded_letter = chr(ord(letter) - SHIFT) # Add the number (shift) to the ASCII value, return new letter
        coded_word = coded_word + coded_letter # Concatenate letters to make new coded word
    return coded_word


def cipher_input():
    print("1) Encrypt the word", WORD + "?\n" +
          "2) Decrypt the word", WORD + "?\n" +
          "3) Quit?")
    choice = int(input("Choice: "))
    return choice


def cipher_output(word):
    print(word)


main()