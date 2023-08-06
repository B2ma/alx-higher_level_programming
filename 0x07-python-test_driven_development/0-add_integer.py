#!/usr/bin/python3
"""
This module contains a function that adds two integers
and returns an integer Value.
"""


def add_integer(a, b=98):
    """A function that adds two integers

    Args:
        a(Int or float): The first integer
        b(int or float): The second integer

    Returns:
        Int: The output of the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
