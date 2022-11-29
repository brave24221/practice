#!/usr/bin/env python3


def googlify(n):
    letter = 'o' * n
    if n > 1:
        return 'G' + letter + 'gle'
    elif n <= 1:
        return 'invalid'


print(googlify(4))
