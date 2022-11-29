#!/usr/bin/env python3


# Given a list and an integer n, return the sum of the first n numbers in the list.

# Examples
# sum_first_n_nums([1, 3, 2], 2) ➞ 4
# sum_first_n_nums([4, 2, 5, 7], 4) ➞ 18
# sum_first_n_nums([3, 6, 2], 0) ➞ 0

# Notes
# If n is larger than the length of the list, return the sum of the whole list.


def sum_first_n_nums(lst, n):
    if n > len(lst):
        return sum(lst)
    return sum(lst[0:n])
