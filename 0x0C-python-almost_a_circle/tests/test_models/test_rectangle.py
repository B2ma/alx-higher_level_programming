#!/usr/bin/python3
"""Rectangle class unittest module"""


import unittest
import sys
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        """Test initialization of the Rectangle class."""
        r = Rectangle(5, 10, 1, 2, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_width_setter(self):
        """Test width setter."""
        r = Rectangle(5, 10)
        r.width = 15
        self.assertEqual(r.width, 15)
        with self.assertRaises(ValueError):
            r.width = -5
        with self.assertRaises(TypeError):
            r.width = "hello"

    def test_height_setter(self):
        """Test height setter."""
        r = Rectangle(5, 10)
        r.height = 20
        self.assertEqual(r.height, 20)
        with self.assertRaises(ValueError):
            r.height = -10
        with self.assertRaises(TypeError):
            r.height = "world"

    def test_x_setter(self):
        """Test x setter."""
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)
        with self.assertRaises(ValueError):
            r.x = -2
        with self.assertRaises(TypeError):
            r.x = "x-coordinate"

    def test_y_setter(self):
        """Test y setter."""
        r = Rectangle(5, 10)
        r.y = 4
        self.assertEqual(r.y, 4)
        with self.assertRaises(ValueError):
            r.y = -3
        with self.assertRaises(TypeError):
            r.y = "y-coordinate"

    def test_area(self):
        """Test the area() method."""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test the display() method."""
        r = Rectangle(3, 2, 2, 1)
        expected_output = "\n  ###\n  ###\n"
        saved_stdout = sys.stdout
        sys.stdout = io.StringIO()

        r.display()
        output = sys.stdout.getvalue()

        sys.stdout = saved_stdout

        self.assertEqual(output, expected_output)

    def test_str(self):
        """Test the __str__() method."""
        r = Rectangle(4, 8, 1, 2, 15)
        self.assertEqual(str(r), "[Rectangle] (15) 1/2 - 4/8")

    def test_update(self):
        """Test the update() method."""
        r = Rectangle(5, 10)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary() method."""
        r = Rectangle(4, 6, 2, 3, 20)
        expected_dict = {'id': 20, 'width': 4, 'height': 6, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_width_setter_invalid(self):
        """Test width setter with invalid width values."""
        r = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            r.width = -5
        with self.assertRaises(TypeError):
            r.width = "hello"

    def test_height_setter_invalid(self):
        """Test height setter with invalid height values."""
        r = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            r.height = -10
        with self.assertRaises(TypeError):
            r.height = "world"

    def test_x_setter_invalid(self):
        """Test x setter with invalid x values."""
        r = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            r.x = -2
        with self.assertRaises(TypeError):
            r.x = "x-coordinate"

    def test_y_setter_invalid(self):
        """Test y setter with invalid y values."""
        r = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            r.y = -3
        with self.assertRaises(TypeError):
            r.y = "y-coordinate"

    def test_invalid_area(self):
        """Test the area() method with invalid attributes."""
        r = Rectangle(5, 10)
        with self.assertRaises(ValueError):
            r.width = -5
            r.area()

    def test_invalid_display(self):
        """Test the display() method with invalid attributes."""
        r = Rectangle(3, 2, 2, 1)
        with self.assertRaises(ValueError):
            r.width = -3
            r.display()

    def test_invalid_to_dictionary(self):
        """Test to_dictionary() with invalid attributes."""
        r = Rectangle(4, 5, 2, 3, 25)
        with self.assertRaises(TypeError):
            r.width = "invalid"  # Set an invalid width (non-integer)
            r.to_dictionary()


if __name__ == "__main__":
    unittest.main()
