#!/usr/bin/python3

"""
Module: 2-append_write
"""


def append_write(filename="", text=""):
    """
    function appends a string to a file encoded in UTF-8 and
    returns the number of characters

    Args:
        filename(str): file to be written to
        text(str): text to be written into filename

    Return: number of characters to be added
    """

    with open(filename, 'a', encoding="utf-8") as mexFile:
        return mexFile.write(text)
