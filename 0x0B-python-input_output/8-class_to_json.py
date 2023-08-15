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
    for attribut_name in dir(obj):
        if not attribut_name.startswith("__") and hasattr(obj, attribut_name):
            attribut_value = getattr(obj, attribut_name)
            if isinstance(attribut_value, (list, dict, str, int, bool)):
                output[attribut_name] = attribut_value
    return output
