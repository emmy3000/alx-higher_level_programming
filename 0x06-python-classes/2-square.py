#!/usr/binpython3

"""Defining a class Square."""

class Square:
    """class level"""

    def __init__(self, size=0):
        """Attributes for allocating sizes to
        an instance.

        size(int): integer size of a new square
                instance.

        Errors: TypeError message if value isn't
                an integer.
                ValueError message if value is less
                than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater or\
            equal to 0")
        else:
            self.__size = size
