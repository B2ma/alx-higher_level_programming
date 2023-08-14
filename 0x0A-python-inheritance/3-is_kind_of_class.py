#!/usr/bin/python3
"""This module contains a function that returns True if the object is an
    instance of, or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited from
    specified class

    Args:
        obj: The object to check
        a_class: The class against which object is checked

    Returns:
        True if object is instance of class, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
