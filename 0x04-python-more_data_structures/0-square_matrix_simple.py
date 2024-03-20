#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for k in matrix:
        squared_k = []
        for element in k:
            squared_k.append(element ** 2)
        squared.append(squared_k)
    return squared
