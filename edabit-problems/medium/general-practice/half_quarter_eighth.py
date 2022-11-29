#!/usr/bin/env python3


# Create a function that takes a number and return an array of tree numbers
# : the half of the number, the quarter of the number and the eighth of the number.

# Examples
# halfQuarterEighth(6) ➞ [ 3, 1.5, 0.75 ]
# halfQuarterEighth(22) ➞ [ 11, 5.5, 2.75 ]
# halfQuarterEighth(25) ➞ [ 12.5, 6.25, 3.125 ]

# Notes
# the order of the array is: half, quarter, eighth


def halfQuarterEighth(n):
    return [n / 2, n / 4, n / 8]
