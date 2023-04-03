#!/usr/bin/python3

"""
Module: ``4-print_square.py``

"""


def print_square(size):
    """
    Function prints a square with the character #

    Args:
        size(int): length of a square.

    Returns:
        a pattern with the character #.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        row = "#" * size
        for i in range(size):
            print(row)
