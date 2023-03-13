#!/usr/bin/python3

"""Program locates all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    mul_2 = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            mul_2[i] = 1
        else:
            mul_2[i] = 0
    return mul_2
