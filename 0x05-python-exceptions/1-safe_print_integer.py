#!/usr/bin/python3

"""Print an integer with "{:d}".format().

value: integer to print

Returns: False if a TypeError or ValueError occurs
        Otherwise returns True.
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
