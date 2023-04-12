#!/usr/bin/python3

"""
    Module: ``10-Square.py``
    inherits features from Rectangle & BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size):
        """Square objects instantiation"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Compute area of the Square"""
        return self.__size ** 2
