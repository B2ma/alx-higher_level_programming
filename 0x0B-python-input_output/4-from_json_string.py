#!/usr/bin/python3
"""The module contains a function that returns object (Python data structure)
    represented by a JSON string"""


import json


def from_json_string(my_obj):
    """
    returns the an object (Python data structure) represented by a JSON string

    Args:
        my_str: the string to be represented

    Returns:
        object (Python data structure) represented by a JSON string
    """
    output = json.loads(my_obj)
    return output
