#!/usr/bin/python3

"""The module defines a Base class"""


class Base:
    """This is the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objets
