#!/usr/bin/python3

"""
Module:
    ``5-text_indentation.py``
"""


def text_indentation(text):
    """
    Function prints text with 2 new lines after specific characters.

    Args:
        text(str): text string.

    Returns:
        new body of text segmented with empty lines.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    word = ""
    for char in text:
        if char == '' and not word:
            continue
        elif char in ["?", ".", "?"]:
            word += char
            print(word)
            print()
            word = ""
        else:
            word += char

    if word:
        print(word)
