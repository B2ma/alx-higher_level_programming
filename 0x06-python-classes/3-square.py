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
    def __init__(self, size=0):
        """
        Initializes a Square instance
        Parameters:
            size(int, optional): the size of the square with 0 as default.
                                Must be an integer, and if provided,
                                must be >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns:
            int: Area of the square
        """
        return self.__size ** 2
