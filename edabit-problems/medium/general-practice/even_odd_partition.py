#!/usr/bin/env python3


# Write a function that partitions the list into two sublists: one with
# all even integers, and the other with all odd integers
# . Return your result in the following format:

# [[evens], [odds]]
# Examples
# even_odd_partition([5, 8, 9, 2, 0]) ➞ [[8, 2, 0], [5, 9]]
# even_odd_partition([1, 0, 1, 0, 1, 0]) ➞ [[0, 0, 0], [1, 1, 1]]
# even_odd_partition([1, 3, 5, 7, 9]) ➞ [[], [1, 3, 5, 7, 9]]
# even_odd_partition([]) ➞ [[], []]

# Notes
# Return two empty sublists if the input is an empty list.
# Keep the same relative ordering as the original list.


def func(lst):
    evens = list(filter(lambda x: (x % 2) == 0, lst))
    odds = list(filter(lambda x: (x % 2) == 1, lst))

    return [evens, odds]
