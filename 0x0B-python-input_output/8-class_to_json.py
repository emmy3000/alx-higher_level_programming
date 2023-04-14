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
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
