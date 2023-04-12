#!/usr/bin/python3

"""
    Module: ``4-inherits_from.py``
"""


def inherits_from(obj, a_class):
    """
    function returns True/false if object is an instance
    of a class that inherited(directly/indirectly) from a
    specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj an instance of a_class;
        Otherwise False.
    """
    return(isinstance(obj, a_class) and type(obj) is not a_class)
