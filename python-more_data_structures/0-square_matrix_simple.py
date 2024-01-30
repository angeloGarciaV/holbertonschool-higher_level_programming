#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    h = len(matrix)
    w = len(matrix[0]) if h > 0 else 0
    matrix2 = [[0 for x in range(w)] for y in range(h)]
    for i in range(h):
        for j in range(w):
            matrix2[i][j] = pow(matrix[i][j], 2)
    return matrix2


"""Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc."""
