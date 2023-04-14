#!/usr/bin/python3


"""
Module: ``8-class_to_json``

Returns the dictionary description with simple data structure
for JSON serialization of an object
"""

import json


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
    else:
        raise TypeError("Object of type %s is not JSON serialized"
                % type(obj).__name__)
