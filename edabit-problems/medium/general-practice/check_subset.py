#!/usr/bin/env python3


# List A is contained inside list B if each element in A also exists in B.

# The number of times a number is present doesn't matter.
# In other words, if we transformed both lists
# into sets, A would be a subset of B.

# A = [3, 3, 9, 9, 9, 5]
# B = [1, 3, 9, 5, 8, 44, 44]

# A_Set = [3, 9, 5]
# B_Set = [1, 3, 9, 5, 8, 44]

# # A_Set is a subset of B_Set
# Create a function that determines if the first list is a subset of the second.

# Examples
# subset([1, 3], [1, 3, 3, 5]) ➞ True
# subset([4, 8, 7], [7, 4, 4, 4, 9, 8]) ➞ True
# subset([1, 3], [1, 33]) ➞ False
# subset([1, 3, 10], [10, 8, 8, 8]) ➞ False

# Notes
# Each input list will have at least one element.


def subset(lst1, lst2):
    for item in lst1:
        if item not in lst2:
            return False

    return True
