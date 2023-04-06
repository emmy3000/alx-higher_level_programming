#!/usr/bin/python3`


def matrix_divided(matrix, div):
    """
    Function divides a matrix with the div values.

    Args:
        matrix(list): a list of lists.
        div(int or float): the number to divie each element
        of the matrix by.

    Returns:
        A new matrix.

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats.
                   if div is not an integer or a float.
                   if any row of the matrix is not the same size.
        ZeroDivisionError: if div is equal to 0.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if not all(
            isinstance(row, list) and
            all(isinstance(elements, (int, float)) for elements in row)
            for row in matrix
            ):
        raise TypeError("matrix must be a list of lists \
                containing integers or floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("All rows in matrix must be of the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("All rows in matrix must be of the same size")

    return [[round(element / div, 2) for element in row] for row in matrix]
