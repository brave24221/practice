#!/usr/bin/env python3

# Given an integer, return "odd" if the sum of all odd digits
# is greater than the sum of all even digits. Return "even" if
# the sum of even digits is greater than the sum of odd digits,
# and "equal" if both sums are the same.

# Examples
# odds_vs_evens(97428) ➞ "odd"
# odd = 16 (9+7)
# even = 14 (4+2+8)

# odds_vs_evens(81961) ➞ "even"
# odd = 11 (1+9+1)
# even = 14 (8+6)

# odds_vs_evens(54870) ➞ "equal"
# odd = 12 (5+7)
# even = 12 (4+8+0)


def odds_vs_evens(num):
    lst = [int(x) for x in str(num)]
    odds = sum(list(filter(lambda x: (x % 2) == 1, lst)))
    evens = sum(list(filter(lambda x: (x % 2) == 0, lst)))

    if odds > evens:
        return 'odd'
    if evens > odds:
        return 'even'

    return 'equal'
