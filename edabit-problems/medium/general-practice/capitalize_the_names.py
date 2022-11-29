#!/usr/bin/env python3


# Create a function that takes a list of names and returns a list with only the first letter capitalized.

# Examples
# cap_me(["mavis", "senaida", "letty"]) ➞ ["Mavis", "Senaida", "Letty"]
# cap_me(["samuel", "MABELLE", "letitia", "meridith"]) ➞ ["Samuel", "Mabelle", "Letitia", "Meridith"]
# cap_me(["Slyvia", "Kristal", "Sharilyn", "Calista"]) ➞ ["Slyvia", "Kristal", "Sharilyn", "Calista"]

# Notes
# Don't change the order of the original list.
# Notice in the second example above, "MABELLE" is returned as "Mabelle".


def cap_me(lst):
    return [i.title() for i in lst]
