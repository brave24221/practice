#!/usr/bin/env python3


# Google's logo can be stretched depending
# on how many pages it lets you skip forward to.


# Let's say we wanted to change the amount of pages that Google could
# skip to. Create a function where given a number of pages n, return
# the word 'Google' but with the correct number of "o"s.

# Examples
# googlify(10) ➞ "Goooooooooogle"
# googlify(23) ➞ "Gooooooooooooooooooooooooogle"
# googlify(2) ➞ "Google"
# googlify(-2) ➞ "invalid"


def googlify(n):
    if n <= 1:
        return 'invalid'
    elif n == 2:
        return 'Google'
    else:
        word = 'G'
        letter = 'o'
        end = 'gle'
        answer = "G{}{}".format(letter * n, end)
        return answer
