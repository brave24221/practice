#!/usr/bin/env python3


# Create a function that flips M's to W's (all uppercase).

# Examples
# wumbo("I LOVE MAKING CHALLENGES") ➞ "I LOVE WAKING CHALLENGES"
# wumbo("MEET ME IN WARSAW") ➞ "WEET WE IN WARSAW"
# wumbo("WUMBOLOGY") ➞ "WUWBOLOGY"


def wumbo(words):
        return words.replace("M", "W")
