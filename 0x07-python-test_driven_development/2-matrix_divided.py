#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Function divides a matrix with the div values.

    Args:
        matrix(list): a list of lists.
        div(int): a divisible of a matrix.

    Returns:
        A new matrix.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("divison by zero")
    if not all(isinstance(row, list) and all(isinstance(elements, (int, float)) for elements in row)for row in matrix):
            raise TypeError("matrix must be a list of lists containing integers or floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("All rows in matrix must be of the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(element/div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
