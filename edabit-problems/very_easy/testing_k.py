#!/usr/bin/env python3

# Write a function that returns True
# if k^k == n for input (n, k) and return False otherwise.

# Examples:
# k_to_k(4, 2) --> True
# k_to_k(387420489, 9) --> True
# 9 ^ 9 == 387420489


def k_to_k(n, k):
    if k ** k == n:
        return True
    else:
        return False
