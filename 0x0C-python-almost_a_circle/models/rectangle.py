#!/usr/bin/python3
"""The rectangle Class module"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base Class

    Private instance attributes, each with its own public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y

    Class constructor:
        __init__: it Calls the super class with id - this super call with use
        the logic of the __init__ of the Base class and also Assigns each
        argument width, height, x and y to the right attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle

        Args:
            width: Rectangle width
            height: Rectagle height
            x: The x coordinate of the Rectangle
            y: The y coordinte of the Rectangle
            id: Rectangle id.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y is less than &/ equal to 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value