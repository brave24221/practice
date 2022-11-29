#!/usr/bin/env python3


# Create a function that takes an integer and return True
# if it's divisible by 100, otherwise return False.

# Examples:
# divisible(1) --> False
# divisible(1000) --> True


def divisible(num):
    if num % 100 == 0:
        return True
    else:
        return False
