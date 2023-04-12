#!/usr/bin/python3

"""
    Module: ``2-is_same_class.py``
"""


def is_same_class(obj, a_class):
    """function returns true if object
    is exactly an instance.

    Args:
        obj: object to be checked.
        a_class: class to compare obj with.

    Returns:
        True if obg is exactly an instance
        of a_class; Otherwise False
    """
    return(type(obj) is a_class)
