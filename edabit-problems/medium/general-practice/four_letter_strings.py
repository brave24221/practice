#!/usr/bin/env python3


# Create a function that takes a list of strings and returns the words that are exactly four letters.

# Examples
# is_four_letters(["Tomato", "Potato", "Pair"]) ➞ ["Pair"]
# is_four_letters(["Kangaroo", "Bear", "Fox"]) ➞ ["Bear"]
# is_four_letters(["Ryan", "Kieran", "Jason", "Matt"]) ➞ ["Ryan", "Matt"]

# Notes
# You can expect valid strings for all test cases.


def is_four_letters(lst):
    return [i for i in lst if len(i) == 4]
