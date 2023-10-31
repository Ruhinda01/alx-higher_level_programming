#!/usr/bin/python3
"""matrix divided module"""


def matrix_divided(matrix, div):
    """
    divides a matrix
    Args:
        matrix : matrix passes
        div (int): integer
    Raises:
        TypeError: matrix must be a matrix of integers/floats
        ZeroDivisionError: division by zero
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    rows = len(matrix)
    columns = len(matrix[0])

    for r in range(rows):
        if len(matrix[r]) != columns:
            raise TypeError("Each row of the matrix must have the same size")
    result_matrix = [[0 for c in range(columns)] for r in range(rows)]
    for i in range(rows):
        for j in range(columns):
            value = matrix[i][j]
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                result_matrix[i][j] = float("{:.2f}".format(matrix[i][j] / div))
    return result_matrix
