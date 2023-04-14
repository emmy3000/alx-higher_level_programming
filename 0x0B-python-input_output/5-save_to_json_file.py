#!/usr/bin/python3

"""
Module: 5-save_to_json_file
Defines a function to save an object to a JSON file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a textfile, using a JSON representation

    Args:
        my_obj (object): Object to be serialized to JSON
        filename (str): Name of the file to save the serialized
        JSON string

    Return:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as mexFile:
        json.dump(my_obj, mexFile)
