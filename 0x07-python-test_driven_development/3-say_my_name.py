#!/usr/bin/python3
"""This module contains say_my_name function that prints My name is
    <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name(str): The first name
        last_name(str): The second name

    Raises:
        TypeError exception with the message first_name must be a
            string or last_name must be a string when first_name or
            last_name is not of string type.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    try:
        if last_name:
            print("My name is {} {}".format(first_name, last_name))
        else:
            print("My name is {} ".format(first_name),)
    except Exception as e:
        print(e)
