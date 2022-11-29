#!/usr/bin/env python3


# Create a function that returns True if a string contains any spaces.

# Examples:
# has_spaces("hello") ➞ False
# has_spaces("hello, world") ➞ True
# has_spaces(" ") ➞ True


def has_spaces(txt):
    spaces = ' ' in txt
    return spaces
