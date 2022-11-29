#!/usr/bin/env python3


# Create a function that finds the index of a given item.

# Examples
# search([1, 5, 3], 5) ➞ 1
# search([9, 8, 3], 3) ➞ 2
# search([1, 2, 3], 4) ➞ -1


def search(lst, item):
    try:
        find = lst.index(item)
        if item in lst:
            return find
    except ValueError:
        return -1


test = [1, 2, 3, 4]
print(search(test, 5))
