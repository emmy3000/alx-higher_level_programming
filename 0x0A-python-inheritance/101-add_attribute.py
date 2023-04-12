#!/usr/bin/python3

"""
``101-add_attribute`` module provides a function to add attributes
to objects.
"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.

    Raises:
        TypeError: If the attriute cannot be added to the
        object.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        obj.__dict__[att] = value
