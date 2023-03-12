#!/usr/bin/python3

"""Prints return value of element retreived and its
    index position"""


def element_at(my_list, idx):
    if not my_list or idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
