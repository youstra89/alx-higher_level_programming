#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_matrix = len(matrix)
    if len_matrix == 0:
        print()
    else:
        for i in range(len(matrix)):
            lst = matrix[i]
            for j in range(len(lst)):
                if j == (len(lst) - 1):
                    print("{:d}".format(lst[j]))
                else:
                    print("{:d}".format(lst[j]), end=' ')
            if i == (len(lst) - 1):
                print()
