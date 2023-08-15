#!/usr/bin/python3
"""This module has a function that creates an Object from a "JSON file"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename: the JSON file
    """
    with open(filename, mode="r") as myfile:
        my_obj = json.load(myfile)
    return my_obj
