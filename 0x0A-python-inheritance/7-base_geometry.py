#!/usr/bin/python3
"""This module contains a class BaseGeometry that has two public instance
    methods area and integer_validator"""


class BaseGeometry:
    """The class"""
    def area(self):
        """
        Public instance method

        Raises:
            Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value

        Args:
            name(str): always a string
            value (int): raises TypeError if value is not int or ValueError
                if value is less or equal to 0
        Raises:
            TypeError: When value is not integer
            ValueError: If value is lees or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
