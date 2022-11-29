#!/usr/bin/env python3


# Create a function that finds the maximum range of a triangle's
# third edge, where the side lengths are all integers.

# Examples:
# next_edge(8, 10) --> 17
# next_edge(5, 7) --> 11

def next_edge(side1, side2):
    return (side1 + side2) - 1
