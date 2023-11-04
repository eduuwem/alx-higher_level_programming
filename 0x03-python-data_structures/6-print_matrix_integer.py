#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for r in matrix:
            for k in r:
                print("{:d}".format(k), end=' ')
            print()
