#!/usr/bin/python3

"""This module contains a class Square that defines a square
"""


class Square:
    """
    Defines a square by: (based on 0-square.py)
    Attributes:
        __size (int): The size of the square.
    Methods:
        __init__(self, size): Initializes a Square instance.
    """
    def __init__(self, size):
        """
        Initializes a Square instance
        Parameters:
            size: the size of the square
        """
        self.__size = size
