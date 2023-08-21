#!/usr/bin/python3
"""Base class unittest  module"""

import unittest
import json
import os
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def setUp(self):
        """
        Set up test environment before each test method.
        """
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """
        Clean up after each test method.
        """
        pass

    def test_instance_creation(self):
        """
        Test the creation of instances and the assignment of IDs.
        """
        # Test Step 1
        instance1 = Base()
        self.assertEqual(instance1.id, 1, "Instance 1 ID mismatch")

        # Test Step 2
        instance2 = Base()
        self.assertEqual(instance2.id, 2, "Instance 2 ID mismatch")

        # Test Step 3
        specified_id = 100
        instance3 = Base(id=specified_id)
        self.assertEqual(instance3.id, specified_id, "Instance 3 ID mismatch")

    def test_instance_id_assignment(self):
        """
        Test the correct assignment of IDs to instances.
        """
        instance1 = Base()
        instance2 = Base()
        instance3 = Base(id=10)
        self.assertEqual(instance1.id, 1, "Instance 1 ID assignment mismatch")
        self.assertEqual(instance2.id, 2, "Instance 2 ID assignment mismatch")
        self.assertEqual(instance3.id, 10, "Instance 3 ID assignment mismatch")

    def test_to_json_string_empty_list(self):
        """
        Test to_json_string method with an empty list.
        """
        dictionary_list = []
        json_string = Base.to_json_string(dictionary_list)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_non_empty_list(self):
        """
        Test to_json_string method with a non-empty list of dictionaries.
        """
        dictionary_list = [{'key': 'value'}, {'another_key': 'another_value'}]
        json_string = Base.to_json_string(dictionary_list)
        expected_json = json.dumps(dictionary_list)
        self.assertEqual(json_string, expected_json)

    def test_to_json_string_non_empty_list_invalid_dicts(self):
        """
        Test to_json_string method with a non-empty list containing
        non-dictionaries.
        """
        non_dict_list = ['string', 123, None]
        with self.assertRaises(TypeError):
            Base.to_json_string(non_dict_list)

    def test_save_to_file_empty_list(self):
        """
        Test save_to_file method with an empty list of instances.
        """
        instance_list = []
        filename = "Base.json"
        Base.save_to_file(instance_list)
        self.assertTrue(
            os.path.exists(filename), f"File '{filename}' not found")
        with open(filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_non_empty_list(self):
        """
        Test save_to_file method with a non-empty list of instances.
        """
        instance1 = Rectangle(10, 20)
        instance2 = Square(5)
        instance_list = [instance1, instance2]
        filename = f"{Base.__name__}.json"
        Base.save_to_file(instance_list)
        self.assertTrue(
            os.path.exists(filename), f"File '{filename}' not found")
        with open(filename, "r") as file:
            content = file.read()
            expected_content = Base.to_json_string(
                [instance1.to_dictionary(), instance2.to_dictionary()])
            self.assertEqual(content, expected_content)

    def test_from_json_string_valid_input(self):
        json_string = '[{"key": "value"}, {"another_key": "another_value"}]'
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)
        self.assertListEqual(result, [{"key": "value"},
                                      {"another_key": "another_value"}])

    def test_from_json_string_invalid_input(self):
        invalid_json_string = "invalid json"
        with self.assertRaises(ValueError):
            Base.from_json_string(invalid_json_string)

    def test_from_json_string_empty_input(self):
        empty_json_string = ""
        result = Base.from_json_string(empty_json_string)
        self.assertIsInstance(result, list)
        self.assertListEqual(result, [])

    def test_from_json_string_non_string_input(self):
        non_string_input = 123  # Example non-string input
        with self.assertRaises(TypeError):
            Base.from_json_string(non_string_input)

    def test_load_from_file_rectangle(self):
        """
        Test loading instances of Rectangle from file.
        """
        filename = "Rectangle.json"
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

        # Create instances and save them to file
        rect1 = Rectangle(10, 20)
        rect2 = Rectangle(5, 10)
        rect_list = [rect1, rect2]
        Rectangle.save_to_file(rect_list)

        # Load instances from file
        loaded_rectangles = Rectangle.load_from_file()

        # Check if loaded instances match the original instances
        self.assertIsInstance(loaded_rectangles, list)
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[0].width, rect1.width)
        self.assertEqual(loaded_rectangles[0].height, rect1.height)
        self.assertEqual(loaded_rectangles[1].width, rect2.width)
        self.assertEqual(loaded_rectangles[1].height, rect2.height)

    def test_load_from_file_square(self):
        """
        Test loading instances of Square from file.
        """
        filename = "Square.json"
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

        # Create instances and save them to file
        square1 = Square(5)
        square2 = Square(10)
        square_list = [square1, square2]
        Square.save_to_file(square_list)

        # Load instances from file
        loaded_squares = Square.load_from_file()

        # Check if loaded instances match the original instances
        self.assertIsInstance(loaded_squares, list)
        self.assertEqual(len(loaded_squares), 2)
        self.assertIsInstance(loaded_squares[0], Square)
        self.assertIsInstance(loaded_squares[1], Square)
        self.assertEqual(loaded_squares[0].size, square1.size)
        self.assertEqual(loaded_squares[1].size, square2.size)

    def test_create_rectangle(self):
        """Test create method for Rectangle class."""
        rect_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 3, 'y': 4}
        rect_instance = Rectangle.create(**rect_dict)

        self.assertIsInstance(rect_instance, Rectangle)
        self.assertEqual(rect_instance.id, 1)
        self.assertEqual(rect_instance.width, 10)
        self.assertEqual(rect_instance.height, 20)
        self.assertEqual(rect_instance.x, 3)
        self.assertEqual(rect_instance.y, 4)

    def test_create_square(self):
        """Test create method for Square class."""
        square_dict = {'id': 2, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)

        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)


if __name__ == '__main__':
    unittest.main()
