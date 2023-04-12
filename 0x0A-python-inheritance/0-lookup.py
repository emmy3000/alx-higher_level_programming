#!/usr/bin/python3

"""
Module: `0-lookup.py`
"""


def lookup(obj):
    """
    Function returns a list of available attributes.

    obj(Object): object having its attributes and
    methods listed.

    """

    return(dir(obj))
