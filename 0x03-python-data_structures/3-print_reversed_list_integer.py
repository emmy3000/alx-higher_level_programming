#!/usr/bin/python3

"""Function that prints all integers of a list,
in reverse order."""


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        result = len(my_list) - i
        print("{:d}".format(result), end='\n')
