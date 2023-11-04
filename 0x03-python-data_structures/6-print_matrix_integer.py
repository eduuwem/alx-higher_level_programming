#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row_list in matrix:
        for new_item in row_list:
            print("{:d}".format(new_item), end=" ")
        print()
