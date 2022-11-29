#!/usr/bin/env python3


# Given a total due and a list representing the amount of change
# in your pocket, determine whether or not you are able
# to pay for the item. Change will always be represented in the following
# order: quarters, dimes, nickels, pennies.

# To illustrate: change_enough([25, 20, 5, 0], 4.25) should
# yield True, since having 25 quarters, 20 dimes, 5 nickels
# and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50.

# Examples
# change_enough([2, 100, 0, 0], 14.11) ➞ False
# change_enough([0, 0, 20, 5], 0.75) ➞ True
# change_enough([30, 40, 20, 5], 12.55) ➞ True
# change_enough([10, 0, 0, 50], 3.85) ➞ False
# change_enough([1, 0, 5, 219], 19.99) ➞ False

# Notes
# quarter: 25 cents / $0.25
# dime: 10 cents / $0.10
# nickel: 5 cents / $0.05
# penny: 1 cent / $0.01


def change_enough(change, amount_due):
    quarter = change[0] * 0.25
    dime = change[1] * 0.10
    nickel = change[2] * 0.05
    penny = change[3] * 0.01

    return (quarter
            + dime
            + nickel
            + penny) >= amount_due
