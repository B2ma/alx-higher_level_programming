#!/usr/bin/python3
"""The base class Module"""
import json


class Base:
    """
    The Base class

    Private class attribute:
        __nb_objects - manages id attributes in all future classes

    class constructor:
        Initialises the class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constuctor

        Args:
            id(int): Public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries(list): list of dictionaries

        Returns:
            [] or JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list_objs(list): a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        obj_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(obj_list)
        with open(filename, mode="w", encoding="utf-8") as myfile:
            myfile.write(json_string)
