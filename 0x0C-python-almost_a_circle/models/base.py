#!/usr/bin/python3
"""The base class Module"""
import json
import csv


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
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("Input must be a list.")

        for item in list_dictionaries:
            if not isinstance(item, dict):
                raise TypeError("Each item in the list must be a dictionary.")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list_objs(list): a list of instances who inherits of Base
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(obj_list)
        with open(filename, mode="w", encoding="utf-8") as myfile:
            myfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
            json_string: the string representing dictionaries

        Returns:
            list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []

        try:
            output = json.loads(json_string)
            if not isinstance(output, list):
                raise TypeError("JSON string does not represent a list.")
            for item in output:
                if not isinstance(item, dict):
                    raise TypeError(
                            "Each item in the list must be a dictionary.")
            return output
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string.")

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set

        Args:
            **dictionary:  a double pointer to a dictionary

        Returns:
            instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            sample = cls(1, 1)
        elif cls.__name__ == "Square":
            sample = cls(1)
        else:
            sample = None
        sample.update(**dictionary)
        return sample

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances

        Returns:
            List of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as myfile:
                json_string = myfile.read()
                obj_list = cls.from_json_string(json_string)
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, mode="r", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(
                                int(row[1]),
                                int(row[2]), int(row[3]), int(row[0]))
                    obj_list.append(obj)
            return obj_list
        except FileNotFoundError:
            return []
