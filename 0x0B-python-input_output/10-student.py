#!/usr/bin/python3


"""
Module: ``10-stundent.py``
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
            attrs (list): A list of strings representing attributes to retrieve
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return new_dict
