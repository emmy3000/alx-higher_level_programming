#!/usr/bin/python3


"""
Module: ``8-class_to_json``

Returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: An instance of a class

    Return:
        A dictionary with simple data structure for JSON serialization
        of the object
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
