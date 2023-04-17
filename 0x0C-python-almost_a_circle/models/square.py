#!/usr/bin/python3
"""
This module defines a Square class that is a subclass of Rectangle.

Classes:
    Square: A Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object with a given size, position, and ID.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the top-left corner
            of the square. Defaults to 0.

            y (int, optional): The y-coordinate of the top-left corner
            of the square. Defaults to 0.

            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: An informal string representation of the Square object.
        """
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """
        Gets the size of the Square object.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square object to the given value.

        Args:
            value (int): The new size of the square.

        Returns:
            None.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square object based on given arguments or
        keyword arguments.

        Args:
            *args: Non-keyword arguments representing the
            new values of the object's attributes.

            **kwargs: Keyword arguments representing the
            new values of the object's attributes.

        Returns:
            None.
        """
        arg_names = ('id', 'size', 'x', 'y')
        if args:
            for name, value in zip(arg_names, args):
                setattr(self, name, value)
        elif kwargs:
            for name, value in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object.

        Returns:
            dict: A dictionary containing the attributes
            of the Square object.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
