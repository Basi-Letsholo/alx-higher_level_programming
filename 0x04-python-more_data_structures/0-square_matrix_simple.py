#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    m_matrix = len(matrix)

    if m_matrix < 1:
        return

    squared_matrix = []
    for i in range(0, m_matrix):
        squared_matrix.append(map(lambda x: x ** 2, matrix[i]))

    return squared_matrix
