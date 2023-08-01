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
        self.size = size

    @property
    def size(self):
        """
        Retrieves size of square
        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Parameters:
            value (int): new square size.
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute
        Parameters:
            value (tuple): The new position of the square (row, column)
        Raises:
            TypeError: If the value is not a tuple of 2 positive integers
            ValueError: If the value doesnt meet the position requirements
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        row, col = value
        if any(not isinstance(val, int) or val < 0 for val in position):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square
        Returns:
            int: Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'
        If the size is equal to 0, it prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
