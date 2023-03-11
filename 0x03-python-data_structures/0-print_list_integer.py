#!/usr/bin/python3

"""Print each integer in a list on new line"""


def print_list_integer(my_list=[]):
    for value in range(len(my_list)):
        print("{:d}".format(my_list[value]), end='\n')
