#!/usr/bin/python3
"""The pascal_triangle module"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n

    Args:
        n(int): number of rows
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for i in range(1, n):
        initial_row = pascal_triangle[i - 1]
        next_row = [1]

        for j in range(1, i):
            new_val = initial_row[j - 1] + initial_row[j]
            next_row.append(new_val)

        next_row.append(1)
        pascal_triangle.append(next_row)

    return pascal_triangle
