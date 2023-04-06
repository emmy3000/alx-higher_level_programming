#!/usr/bin/python3

"""
Module:
    ``5-text_indentation.py``
"""


def text_indentation(text):
    """
    Function print strings that splits after specific
    character "?", "." and ":" followed by 2 new lines

    Args:
        text(str): text string.

    Returns:
        new body of text segmented with empty lines.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = ""
    for char in text:
        if char in [".", ":", "?"]:
            sentence += char
            print(sentence.strip())
            print()
            sentence = ""
        else:
            sentence += char

    if sentence:
        print(sentence.strip())
