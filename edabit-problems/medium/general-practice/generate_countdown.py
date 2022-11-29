#!/usr/bin/env python3


# Create a function that takes a number as an argument and returns a list of numbers counting down from this number to zero.

# Examples
# countdown(5) ➞ [5, 4, 3, 2, 1, 0]
# countdown(1) ➞ [1, 0]
# countdown(0) ➞ [0]

# Notes
# The argument will always be greater than or equal to zero.


def countdown(start):
    hold = list(range(start + 1))
    return hold[::-1]
