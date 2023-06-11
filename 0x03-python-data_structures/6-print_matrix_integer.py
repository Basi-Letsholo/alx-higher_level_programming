#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)

    if matrix_len <= 0:
        print(''.format())

    elif matrix_len > 0:
        for i in range(0, matrix_len):
            temp_len = len(matrix[i])
            for j in range(0, temp_len):
                print("{:d}".format(matrix[i][j]), end='')
                if j < temp_len - 1:
                    print(' '.format(), end='')
            print(''.format())
