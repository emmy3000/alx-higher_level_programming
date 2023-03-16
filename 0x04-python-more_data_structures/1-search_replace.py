#!/user/bin/python3

"""Program replaces all occurrences of an element
by another in a new list"""


def search_replace(my_list, search, replace):
    def replace_operation(element):
        return (element if element != search else replace)
    return list(map(replace_operation, my_list))
