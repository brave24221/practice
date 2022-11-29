#!/usr/bin/env python3


# Write a function that takes three string arguments (first, last, word)
# and returns true if it is sorted,
# only when word is found between first and last.

# Examples
# is_between("apple", "banana", "azure") ➞ True
# is_between("monk", "monument", "monkey") ➞ True
# is_between("bookend", "boolean", "boost") ➞ False

# Notes
# All letters will be in lowercase.
# All three words will be different.
# Remember the string word is in the middle


def is_between(first, last, word):
    lst = [first, word, last]

    if sorted(lst) == lst:
        return True
    else:
        return False
