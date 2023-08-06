#!/usr/bin/python3
"""This module contains print_square function that prints a square with the
    character #"""


def print_square(size):
    """
    a function that prints a square with the character #

    Args:
        size(int): the size length of the square
    Raises:
        TypeError: if size is not an integeror is a float and less than 0
            TypeError is raised with the exception message size must be an
            integer.
        ValueError: if size is less than Zero with exception message
            size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
