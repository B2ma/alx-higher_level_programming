#!/usr/bin/python3
"""Unittest for max_integer([..]

"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_interger function
    """
    def test_empty_list(self):
        """
        Tests if the the function returns None for an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """
        Tests if the function correctly handles a list with single element.
        """
        self.assertEqual(max_integer([5]), 5)

    def test_posive_numbers(self):
        """
        Tests if the function correctly finds the maximum positive number
        """

        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_negative_numbers(self):
        """
        Tests if the function correctly finds the maximum negative number
        """

        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_mixed_numbers(self):
        """
        Tests if the function correctly finds maximum of mixed numbers(-/+)
        """

        self.assertEqual(max_integer([-1, 3, -2, 4]), 4)

    def test_float_numbers(self):
        """
        Tests if the function correctly finds maximum of float numbers
        """
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_float_numbers(self):
        """
        Tests if the function correctly handles a list of mixed float numbers
        """
        self.assertEqual(max_integer([1.5, -2.5, 3.5]), 3.5)

    def test_max_at_beginning(self):
        """
        Tests if the function correctly handles the maximum number at the
            beginning of the list.
        """
        self.assertEqual(max_integer([7, 4, 3, 2]), 7)

    def test_max_at_end(self):
        """
        Test if the function correctly handles the maximum number at the end
            of the list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 7]), 7)

    def test_string(self):
        """Tests a string"""
        self.assertEqual(max_integer("Malika"), 'l')

    def test_list_of_strings(self):
        """Tests list of strings"""
        self.assertEqual(max_integer(["He", "is", "Good"]), "is")


if __name__ == '__main__':
    unittest.main()
