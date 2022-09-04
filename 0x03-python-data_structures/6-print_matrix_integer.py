#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_matrix = len(matrix)
    if len_matrix == 0:
        print()
    else:
        for i in matrix:
            print(' '.join('{:d}'.format(j) for j in i))
