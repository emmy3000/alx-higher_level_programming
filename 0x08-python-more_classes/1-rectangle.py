#!/usr/bin/python3

"""
Module: ``1-rectangle.py``

"""


class Rectangle:
    """class Rectangle definition"""
    def __init__(self, width=0, height=0):
        """
        Initialize a width and height attributes with
        optional integer literals.

        Args:
            width(int): width of the rectangle.
            height(int): height of the rectangle.

        Returns:
            new instance of a class Rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """object method for geting width private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set new width value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """object method for getting width private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set new height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height  must be >= 0")
        self.__height = value
