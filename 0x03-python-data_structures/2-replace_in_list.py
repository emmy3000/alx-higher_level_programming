#!/usr/bin/python3

"""Prints an element of a list at a sprecific
position"""


def replace_in_list(my_list, idx, element):
    if not my_list or idx < 0 or idx >= len(my_list):
        return None
    else:
        my_list[idx] = element
        return my_list
