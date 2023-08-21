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
        attributes = ["id", "size", "x", "y"]
        for i, value in enumerate(args):
            if not isinstance(value, int):
                raise TypeError(f"{attributes[i]} must be an integer")
            setattr(self, attributes[i], value)

        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise TypeError(f"{key} must be an integer")
            setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square

        Returns:
            dictionary representation of a Rectangle
        """
        try:
            return {
                    'id': self.id,
                    'size': self.width, 'x': self.x, 'y': self.y}
        except TypeError as e:
            return {'error': str(e)}
