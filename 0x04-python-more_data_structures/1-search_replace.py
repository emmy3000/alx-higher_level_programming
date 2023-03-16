#!/user/bin/python3

"""Program replaces all occurrences of an element\
by another in a new list"""


def search_replace(my_list, search, replace):
    if my_list:
        new_list = list(map(lambda x: replace if x == search else x, my_list))
        return new_list
