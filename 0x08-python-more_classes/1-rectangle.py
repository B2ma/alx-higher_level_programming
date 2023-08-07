#!/usr/bin/python3
"""This module contains an empty class that defines a rectangle"""


class Rectangle:
    """An empty class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes the data

        Args:
            width (int): The rectangle's width with 0 as default
            height(int): The rectangle's height with 0 as default
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter metthod for width attribute

        Args:
            value (int): The width value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than Zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.

        Returns:
            int: The rectangle's height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        Args:
            value (int): The height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
