#!/usr/bin/python3
"""This module contains a class BaseGeometry that has a public instance method
    that raises an Exception with the message area() is not implemented"""


class BaseGeometry:
    """The class"""
    def area(self):
        """
        Public instance method

        Raises:
            Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
