#!/usr/bin/env python3


# Write a function that takes two integers "hours" and "minutes"
# and converts them into seconds.

# Examples:
# convert(1, 3) --> 3780
# convert(2, 0) --> 7200

def convert(hours, minutes):
    return (hours * 3600) + (minutes * 60)
