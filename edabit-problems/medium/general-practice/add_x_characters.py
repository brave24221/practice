#!/usr/bin/env python3


# Create a function that takes a string, a character and a length and returns (length) characters before and after the string

# Examples
# my_func("John", "*", 4) ➞ "****John****"
# my_func("edabit", "^", 5) ➞  "^^^^^edabit^^^^^"


def my_func(string, char, length):
    char_length = char * length
    answer = "{}{}{}".format(char_length, string, char_length)
    # answer = f"{char_length}{string}{char_length}"
    return answer
