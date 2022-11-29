#!/usr/bin/env python3


# In this challenge, you have to implement a function that
# returns the given distance kilometers converted into miles.
# You have to round the result up to the fifth decimal digit.

# Examples
# km_to_miles(2) ➞ 1.24274
# km_to_miles(6) ➞ 3.72823
# km_to_miles(8) ➞ 4.97097


def km_to_miles(kilometers):
    answer = kilometers * 0.621371
    return round(answer, 5)
