#!/usr/bin/python3
"""This module contains a function that writes an Object to a text file
    using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: the object to write in JSON representation
        filename: the file to write
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
