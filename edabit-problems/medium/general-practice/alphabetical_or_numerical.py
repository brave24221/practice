#!/usr/bin/env python3


# Create a function that takes a string and returns a tuple
# that consists of two lists. a list that has all the alphabet letters in
# the string, and a list that has all the numeric
# characters in the string

# Examples
# my_func("ed4b1t 15 the best") ➞ (['4', '1', '1', '5'], ['e', 'd', 'b', 't', 't', 'h', 'e', 'b', 'e', 's', 't'])

# Notes
# the first list is the numeric list and the second one is the alphabet list


def my_func(string):
    alpha_lst = []
    num_lst = []

    for char in string:
        if char.isalpha():
            alpha_lst.append(char)
        if char.isnumeric():
            num_lst.append(char)

    return (num_lst, alpha_lst)
