#!/usr/bin/env python3


# Create a function that returns the number of decimal places a
# number has. Any zeros after the decimal point
# count towards the number of decimal places.
#
# Examples
# get_decimal_places("43.20") ➞ 2
# get_decimal_places("400") ➞ 0
# get_decimal_places("3.1") ➞ 1

# Notes
# Return 0 if the number doesn't have any decimal places (see example #2).


def get_decimal_places(n):
    hold = n.split('.')

    if len(hold) == 1:
        return 0
    else:
        return len(hold[1])
