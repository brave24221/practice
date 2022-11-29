#!/usr/bin/env python3


# Zip codes consist of 5 consecutive digits. Given a string, write
# a function to determine whether
# the input is a valid zip code. A valid zip code is as follows:

# Must only contain numbers (no non-digits allowed).
# Must not contain any spaces.
# Must not be greater than 5 digits in length.

# Examples
# is_valid("59001") ➞ True
# is_valid("853a7") ➞ False
# is_valid("732 32") ➞ False


def is_valid(zip_code):
    if len(zip_code) == 5 and zip_code.isdigit() and ' ' not in zip_code:
        return True
    else:
        return False
