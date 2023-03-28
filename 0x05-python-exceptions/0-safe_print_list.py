#!/usr/bin/python3
"""Write a function that prints x elements of a list
my_list: list of element to print.
x: number of integer elements in the list to print.

Returns: number of elements printed.
"""


def safe_print_list(my_list=[], x=0):
    ret = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
