#!/usr/bin/python3
""" This module contains matrix_divided function that divides all elements of a
        matrix"""


def matrix_divided(matrix, div):
    """A function that devides all elements of a matrix

    Args:
        matrix(int or float): list of lists of integers or floats
        div(int or float): Number to divide the matrix
    Returns:
        float: a new matrix with results of each element in the existing
        matrix divided by div and rounded to 2 decimal places
    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats
            or if div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(message)
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(message)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
