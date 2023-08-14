#!/usr/bin/python3
"""This module contains a a function that returns the list of available
    attributes and methods of an object"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        Obj: The object

    Return:
        a list object
    """
    return (dir(obj))
