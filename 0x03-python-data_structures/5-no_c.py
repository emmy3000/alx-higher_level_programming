#!/usr/bin/python3

"""Print that removes all characters c and C from
a string."""


def no_c(my_string):
    if my_string:
        str_list = list(my_string)
        for char in ['c', 'C']:
            while char in str_list:
                str_list.remove(char)
                my_string = "".join(str_list)
        return my_string
