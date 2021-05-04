#!/usr/bin/env python
"""
find next palindrome
"""

from math import ceil


def next_palindrome(num: int):
    """find next palindrome"""
    start = str(num)
    full_len = len(start)
    half_len = ceil(full_len / 2)
    head = start[:half_len]
    tail = start[-half_len:]

    if head[::-1] <= tail or tail == '':
        head = str(int(head) + 1)
    if len(head) > half_len:
        full_len += 1

    left_len = ceil(full_len/2)
    right_len = int(full_len/2)
    left = head[:left_len]
    right = head[:right_len][::-1]

    return int(f"{left}{right}")
