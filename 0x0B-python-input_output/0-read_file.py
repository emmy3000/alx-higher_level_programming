#!/usr/bin/python3

"""
Module: 0-read_file
"""


def read_file(filename=""):
    """
    function reads a text file

    Args:
        filename(str): file to be printed

    Return: prints file content to stdout.
    """

    with open(filename, 'r', encoding="utf-8") as mexFile:
        print(mexFile.read())
