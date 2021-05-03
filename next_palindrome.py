#!/usr/bin/env python
"""
find next palindrome
"""

from math import ceil


def next_palindrome(num: int):
    """find next palindrome"""
    start = str(num)
    half_len = ceil(len(start) / 2)
    half_string = start[:half_len]
    new_half_string = str(int(half_string) + 1)
    need_new_digit = len(new_half_string) > len(half_string)

    left_len = half_len - 1 if len(start) % 2 else half_len
    left = new_half_string[:left_len]

    right_len = half_len + 1 if need_new_digit else half_len
    right = new_half_string[:right_len][::-1]

    final = f"{left}{right}"
    return int(final)
