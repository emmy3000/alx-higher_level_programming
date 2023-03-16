#!/usr/bin/python3

"""Program adds all unique integers in a list once
for each integer"""


def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0
    
    for i in uniq_list:
        num += i

    return (num)
