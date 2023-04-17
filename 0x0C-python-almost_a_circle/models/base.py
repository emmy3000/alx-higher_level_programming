#!/usr/bin/python3
"""
This module defines the base class for all other classes in the project.

Classes that inherit from this base class will have a unique identifier and
methods for converting instances to dictionaries and JSON strings.
"""

import json


class Base:
    """
    This class serves as the base class for all other classes in the project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the id attribute.

        If id is None, then the class attribute __nb_objects is incremented
        and assigned as the id value for the instance. Otherwise, the given id
        value is assigned to the instance's id attribute.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of objects represented by the given JSON string.

        Args:
            json_string (str): A string representing a JSON-encoded
            list of dictionaries.

        Returns:
            list: A list of objects.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file named <ClassName>.json.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Creates and returns an instance of the class with all attributes set
        based on a dictionary of attribute key-value pairs.

        Args:
            **dictionary: A dictionary of attribute key-value pairs.

        Returns:
            An instance of the class with all attributes set based on the
            provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            instance = None
        if instance:
            instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Loads and returns a list of instances of the class from a JSON file.

        Returns:
            A list of instances of the class loaded from the JSON file. If the
            file does not exist, an empty list is returned.
        """
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, mode="r", encoding="utf-8") as f:
            return [cls.create(**dict) for dict in
                    Base.from_json_string(f.read())]
