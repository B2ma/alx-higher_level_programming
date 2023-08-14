#!/usr/bin/python3
"""This module contains a class MyList that inherits from list class"""


class MyList(list):
    """
    MyList class that inherits from list.

    Public Methods:
    print_sorted(): prints the list, but sorted (ascending sort)
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
