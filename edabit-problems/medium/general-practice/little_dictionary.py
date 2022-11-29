#!/usr/bin/env python3


# Create a function that takes an initial word and filters out
# a list to contain words that start with the same letters as the initial word.

# Examples
# dictionary("bu", ["button", "breakfast", "border"]) ➞ ["button"]
# dictionary("tri", ["triplet", "tries", "trip", "piano", "tree"]) ➞ ["triplet", "tries", trip"]
# dictionary("beau", ["pastry", "delicious", "name", "boring"]) ➞ []

# Notes
# If none of the words match, return an empty list.
# Keep the filtered list in the same
# relative order as the original list of words.


def dictionary(initial, words):
    return [i for i in words if i.startswith(initial)]
