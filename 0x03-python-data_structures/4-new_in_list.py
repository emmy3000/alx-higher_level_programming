#!/usr/bin/python3

"""Prints an element in a list at a specific position 
without modifying the original list."""


def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
