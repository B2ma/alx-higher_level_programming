#!/usr/bin/python3
"""The base class Module"""


class Base:
    """
    The Base class

    Private class attribute:
        __nb_objects - manages id attributes in all future classes

    class constructor:
        Initialises the class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constuctor

        Args:
            id(int): Public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
