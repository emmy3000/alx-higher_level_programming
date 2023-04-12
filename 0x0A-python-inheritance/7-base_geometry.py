#!/usr/bin/python3

"""
    Module: ``7-base_geometry.py``
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
