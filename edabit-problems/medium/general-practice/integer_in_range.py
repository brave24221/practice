#!/usr/bin/env python3


# Create a function which validates whether a number n is exclusively
# within the bounds of lower and upper. Return False if n is not an integer.

# Examples
# int_within_bounds(3, 1, 9) ➞ True
# int_within_bounds(6, 1, 6) ➞ False
# int_within_bounds(4.5, 3, 8) ➞ False

# Notes
# Exclusively means that a number is considered not within
# the bounds if it is equal to the upper bound (see example #2)

# Bounds will be always given as intege


def int_within_bounds(n, lower, upper):
    if n in range(lower, upper):
        return True
    elif type(n) != int:
        return False
    else:
        return False
