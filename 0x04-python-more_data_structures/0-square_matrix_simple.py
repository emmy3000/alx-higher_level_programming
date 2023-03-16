#!/usr/bin/python3

"""Program computes square values of all integers
in a matrix"""


def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for segment in matrix:
            squared_segment = list(map(lambda x: x ** 2, segment))
            new_matrix.append(squared_segment)
        return new_matrix
