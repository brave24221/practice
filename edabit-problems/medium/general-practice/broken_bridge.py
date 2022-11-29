#!/usr/bin/env python3


# Create a function which validates whether a bridge is safe to walk on (i.e. has no gaps in it to fall through).

# Examples
# is_safe_bridge('####') ➞ True
# is_safe_bridge('## ####') ➞ False
# is_safe_bridge('#') ➞ True


def is_safe_bridge(s):
    if ' ' in s:
        return False

    return True
