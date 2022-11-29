#!/usr/bin/env python3


# Create a function that takes a number
# as an argument and returns "even" for even numbers and "odd" for odd numbers.

# Examples:
# isEvenOrOdd(3) ➞ "odd"
# isEvenOrOdd(146) ➞ "even"
# isEvenOrOdd(19) ➞ "odd"


def isEvenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
