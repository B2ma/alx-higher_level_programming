#!/usr/bin/python3
"""This module contains a derived class Rectangle that inherits from
    BaseGeometry. it also contains init method for instantiation"""


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


class Rectangle (BaseGeometry):
    """
    A Rectangle class derived from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instatiation with width and height

        Args:
            width(int): must be private, positive integers and validated by
            integer_validator
            height(int): must be private, positive integers and validated by
            integer_validator
        Raises:
            TypeError: When width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
