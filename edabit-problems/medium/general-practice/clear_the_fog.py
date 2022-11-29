#!/usr/bin/env python3


# Create a function which returns the word in the string,
# but with all the fog letters removed. However, if the string
# is clear from fog, return "It's a clear day!".

# Examples
# clear_fog("sky") ➞ "It's a clear day!"
# clear_fog("fogfogfffoooofftreesggfoogfog") ➞ "trees"
# clear_fog("fogFogFogffffooobirdsandthebeesGGGfogFog") ➞ "birdsandthebees"

# Notes
# There won't be any fog inside of any of the actual words.
# Tests won't include the letters f, o or g.
# Hidden words are always in lowercase.


def clear_fog(txt):
    filtered_chars = ''.join((filter(lambda x: x not in ('f', 'o', 'g'), txt)))
