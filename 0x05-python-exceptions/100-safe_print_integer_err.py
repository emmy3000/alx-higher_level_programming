#!/usr/bin/python3

import sys

"""Prints an integer with "{:d}".format().
    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.
    Returns:

        If a TypeError or ValueError occurs - False.
        Otherwise retrun True.
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
