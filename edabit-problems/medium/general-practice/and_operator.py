#!/usr/bin/env python3


# Python has a logical operator and, which can also be written as &. The
# and operator takes two boolean values
# and returns true if both values are true.

# Consider a and b:

# - `a` is checked if it is `True` or `False`.
# - If `a` is `False`,  `False` is returned
# - `b` is checked if it is `False` or `False`.
# - If `b` is `False`, `False` is returned
# - Otherwise, `True` is returned (as both `a` and `b` are therefore `True` )

# The and operator will only return True for True and True.

# Make a function using the and operator.

# Examples
# And(true, false) ➞ False
# And(true, true) ➞ True
# And(false, true) ➞ False
# And(false, false) ➞ False


def And(a, b):
    if a == True and b == True:
        return True

    return False
