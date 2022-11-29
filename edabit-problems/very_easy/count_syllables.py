#!/usr/bin/env python3


# Create a function that returns the number
# of syllables in a simple string. The string is made
# up of short repeated words like "Lalalalalala" (which would have 7 syllables).

# Examples:
# count_syllables("Hehehehehehe") ➞ 6
# count_syllables("bobobobobobobobo") ➞ 8
# count_syllables("NANANA") ➞ 3


def count_syllables(txt):
    return len(txt) // 2
