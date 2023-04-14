#!/usr/bin/python3

"""
Module: 1-write_file
"""


def write_file(filename="", text=""):
    """
<<<<<<< HEAD
    function writes text to a file encoded in UTF-8 and
    returns the number of characters
=======
    function writes text to a file encoded in UTF-8
>>>>>>> 9acde752f18dd2433113461b76df55a723408bb3

    Args:
        filename(str): file to be written to
        text(str): text to be written into filename

    Return: number of characters written to filename
    """

    with open(filename, 'w', encoding="utf-8") as mexFile:
        return mexFile.write(text)
