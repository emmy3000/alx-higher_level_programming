#!/usr/bin/python3

"""
    N-Queens Solver: A Python Backtracking Algorithm

"""

import sys


def is_safe(board, row, col, n):
    """checks safety of a queen placed at board[row][col]
        starting from the left side"""

    for i in range(col):
        if board[row][i]:
            return False

    """checking upper diagonal position by the left"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    """checking lower diagonal position by the left"""
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_n_queens(board, col, n, result):
    """solution to n queens problem using a recursive approach"""

    if col == n:
        queens = []
        for i in range(n):
            for j in range(n):
                if board[i][j]:
                    queens.append([i, j])

        result.append(queens)
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, col + 1, n, result)
            board[row][col] = 0


def nqueens(n):
    """returns a list to all possible solutions to
    N-queens problem."""

    board = [[0 for i in range(n)] for j in range(n)]
    result = []
    solve_n_queens(board, 0, n, result)
    return result


if __name__ == '__main__':
    """Parsing args from the command line"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N\n N -> Integer greater or equal to 4.")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")

    if n < 4:
        print("Error: The input value N must be at least 4.")
        sys.exit(1)

    """Initializing the board"""
    board = [[0 for i in range(n)] for j in range(n)]
    result = []

    """n queens solution"""
    solve_n_queens(board, 0, n, result)

    for queens in result:
        print(queens)
