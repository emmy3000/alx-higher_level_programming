#!/usr/bin/python3

"""Program that locates the biggest integer of a list"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    biggest = my_list[0]
    for i in range(1, len(my_list)):
        if biggest < my_list[i]:
            biggest = my_list[i]
        else:
            continue
    return biggest
