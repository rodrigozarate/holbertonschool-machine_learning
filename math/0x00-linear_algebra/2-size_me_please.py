#!/usr/bin/env python3
""" Matrix shape """


def matrix_shape(matrix):
    """ Shape of matrix """
    if type(matrix) != list or not matrix:
        return []
    return [len(matrix), *matrix_shape(matrix[0])]
