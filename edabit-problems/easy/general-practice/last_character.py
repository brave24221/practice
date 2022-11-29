#!/usr/bin/env python3


# Create a function that takes a string (a random name).
# If the last character of the name is an "n", return True,
# otherwise return False.

# Examples:
# is_last_character_n("Aiden") ➞ True
# is_last_character_n("Piet") ➞ False
# is_last_character_n("Bert") ➞ False


def is_last_character_n(word):
    if word.endswith('n'):
        return True
    else:
        return False
