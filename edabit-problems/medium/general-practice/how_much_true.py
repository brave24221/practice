#!/usr/bin/env python3


# Create a function which returns the number of True values there are in a list.

# Examples
# count_true([True, False, False, True, False]) ➞ 2
# count_true([False, False, False, False]) ➞ 0
# count_true([]) ➞ 0


def count_true(lst):
    if True in lst:
        return lst.count(True)
    elif len(lst) == 0:
        return 0
    else:
        return 0
