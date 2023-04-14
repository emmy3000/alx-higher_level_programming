#!/usr/bin/python3


"""
Module: ``11-stundent.py``
"""


class Student:
    """
    Student class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance

        Return:
            attrs (list): A list of strings representing attributes
            to retrieve, Defaults to None which retrieves all attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        those from a dictionary

        Args:
            json (dict): A dictionary representation of the
            Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
