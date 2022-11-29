#!/usr/bin/env python3


# Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.

# To illustrate:

# largest_swap(27) ➞ False

# largest_swap(43) ➞ True
# If 27 is our input, we should return False because swapping the digits gives us 72, and 72 > 27. On the other hand, swapping 43 gives us 34, and 43 > 34.

# Examples
# largest_swap(14) ➞ False
# largest_swap(53) ➞ True
# largest_swap(99) ➞ True

# Notes
# Numbers with two identical digits (third example) should yield True (you can't do better).


def largest_swap(num):
    string = str(num)[::-1]

    if int(string) > num:
        return False
    elif int(string) == num:
        return True

    return True
