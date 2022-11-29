#!/usr/bin/env python3


# In the Code tab is a function which is meant to return how many
# uppercase letters there are in a list of various words.
# Fix the list comprehension so that the code functions normally!

# Examples
# count_uppercase(['SOLO', 'hello', 'Tea', 'wHat']) ➞ 6
# count_uppercase(['little', 'lower', 'down']) ➞ 0
# count_uppercase(['EDAbit', 'Educate', 'Coding']) ➞ 5


# Buggy code
# def count_uppercase(lst):
#     return sum(letter.isupper() for letter in word for word in lst)

# My revision:
def count_uppercase(lst):
    return sum(letter.isupper() for word in lst for letter in word)
