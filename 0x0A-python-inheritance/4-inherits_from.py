#!/usr/bin/python3
"""This module contains a function that returns True if the object is an
    instance of, or if the object is an instance of a class that inherited
    (directly or indirectly) from, the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly)from specified class

    Args:
        obj: The object to check
        a_class: The class against which object is checked

    Returns:
        True if object is instance of class, otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
