#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    h = len(matrix)
    w = len(matrix[0]) if h > 0 else 0
    matrix2 = [[0 for x in range(w)] for y in range(h)]
    for i in range(h):
        for j in range(w):
            matrix2[i][j] = pow(matrix[i][j], 2)
    return matrix2
