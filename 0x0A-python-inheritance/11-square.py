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
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the rectangle description for str().

        Returns:
            str: Rectangle description as [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A Square class derived from Rectangle.
    """
    def __init__(self, size):
        """
        Instantiation with size.

        Args:
            size (int): Must be private, positive integer, and validated by
                        integer_validator.

        Raises:
            TypeError: When size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return the square description for str().

        Returns:
            str: Square description in the format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
