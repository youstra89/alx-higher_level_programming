#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_list = []
    for i in range(len(matrix)):
        my_list.append(list(map(lambda x: x**2, matrix[i])))
    return my_list
