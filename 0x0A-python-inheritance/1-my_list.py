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


    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
