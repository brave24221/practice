#!/usr/bin/env python3


# Create a function that returns the numbers of frames shown in a given
# number of minutes for a certain FPS.

# Examples:
# frames(1, 1) --> 60
# frames (10, 1) --> 600
# frames (10, 25 --> 15000


def frames(minutes, fps):
    return (minutes * 60) * fps
