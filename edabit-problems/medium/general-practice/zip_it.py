#!/usr/bin/env python3


# Given a list of women and a list of men either:

# return "sizes don't match" if the two lists have different sizes or
# if the sizes match, return a list of pairs, with the first woman paired with the first man, second woman paired with the second man, etc.
# Examples
# [Elise, Mary], [John, Rick] ➞ [(Elise, John), (Mary, Rick)]
# [Ana, Amy, Lisa], [Bob, Josh] ➞ "sizes don't match"
# [Ana, Amy, Lisa], [Bob, Josh, Tim] ➞ [(Ana, Bob), (Amy, Josh), (Lisa, Tim)]

# Notes
# consider using the zip() function


def zip_it(women, men):
    if len(women) == len(men):
        return list(zip(women, men))
    else:
        return 'sizes don\'t match'
