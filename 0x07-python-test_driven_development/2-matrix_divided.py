#!/usr/bin/python3
""""
    Modulus that divides a matrix
    matrix: matrix to be divided
    div: divisor
"""


def matrix_divided(matrix, div):
    """
        Function that divides a matrix
    """
    i = 0
    if type(div) != int or type(div) != float:
        TypeError("div must be a number")
    if div == 0:
        ZeroDivisionError("division by zero")
    if not any (matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix[0] is not None:
        i = len(matrix[0])
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for value in row:
            if type(value) != int and type(value) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != i:
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(value / div, 2) for value in row] for row in matrix]
