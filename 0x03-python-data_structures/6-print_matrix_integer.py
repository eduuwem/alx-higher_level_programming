#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row_list in matrix:
        print(' '.join('{:d}'.format(l)for l in row_list))
