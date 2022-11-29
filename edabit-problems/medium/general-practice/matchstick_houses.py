#!/usr/bin/env python3


This challenge will help you interpret mathematical relationships both
algebraically and geometrically.

# --Image--
# Create a function that takes a number (step) as an argument and returns
# the amount of matchsticks in that step.
# See step 1, 2 and 3 in the image above.


# Examples
# match_houses(1) ➞ 6
# match_houses(4) ➞ 21
# match_houses(87) ➞ 436

# Notes
# Step 0 returns 0 matchsticks.
# The input (step) will always be a non-negative integer.

def match_houses(step):
    if step == 0:
        return 0

    return (step * 5) + 1
