#!/usr/bin/env python3


# Write a function that returns True if two rooks can attack each other, and False otherwise.

# Examples
# can_capture(["A8", "E8"]) ➞ True
# can_capture(["A1", "B2"]) ➞ False
# can_capture(["H4", "H3"]) ➞ True
# can_capture(["F5", "C8"]) ➞ False

# Notes
# Assume no blocking pieces.
# Two rooks can attack each other if they share the same row (letter) or column (number).


def can_capture(rooks):
    if rooks[0][0].startswith(rooks[0][0]) == rooks[1][0].startswith(rooks[0][0]):
        return True
    elif rooks[0][1].endswith(rooks[0][1]) == rooks[1][1].endswith(rooks[0][1]):
        return True
    else:
        return False
