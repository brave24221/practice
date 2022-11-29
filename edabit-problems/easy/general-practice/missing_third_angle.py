#!/usr/bin/env python3


# You are given 2 out of 3 angles in a triangle, in degrees.

# Write a function that classifies the missing angle as either
# "acute", "right", or "obtuse" based on its degrees.

# An acute angle is less than 90 degrees.
# A right angle is exactly 90 degrees.
# An obtuse angle is greater than 90 degrees (but less than 180 degrees).

# For example: missing_angle(11, 20) should return "obtuse", since the missing angle would be 149 degrees, which makes it obtuse.


def missing_angle(angle1, angle2):
    max = 180
    if max - (angle1 + angle2) < 90:
        return "acute"
    elif max - (angle1 + angle2) == 90:
        return "right"
    elif max - (angle1 + angle2) > 90:
        return "obtuse"
