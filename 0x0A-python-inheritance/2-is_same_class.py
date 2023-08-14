#!/usr/bin/python3
"""This module contains a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False """


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class

    Args:
        obj: The object to be checked
        a_class: The class against which the object is checked.
    Returns:
        True if is exactly an instance of the class, otherwise returns False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
