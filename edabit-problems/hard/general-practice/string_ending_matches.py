#!/usr/bin/env python3


# Create a function that takes two strings and returns True
# if the first string ends with the second string; otherwise return False.

# Examples
# check_ending("abc", "bc") ➞ True
# check_ending("abc", "d") ➞ False
# check_ending("samurai", "zi") ➞ False
# check_ending("feminine", "nine") ➞ True
# check_ending("convention", "tio") ➞ False


def check_ending(str1, str2):
    return str1.endswith(str2)
