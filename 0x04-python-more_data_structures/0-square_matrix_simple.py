#!/usr/bin/python3

# Computes the square value of all integers of a matrix


def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])
