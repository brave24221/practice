#!/usr/bin/env python3


# Create a function that takes a letter and returns the next letter in the alphabet

# Examples
# a ➞ b
# x ➞ y
# z ➞ a

# Notes
# -'z' should return 'a'
# -only 1 letter will be inputted


def next_letter(n):
    hold = ord(n)
    if chr(hold) == 122:
        return chr(97)

    return chr(hold + 1)
