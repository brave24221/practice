#!/usr/bin/env python3


# Given a list of prices prices and a "supposed" total t, return True if there is a hidden fee added to the total (i.e. the total is greater than the sum of prices), otherwise return False.

# Examples
# has_hidden_fee(["$2", "$4", "$1", "$8"], "$15") ➞ False
# has_hidden_fee(["$1", "$2", "$3"], "$6") ➞ False
# has_hidden_fee(["$1"], "$4") ➞ True

# Notes
# Remember that each price is given as a string.


def has_hidden_fee(prices, t):
    hold = [int(i.replace('$', '')) for i in prices]
    total = int(t.replace("$", ""))

    return total > sum(hold)
