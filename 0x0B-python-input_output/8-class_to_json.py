#!/usr/bin/python3
"""This module contains a  function that returns the dictionary description
    with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure (list,
    dictionary, string, integer and boolean) for JSON serialization of an
    object

    Args:
        obj: An object which is an instance of a class

    Returns:
        dictionary description with simple data structure for JSON
        serialization of an object
    """
    output = {}
    for attribute_name in dir(obj):
        if not attribute_name.startswith("__") and hasattr(obj, attribute_name):
            attribute_value = getattr(obj, attribute_name)
            if isinstance(attribute_value, (list, dict, str, int, bool)):
                output[attribute_name] = attribute_value
    return output
