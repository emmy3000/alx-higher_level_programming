#usr/bin/python3

"""Module: 1-my_list.py"""


class MyList(list):
    """Derived class from base class named list"""

    def __init__(self, data=[]):
        """Constructor for MyList class"""
        super().__init__(data)

    def print_sorted(self):
        """prints a sorted list of integers"""
        print(sorted(self))
