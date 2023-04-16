#!/usr/bin/python3

"""Module defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class that inherits from the
    Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int, optional): x-cordinate of the rectangle;
            Defaults to 0.
            y (int, optional): y-cordinate of the rectangle;
            Defaults to 0.
            id (int, optional): Identity of the rectange=le;
            Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Gets the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle.

            Args:
                value (int): The value to set the width to

            Raises:
                TypeError: If the value is not an integer
                ValueError: If the value is less than or equal to 0
            """
            if not instance(value, int):
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

        @property
        def height(self):
            """Gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle

            Args:
                value (int): The value to set the height of the
                rectangle to

            Raises:
                TypeError: If the value is not an integer
                ValueError: If the value is less than or equal to 0
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

        @property
        def x(self):
            """Gets the x-cordinate of the rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets the x-cordinate to the rectangle

            Args:
                value (int): The value to set the x-cordinate of
                the rectangle to

            Raises:
                TypeError: If the value is not an integer
                ValueError: If the value is less than or equal to 0
            """
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be > 0")
            else:
                self.__x = value

        @property
        def y(self):
            """Gets the y-cordinate of the rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            """Sets the x cordinate to the rectangle

            Args:
                value (int): The value to set the y-cordinate of the
                rectangle to

            Raises:
                TypeError: If the value is not an interger
                ValueError: If the value is less than or equal to 0
            """
            if not isintance(value, int):
                raise TypeError("y must be an integer")
            elif value <= 0:
                raise ValueError("y must be > 0")

        def area(self):
            """Reurns the area of the Rectangle instance"""
            return self.__width * self.__height

        def display(self):
            """Prints the Rectangle instance with '#' character"""
            for i in range(self.__y):
                print()
            for i in range(self.__height):
                for j in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print()

        def __str__(self):
            """Returns a formal string representaion of the
            Rectangle instance"""
            return "[Rectangle] ({:d}) ({:d})/({:d}) - ({:d})/({:d})".format(
                    sielf.id, self.__x, self.__y, self.__width, self.__height
                    )
