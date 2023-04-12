#usr/bin/python3

"""
Module: `1-my_list.py`
A module that defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    Derived class from base class named list
    """

    def __init__(self, data=[]):
        """
        Constructor for MyList class.

        Args:
            data(list): list of integers.
        """
        super().__init__(data)

    def print_sorted(self):
        """
        prints a sorted list of integers

        Returns:
            None
        """
        print(sorted(self))
