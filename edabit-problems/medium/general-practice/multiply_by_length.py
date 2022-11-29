#!/usr/bin/env python3


# Create a function to multiply all of the values in a list by the amount of values in the given list.

# Examples
# MultiplyByLength([2, 3, 1, 0]) ➞ [8, 12, 4, 0]
# MultiplyByLength([4, 1, 1]) ➞ ([12, 3, 3])
# MultiplyByLength([1, 0, 3, 3, 7, 2, 1]) ➞  [7, 0, 21, 21, 49, 14, 7]
# MultiplyByLength([0]) ➞ ([0])

# Notes
# All of the values given are numbers.
# All lists will have at least one element.
# Don't forget to return the resul


def MultiplyByLength(arr):
    return [i * len(arr) for i in arr]
