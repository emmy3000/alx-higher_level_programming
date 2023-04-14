#!/usr/bin/python3

"""
Module: 4-from_json_string-input_output
"""

import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string

    Args:
        my_str(str): A JSON string.

    Return:
        A Python data structure represented by the JSON string
    """
    return json.loads(my_str)
