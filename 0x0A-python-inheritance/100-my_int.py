#!/usr/bin/python3

"""

Module: ``100-my_int.py``
"""


class MyInt(int):
    """
    A rebel version of an integer. Perfect for opposite day!

    Method:
        __eq__(other): Return True if self is not equal to other;
        False otherwise.
        __ne__(other): Return True if self is equal to other;
        False otherwise.
    """

    def __new__(cls, *args, **kwargs):
        """Create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Inverts the == to != operator"""
        return int(self) != other

    def __ne__(self, other):
        """Inverts the != to == operator"""
        return int(self) == other
