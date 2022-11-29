#!/usr/bin/env python3


# Create a function that checks if the argument is an integer
# or a string. Return int if it's an integer and str if it's a string.

# Examples
# int_or_string(8) ➞ "int"
# int_or_string("Hello") ➞ "str"
# int_or_string(9843532) ➞ "int"


def int_or_string(var):
    if type(var) == int:
        return 'int'
    elif type(var) == str:
        return "str"
