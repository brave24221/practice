#!/usr/bin/env python3


# Given a fraction as a string, return whether or not it is greater than 1 when evaluated.

# Examples
# greater_than_one("1/2") ➞ False
# greater_than_one("7/4") ➞ True
# greater_than_one("10/10") ➞ False


def greater_than_one(frac):
    if eval(frac) > 1:
        return True
    else:
        return False
