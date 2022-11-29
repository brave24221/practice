#!/usr/bin/env python3


# Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.

# Examples
# get_case("whisper...") ➞ "lower"
# get_case("SHOUT!") ➞ "upper"
# get_case("Indoor Voice") ➞ "mixed"


def get_case(txt):
    if txt.isupper():
        return "upper"
    elif txt.islower():
        return "lower"
    elif txt != txt.islower() and txt != txt.isupper():
        return "mixed"
