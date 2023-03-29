#!/usr/binpython3

"""class definition of a Square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Attributes for new square instance

            size: integer size of new square
                instance.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater or\
            equal to 0")
        else:
            self.__size = size
