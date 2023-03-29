#!/usr/binpython3

"""class definition of a Square"""


class Square:
    """class Square's class level"""

    def __init__(self, size=0):
        """Initialize a protected attribute.
        Args:
            size(int): size of new Square instance.

        Errors:
            TypeError message if value isn't an integer.
            ValueError message if value is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
