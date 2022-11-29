#!/usr/bin/env python3


# Create a function that returns the product of all odd integers in a list.

# Examples
# odd_product([3, 4, 1, 1, 5]) ➞ 15
# odd_product([5, 5, 8, 2, 4, 32]) ➞ 25
# odd_product([1, 2, 1, 2, 1, 2, 1, 2]) ➞ 1



def odd_product(lst):
    result = 1
    divisble = list(filter(lambda x: (x % 2) == 1, lst))
    for i in divisble:
        result *= i

    return result
