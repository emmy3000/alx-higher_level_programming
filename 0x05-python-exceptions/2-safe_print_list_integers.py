#!/usr/bin/python3

"""Print the first x elements of a list only in integers

my_list: List of where elements are printed from.
x: number of elements in list my_list

Returns: number of integers printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i], end=""))
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
