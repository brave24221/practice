#!/usr/bin/env python3


# Create a function that returns the total number of parameters passed in.

# Examples
# number_args("a", "b", "c") ➞ 3
# number_args(10, 20, 30, 40, 50) ➞ 5
# number_args(x, y) ➞ 2
# number_args() ➞ 0

# Notes
# How can you express the input parameter so it takes a variable number of arguments?


def number_args(*args):
    lst = []
    for variable in args:
        lst.append(variable)

    return len(lst)
