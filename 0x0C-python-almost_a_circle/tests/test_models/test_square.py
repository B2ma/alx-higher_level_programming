#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        """Test initialization of the Square class."""
        s = Square(5, 2, 3, 15)
        self.assertEqual(s.id, 15)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_size_setter(self):
        """Test size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid(self):
        """Test size setter with invalid size values."""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -10
        with self.assertRaises(TypeError):
            s.size = "invalid"

    def test_str(self):
        """Test the __str__() method."""
        s = Square(6, 2, 3, 20)
        self.assertEqual(str(s), "[Square] (20) 2/3 - 6")

    def test_update(self):
        """Test the update() method."""
        s = Square(5)
        s.update(1, 8, 4, 5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_update_with_args(self):
        """Test the update() method with *args."""
        s = Square(5)
        s.update(1, 8, 4, 5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_update_with_kwargs(self):
        """Test the update() method with **kwargs."""
        s = Square(5)
        s.update(size=10, y=6)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.y, 6)

    def test_to_dictionary(self):
        """Test the to_dictionary() method."""
        s = Square(4, 2, 3, 25)
        expected_dict = {'id': 25, 'size': 4, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    # Additional test methods for other methods of the Square class
    def test_invalid_coordinates(self):
        """Test initialization with invalid coordinates."""
        with self.assertRaises(ValueError):
            Square(5, -2, 3)
        with self.assertRaises(TypeError):
            Square(5, "x", 3)

    def test_invalid_update_args(self):
        """Test update() with invalid *args."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update("invalid", 8, 4, 5)

    def test_invalid_update_args(self):
        """Test update() with invalid *args."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update("invalid", 8, 4, 5)

    def test_invalid_to_dictionary(self):
        """Test to_dictionary() with invalid attributes."""
        s = Square(4, 2, 3, 25)
        with self.assertRaises(TypeError):
            s.width = "invalid"  # Set an invalid width (non-integer)
            s.to_dictionary()


if __name__ == "__main__":
    unittest.main()
