#!/usr/bin/python3

"""
``3-say_name-name`` module.
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints a string to output.

    Args:
        first_name(str): string parameter 1
        last_name(str): string parameter 2

    Returns:
        The string "My name is <first_name> <last_name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
