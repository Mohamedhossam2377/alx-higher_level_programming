#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sub_m: list(map(lambda x: x**2, sub_m)), matrix))
