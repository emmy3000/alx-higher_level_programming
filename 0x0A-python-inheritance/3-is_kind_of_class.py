#!/usr/bin/python3

"""
Module: ``3-is_kind_of_class.py``
"""


def is_kind_of_class(obj, a_class):
    """
    function returns True/False if object is an instance of,
    or object is an instance of class that inherited from

    Args:
        obj: the object to be checked
        a_class: the class to check against

    Return:
        True if obj is an instance of a_class or an inherited
        class, Otherwise False
    """
    return(isinstance(obj, a_class))
