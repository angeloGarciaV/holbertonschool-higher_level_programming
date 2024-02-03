#!/usr/bin/python3
"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        matrix: matrix to divide
        div: number to divide by
    Returns:
        new_matrix
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0"""
    if type(matrix) is not list\
            or not all(type(row) is list for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    def div_matrix(x, div): return round(x / div, 2)
    new_matrix = [[div_matrix(num, div) for num in row] for row in matrix]
    return new_matrix
