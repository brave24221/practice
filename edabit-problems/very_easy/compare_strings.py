#!/usr/bin/env python3

# Create a function that takes two strings as arguments and return
# either True or False depending on whether the total number of characters in
# the first string is equal to the total
# number of characters in the second string.

# Examples:
# comp("AB", "CD") --> True
# comp("ABC", "DE") --> False


def comp(txt1, txt2):
    if len(txt1) == len(txt2):
        return True
    else:
        return False
