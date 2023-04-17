#!/usr/bin/python3

"""
Module defining a Rectangle class that inherits from Base
and acts as a superclass to the Square class
"""

from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle
    and inherits from superclass Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle or Square class

        Args:
            width (int): The width of the rectangle or square.

            height (int): The height of the rectangle or the side
            of the square.

            x (int, optional): The horizontal offset of the rectangle
            or square.Defaults to 0.

            y (int, optional): The vertical offset of the rectangle
            or square.Defaults to 0.

            id (int, optional): The ID of the rectangle or square.
            Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the Rectangle.
        Args:
            width (int): The width of the Rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than or equal to 0.
        """
        self.IntegerValidation("width", width, True)
        self.__width = width

    @property
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the Rectangle.
        Args:
            height (int): The height of the Rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.
        """
        self.IntegerValidation("height", height, True)
        self.__height = height

    @property
    def x(self):
        """x-coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x-coordinate of the Rectangle.
        Args:
            x (int): The x-coordinate of the Rectangle.
        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        self.IntegerValidation("x", x, False)
        self.__x = x

    @property
    def y(self):
        """y-coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y-coordinate of the Rectangle.
        Args:
            y (int): The y-coordinate of the Rectangle.
        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        self.IntegerValidation("y", y, False)
        self.__y = y

    def IntegerValidation(self, name, value, wh=True):
        """Validates whether the given input is an integer
        and whether it is greater than zero (if wh=True) or
        greater than or equal to zero (if wh=False).

        Args:
            name (str): The name of the input value being validated.
            value (int): The input value being validated.
            wh (bool): Whether the input value should be greater
            than zero (if True) or greater than or equal to zero (if False).

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is not greater than
            zero (if wh=True) or greater than or equal to zero (if wh=False).
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if wh and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not wh and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.width * self.height

    def display(self):
        """Prints the Rectangle to the standard output.
        """
        rect = '\n' * self.y + (' '
                                * self.x + '#' * self.width + '\n'
                                ) * self.height
        print(rect, end='')

    def __str__(self):
        """Returns the string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle.

        Args:
            *args: The new attribute values, in the
            order (id, width, height, x, y).
            **kwargs: The new attribute values, as keyword arguments.

        Raises:
            TypeError: If the attribute value is not an integer.
            ValueError: If the attribute value is not greater than
            zero (if wh=True) or greater than or equal to zero (if wh=False).
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        if args:
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)

        if kwargs:
            for attr, arg in kwargs.items():
                setattr(self, attr, arg)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle.

        Returns:
            dict: The dictionary representation of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
            }
