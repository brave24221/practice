#!/usr/bin/env python3


# Given a sorted list of numbers, remove any numbers
# that are divisible by 13. Return the amended list.

# Examples
# unlucky_13([53, 182, 435, 591, 637]) ➞ [53, 435, 591]
# # 182 and 637 are divisible by 13.

# unlucky_13([24, 316, 393, 458, 1279]) ➞ [24, 316, 393, 458, 1279]
# # No numbers in the list are divisible by 13.

# unlucky_13([104, 351, 455, 806, 871]) ➞ []
# # All numbers in the list are divisible by 13.


def unlucky_13(nums):
    return [i for i in nums if i % 13]
