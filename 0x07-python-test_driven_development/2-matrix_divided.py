#!/usr/bin/python3
""" Matrix Divided module. """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) > 1:
        for i in range(1, len(matrix)):
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError("each row of the matrix must have the same size")
            
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix
