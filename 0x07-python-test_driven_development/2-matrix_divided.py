#!/usr/bin/python3
"""
Matrix
"""

def matrix_divided(matrix, div):
    """Divide all elements of the matrix
    Parameters:
    matrix = matrix
    div = integer dividing elements
    Local Args:
    matrix_new = list of lists
    new_list = lists with new elements
    """

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not div:
        raise ZeroDivisionError('division by zero')

    matrix_new = []
    new_list = []
    index = len(matrix[0])
    for row in matrix:
        if len(row) != index:
            raise TypeError('Each row of the matrix must have the same size')
        if type(row) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for num in row:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
            new_list.append(round(num / div, 2))
        matrix_new.append(new_list)
        new_list = []
    return matrix_new
