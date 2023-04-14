#!/usr/bin/python3


"""
Module: ``6-load_from_json_file``
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename (str): The name of the JSON file to load

    Return:
        The deserialized object from the JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as mexFile:
        return json.load(mexFile)
