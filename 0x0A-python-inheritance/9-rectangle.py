#!/usr/bin/python3

"""
    Module: ``9-rectangle.py``
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from Biochemistry"""

    def __init__(self, width, height):
        """Initializes Rectangle instances"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Returns an informal string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculates area of Rectangle instance"""
        return self.__width * self.__height
