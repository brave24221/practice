#!/usr/bin/env/python3


# Create a function that filters out a list of state names into two categories based on the second parameter.

# Abbreviations abb
# Full names full

# Examples
# filter_state_names(["Arizona", "CA", "NY", "Nevada"], "abb")
# ➞ ["CA", "NY"]

# filter_state_names(["Arizona", "CA", "NY", "Nevada"], "full")
# ➞ ["Arizona", "Nevada"]

# filter_state_names(["MT", "NJ", "TX", "ID", "IL"], "abb")
# ➞ ["MT", "NJ", "TX", "ID", "IL"]

# filter_state_names(["MT", "NJ", "TX", "ID", "IL"], "full")
# ➞ []


def filter_state_names(lst, cat):
    if cat == 'abb':
        return [i for i in lst if len(i) == 2]

    return [i for i in lst if len(i) > 2]
