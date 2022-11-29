#!/usr/bin/env python3


# Create a function that takes a number and returns a list with
# the digits of the number in reverse order.

# Examples
# reverse_list(1485979) ➞ [9, 7, 9, 5, 8, 4, 1]
# reverse_list(623478) ➞ [8, 7, 4, 3, 2, 6]


def reverse_list(num):
    lst = []

    string = str(num)
    for num in string:
        lst.append(int(num))
    lst.reverse()

    return lst
