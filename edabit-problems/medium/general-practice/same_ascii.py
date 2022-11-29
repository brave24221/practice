#!/usr/bin/env python3


# Return True if the sum of ASCII values of the first string is
# same as the sum of ASCII values of the
# second string, otherwise return False.

# Examples
# same_ascii("a", "a") ➞ True
# same_ascii("AA", "B@") ➞ True
# same_ascii("EdAbIt", "EDABIT") ➞ False


def same_ascii(a, b):
    list_a, list_b = [ord(i) for i in a], [ord(j) for j in b]

    if sum(list_a) == sum(list_b):
        return True
    return False
