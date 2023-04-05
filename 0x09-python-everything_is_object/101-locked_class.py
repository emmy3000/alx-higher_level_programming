#!/usr/bin/python3

"""
Module: ``101-locked_class.py``
"""


class LockedClass:
    """
    class prevents a user from dynamically creating
    new instance attibutes except new instance
    attrbute is called first_name.
    """

    __slots__ = ("first_name",)

    pass
