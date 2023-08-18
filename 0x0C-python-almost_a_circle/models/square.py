#!/usr/bin/python3
"""Square Class module that inherits from Rectangle Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor

        Args:
            size(int): the square size
            x(int): x coordinate
            y(int): y coordinate
            id(int): Squre unique id

        Raises:
            TypeError: If size, x, or y is not an integer.
            ValueError: If size, x, or y is less than &/ equal to 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square based on arguments.

        Args:
            *args: Variable arguments in the order: id, size, x, y.
            **kwargs: Key-value arguments for attribute updates.
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
