#!/usr/bin/python3
"""
Module:
   ``0-add_integer.py``
"""


def add_integer(a, b=98):
    """
    Function adds 2 integers.

    Args:
        a(int): integer parameter 1.
        b(int): integer parameter 2.

    Return:
        sum of integers a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be integer or float")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
