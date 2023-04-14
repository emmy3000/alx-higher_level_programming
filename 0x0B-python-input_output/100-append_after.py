 #!/usr/bin/python3

"""
Module: ``100-append_after``
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string

    Args:
        filename (str): The file to insert the new line
        search_string (str): The string to search in each line
        new_string (str): The new line to be inserted after each line
        containing the search_string
    """
    lines = []
    with open(filename, mode='r', encoding='utf-8') as mexFile:
        for line in mexFile:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as mexFile:
        mexFile.writelines(lines)
