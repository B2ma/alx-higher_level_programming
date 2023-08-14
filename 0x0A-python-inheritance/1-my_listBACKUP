#!/usr/bin/pythom3
"""This module contains a class that inherits from list class"""


class MyList(list):
    """
    Mylist class that inherits from list .

    Only integer values are allowed in the list.

    Public Methods:
    print_sorted(): prints the list, but sorted (ascending sort)

    Attributes:
    Inherits all attributes of the built-in list class.
    """

    def __init__(self, iterable=None):
        """
        Initializes MyList.

        Args:
        iterable (iterable, optional): An iterable of integers.

        Raises:
        ValueError: If any element in the iterable is not an integer.
        """
        if iterable is None:
            iterable = []
        for i in iterable:
            if not isinstance(i, int):
                raise ValueError("Should be intergers only")
        super().__init__(iterable)

    def append(self, value):
        """
        Appends an integer value at the end of the list.

        Args:
        value (int): The value to append.

        Raises:
        ValueError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError("Should be intergers only")
        super().append(value)

    def extend(self, iterable):
        """
        Extend the list with integer values.

        Args:
        iterable (iterable): An iterable containing integers.

        Raises:
        ValueError: If any element in the iterable is not an integer.
        """
        for value in iterable:
            if not isinstance(value, int):
                raise ValueError("Should be intergers only")
        super().extend(iterable)

    def insert(self, index, value):
        """
        Insert a value at a specific index in the list.

        Args:
        index (int): The index at which to insert the value.
        value (int): The value to insert.

        Raises:
        ValueError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError("Should be intergers only")
        super().insert(index, value)

    def __setitem__(self, index, value):
        """
        Set the value of an element at a specific index in the list.

        Args:
        index (int): The index of the element to set.
        value (int): The value to set.

        Raises:
        ValueError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError("Should be intergers only")
        super().__setitem__(index, value)

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
