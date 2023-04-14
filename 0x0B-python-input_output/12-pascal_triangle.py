#!/usr/bin/python3

"""
Module: ``12-pascal_triangle.py``
"""


def pascal_triangle(n):
    """
    Returens a list of lists of integers representing Pascal's
    triangle of n

    Args:
        n (int): The number of rows to generate in Pascal's triangle

    Returns:
        A list of lists of integers representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    row = [1]
    result = []
    result.append(row)

    for i in range(1, n):
        row = [1] + [row[j] + row[j+1]
                for j in range(len(row) - 1)] + [1]

        result.append(row)
    return result
