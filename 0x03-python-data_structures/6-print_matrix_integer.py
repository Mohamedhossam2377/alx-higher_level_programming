#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for sub in range(len(matrix)):
            for i in range(len(matrix[sub])):
                if i != len(matrix[sub]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[sub][i]), end=endspace)
            print()
