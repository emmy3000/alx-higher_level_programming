#!/usr/bin/python3

"""
Module: ``9-rectangle.py``

"""


class Rectangle:
    """class Rectangle definition"""

    number_of_instances = 0
    print_symbol = "#"

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

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
        """object method for getting height private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set new height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height  must be >= 0")
        self.__height = value

    def area(self):
        """method for obtaining the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method for obtaining the perimeter of the retangle"""
        if self.__width == 0 and self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns an informal representation of a string of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """returns a formal representation of a string of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when an instance of the Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        return cls(size, size)
