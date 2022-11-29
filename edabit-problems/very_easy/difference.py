#!/usr/bin/env python3


# Create a function that takes a list and
# returns the difference between the biggest and smallest numbers.

# Examples:
# difference_max_min([10, 4, 1, -10, -60, 32, 21]) --> 81
# Smallest number is -50, biggest is 32.

# difference_max_min([44, 32, 86, 19]) --> 67
# Smallest number is 19, biggest is 86.


def difference_max_min(lst):
    return max(lst) - min(lst)
