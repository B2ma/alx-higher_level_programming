#!/usr/bin/python3
"""The module contains a function that returns the JSON representation
    of an object (string):"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj: the object to be represented

    Returns:
        JSON representation of my_obj
    """
    output = json.dumps(my_obj)
    return output
