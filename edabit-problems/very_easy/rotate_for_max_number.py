# Create a function which takes a number and returns the
# maximum value # by rearranging its digits.

# Examples
# rotate_max_number(123) ➞ 321
# rotate_max_number("001") ➞ 100
# rotate_max_number(999) ➞ 999


def rotate_max_number(num):
    return int(''.join(sorted(str(num))[::-1]))
