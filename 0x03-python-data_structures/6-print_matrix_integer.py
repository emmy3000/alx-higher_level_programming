#!/usr/bin/python3

"""Program prints a matrix of integers."""


"""def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j < len(matrix[i]) - 1:
                    print("{:d} ".format(matrix[i][j]), end="")
                else:
                    print("{:d}$".format(matrix[i][j]), end='\n')"""

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(" ".join("{:d}".format(j) for j in i))
