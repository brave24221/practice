#!/usr/bin/env python3


# Create a function that returns True if an integer is evenly
# divisble by 5, and returns False if otherwise.

# Examples:
# divisible_by_five(5) --> True
# divisible_by_five(-55) --> True


def divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False
