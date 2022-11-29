#!/usr/bin/env python3


# Create a function that takes a number as
# its only argument and returns True if it's less
# than or equal to zero, otherwise return False.

# Examples:
# less_than_or_equal_to_zero(5) ➞ False
# less_than_or_equal_to_zero(0) ➞ True
# less_than_or_equal_to_zero(-2) ➞ True


def less_than_or_equal_to_zero(num):
    if num <= 0:
        return True
    else:
        return False
