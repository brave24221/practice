#!/usr/bin/env python3


# Create two functions: is_prefix(word, prefix-) and is_suffix(word, -suffix).

# is_prefix should return True if it begins with the prefix argument.
# is_suffix should return True if it ends with the suffix argument.
# Otherwise return False.

# Examples
# is_prefix("automation", "auto-") ➞ True
# is_suffix("arachnophobia", "-phobia") ➞ True
# is_prefix("retrospect", "sub-") ➞ False
# is_suffix("vocation", "-logy") ➞ False

# Notes
# The prefix and suffix arguments have dashes - in them.


def is_prefix(word, prefix):
    return word.startswith(prefix.replace('-', ''))


def is_suffix(word, suffix):
    return word.endswith(suffix.replace('-', ''))
