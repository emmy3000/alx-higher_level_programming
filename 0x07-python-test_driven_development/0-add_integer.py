#!/usr/bin/python3
"""
Module:
    0-add_integer

Function:
    exports a function for adding 2 integers.
"""


def add_integer(a, b=98):
    """
    Function adds 2 int.

    Args:
        a(int): integer parameter 1.
        b(int): integer parameter 2.

    Return:
        sum of integers a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
