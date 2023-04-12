#!/usr/bin/python3

"""
    Module: ``11-Square.py``
    inherits features from class BaseGeometry & Rectangle
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value argument"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from Biochemistry"""

    def __init__(self, width, height):
        """Initializes Rectangle instances"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Calculates area of Rectangle instance"""
        return self.__width * self.__height

    def __str__(self):
        """Returns an informal string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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

    def __str__(self):
        """Returns an informal string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
