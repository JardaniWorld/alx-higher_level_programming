#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    array = [list(map(lambda x: x*x, value)) for value in matrix]
    return array
