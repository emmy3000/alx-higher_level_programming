#!/usr/bin/python3

"""class definition of a Square"""


class Square:
    """class Square's class level"""

    def __init__(self, size=None):
        """Initialize a size attribute.

        Attributes:
            size(int): size of new Square\
            instance.
        """
        self.__size = size
