#!/usr/bin/env python3


# The ternary operator (sometimes called Conditional Expressions) in
# python is an alternative to the if... else... statement.

# It is written in the format:

# condition_if_true if condition else condition_if_false
# Ternary operators are more readable than multi-line if statements,
# and allow us to quickly test a condition without
# having to use additional lines and operations.

# For example:

# is_nice = True

# #Using ternary operator
# state = "nice" if is_nice else "not nice"

# #Equivalent code using multi-line if statements
# if is_nice:
    # state = "nice"
# else:
    # state = "not nice"
# Write a function that uses the ternary operator to return "yeah"
# if the condition is True, and "nope" otherwise.

# Examples
# yeahNope(True) ➞ "yeah"
# yeahNope(False) ➞ "nope"


def yeahNope(b):
    if b == True:
        return 'yeah'
    else:
        return 'nope'
