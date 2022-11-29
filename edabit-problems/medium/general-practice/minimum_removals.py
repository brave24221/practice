#!/usr/bin/env python3


# Create a function that returns the minimum number of elements removed to make the sum of all elements in a list even.

# Examples
# minimum_removals([1, 2, 3, 4, 5]) ➞ 1
# minimum_removals([5, 7, 9, 11]) ➞ 0
# minimum_removals([5, 7, 9, 12]) ➞ 1

# Notes
# If the sum is already even, return 0 (see example #2).
# The output will be either 0 or 1.


def minimum_removals(lst):
    if not sum(lst) % 2 == 0:
        return 1
    else:
        return 0
